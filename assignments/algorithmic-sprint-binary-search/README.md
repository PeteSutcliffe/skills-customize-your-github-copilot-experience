# 📘 Assignment: Algorithmic Sprint — Binary Search & Two‑Pointer Optimization

## 🎯 Objective

Students will implement binary search and the two‑pointer technique in Python, use them to solve array/search problems, and compare their performance to naive approaches.

## 📝 Tasks

### 🛠️ Implement Binary Search

#### Description
Write an efficient binary search function that finds the index of a target value in a sorted list.

#### Requirements
Completed program should:

- Implement `binary_search(arr, target)` (iterative or recursive) that returns the index of `target` or `-1` if not found.
- Include example input/output and at least two test cases (found and not found).
- Explain the time complexity (in comments or README) and compare to linear search.

```
Example:
binary_search([1,2,3,4,5], 4) -> 3
binary_search([1,2,3], 7) -> -1
```

### 🛠️ Two‑Pointer Optimization: Pair Sum

#### Description
Given a sorted list of integers and a target sum, implement a two‑pointer solution to find a pair of values that add up to the target.

#### Requirements
Completed program should:

- Implement `two_pointer_pair_sum(arr, target)` that returns a tuple `(i, j)` of indices, or `None` if no pair exists.
- Compare the two‑pointer approach to a naive O(n^2) approach in comments and note the complexity.
- Include at least two example test cases.

```
Example:
two_pointer_pair_sum([1,2,3,4,6], 6) -> (1,3)  # values 2 and 4
```

---

Files:

- Starter code: `starter-code.py`
