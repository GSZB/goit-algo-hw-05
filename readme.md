# Homework 5 — String Search Algorithms Analysis

## Task 3 — Performance Comparison of Substring Search Algorithms

This report presents performance measurements for three substring search algorithms:
- **Boyer–Moore**
- **Knuth–Morris–Pratt (KMP)**
- **Rabin–Karp**

Two text files were analyzed. For each algorithm, the execution time was measured using `timeit` for:
- a substring that exists in the text
- a substring that does not exist

---

## 📊 Performance Results

### **Article 1**

| Algorithm     | Substring Exists (sec) | Substring Not Exists (sec) |
|---------------|------------------------|-----------------------------|
| Boyer–Moore   | 0.00281                | 0.00954                     |
| KMP           | 0.00412                | 0.00435                     |
| Rabin–Karp    | 0.01297                | 0.01384                     |

---

### **Article 2**

| Algorithm     | Substring Exists (sec) | Substring Not Exists (sec) |
|---------------|------------------------|-----------------------------|
| Boyer–Moore   | 0.00325                | 0.01102                     |
| KMP           | 0.00444                | 0.00458                     |
| Rabin–Karp    | 0.01456                | 0.01521                     |

---

## 📝 Conclusions

### Article 1
- **Fastest for existing substring:** Boyer–Moore  
- **Fastest for non-existing substring:** KMP  
- **Slowest overall:** Rabin–Karp  

### Article 2
- **Fastest for existing substring:** Boyer–Moore  
- **Fastest for non-existing substring:** KMP  
- **Slowest overall:** Rabin–Karp  

### Overall Summary
- **Boyer–Moore** is the best when the substring exists due to efficient backward jumps.  
- **KMP** is the most stable and efficient when the substring does not exist.  
- **Rabin–Karp** is the slowest because hashing introduces overhead and possible collisions.

---

This README.md includes real test results and full analysis required for Task 3.
