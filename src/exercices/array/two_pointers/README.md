# Two Pointers Technique

## 🎯 Concept
Two pointers technique uses two indices moving through an array:
- **Opposite ends**: Start from beginning and end, move toward center
- **Same direction**: Both pointers move forward at different speeds
- **Fast/Slow**: One pointer moves faster than the other

## 📚 Problems in this folder:

### `product_nums_list_execept_itself.ipynb`
- **Technique**: Left and right pass with pointers
- **Pattern**: Calculate products excluding current element
- **Key insight**: Two passes - left products, then right products

### `rotation_array.ipynb`
- **Technique**: Multiple pointer operations for rotation
- **Pattern**: Array rotation and reversal
- **Key insight**: Rotate by reversing subarrays

### `picking-numbers.ipynb`
- **Technique**: Two pointers for adjacent value analysis
- **Pattern**: Find longest subarray with difference ≤ 1
- **Key insight**: Sort first, then use sliding window

## 💡 Common Patterns:
1. **Opposite Pointers**: 
   ```python
   left, right = 0, len(arr) - 1
   while left < right:
       # process arr[left] and arr[right]
       left += 1
       right -= 1
   ```

2. **Same Direction**: 
   ```python
   slow = fast = 0
   while fast < len(arr):
       # move fast pointer
       if condition:
           slow += 1
   ```

3. **Three Pointers**:
   ```python
   i = 0
   for j in range(len(arr)):
       if condition:
           arr[i] = arr[j]
           i += 1
   ```