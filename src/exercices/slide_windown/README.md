# Sliding Window Technique

## 🎯 Concept
Sliding window maintains a "window" of elements and slides it across the array:
- **Fixed size**: Window size remains constant
- **Variable size**: Window expands/contracts based on conditions
- **Two pointers**: Usually implemented with left and right pointers

## 📚 Problems in this folder:

### `max_sum_in_subarray.ipynb`
- **Technique**: Kadane's algorithm (variable window)
- **Pattern**: Maximum subarray sum
- **Key insight**: Extend window when sum positive, reset when negative

### `max_sum_in _slide_windown.ipynb`
- **Technique**: Fixed-size sliding window
- **Pattern**: Maximum sum in fixed-size subarray
- **Key insight**: Slide window by removing left element, adding right element

### `the-birthday-choco-bar.ipynb`
- **Technique**: Variable sliding window
- **Pattern**: Count subarrays with specific sum
- **Key insight**: Expand window until sum >= target, then contract

## 💡 Common Patterns:
1. **Fixed Window**:
   ```python
   window_sum = sum(arr[:k])  # initial window
   max_sum = window_sum
   
   for i in range(k, len(arr)):
       window_sum = window_sum - arr[i-k] + arr[i]
       max_sum = max(max_sum, window_sum)
   ```

2. **Variable Window**:
   ```python
   left = 0
   for right in range(len(arr)):
       # expand window
       while condition_violated:
           # contract window
           left += 1
   ```

3. **Kadane's Algorithm**:
   ```python
   max_sum = current_sum = arr[0]
   for i in range(1, len(arr)):
       current_sum = max(arr[i], current_sum + arr[i])
       max_sum = max(max_sum, current_sum)
   ```

## ⚡ Time Complexity:
- Usually O(n) - each element visited at most twice
- Much better than brute force O(n²) or O(n³)