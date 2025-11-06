# Binary Search Techniques

## 🎯 Concept
Binary search efficiently finds elements in sorted data or searches for conditions:
- **Classic binary search**: Find exact element in sorted array
- **Lower/Upper bound**: Find insertion points
- **Search on answer**: Binary search on possible answers
- **Peak finding**: Find local maxima/minima

## 📚 Problems in this folder:

### `climbing_the_leaderboard.ipynb`
- **Technique**: Modified binary search for ranking
- **Pattern**: Dense ranking with binary search optimization
- **Key insight**: Use binary search concepts to find rank position efficiently

## 💡 Common Patterns:
1. **Classic Binary Search**:
   ```python
   def binary_search(arr, target):
       left, right = 0, len(arr) - 1
       
       while left <= right:
           mid = (left + right) // 2
           if arr[mid] == target:
               return mid
           elif arr[mid] < target:
               left = mid + 1
           else:
               right = mid - 1
       return -1
   ```

2. **Lower Bound** (first position >= target):
   ```python
   def lower_bound(arr, target):
       left, right = 0, len(arr)
       
       while left < right:
           mid = (left + right) // 2
           if arr[mid] < target:
               left = mid + 1
           else:
               right = mid
       return left
   ```

3. **Search on Answer**:
   ```python
   def search_answer(condition_func, low, high):
       while low < high:
           mid = (low + high) // 2
           if condition_func(mid):
               high = mid
           else:
               low = mid + 1
       return low
   ```

## ⚡ Time Complexity:
- O(log n) for each search operation
- Significantly faster than linear search O(n)

## ✅ When to Use:
- Data is sorted (or can be sorted)
- Searching for specific values or conditions
- Finding boundaries or insertion points
- Optimizing over a range of possible answers