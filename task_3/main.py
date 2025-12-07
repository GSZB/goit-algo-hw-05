import timeit


def kmp_search(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        j = 0

        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
        return lps

    lps = build_lps(pattern)
    i = j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def rabin_karp_search(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)

    h = pow(d, m - 1) % q
    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return -1


def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)

    if m > n:
        return -1

    skip = {pattern[i]: i for i in range(m)}

    i = m - 1

    while i < n:
        j = m - 1
        k = i

        while j >= 0 and text[k] == pattern[j]:
            j -= 1
            k -= 1

        if j == -1:
            return k + 1

        i += m - 1 if text[i] not in skip else m - 1 - skip[text[i]]

    return -1


def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def measure(func, text, pattern):
    t = timeit.timeit(lambda: func(text, pattern), number=10)
    return t


def main():
    text1 = load_text("article1.txt")
    text2 = load_text("article2.txt")

    existing_substring = "the"
    fake_substring = "qwertyuiop123456"

    algorithms = {
        "KMP": kmp_search,
        "Rabin-Karp": rabin_karp_search,
        "Boyer-Moore": boyer_moore_search,
    }

    for idx, text in enumerate([text1, text2], start=1):
        print(f"\n=== TEXT {idx} ===")

        for pattern_name, func in algorithms.items():
            t1 = measure(func, text, existing_substring)
            t2 = measure(func, text, fake_substring)
            print(f"{pattern_name}: existing={t1:.6f}s | fake={t2:.6f}s")


if __name__ == "__main__":
    main()
