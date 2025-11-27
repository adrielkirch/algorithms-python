# Array Operations Problems

## 📊 Concept
Problems involving array traversal, queries, and element-wise operations with specific rules.

## 🎯 Key Patterns
- **Range queries**: Answer queries about array ranges
- **Element counting**: Count elements meeting criteria
- **Index manipulation**: Handle circular arrays, rotations
- **Filtering**: Select elements based on conditions

## 📚 Problems

### `apple_orange_thrown_distance.ipynb`
**Pattern**: Range checking
- Calculate landing positions
- Count items within target range
**Key insight**: `start <= position <= end` check

### `circular_array_rotation.ipynb`
**Pattern**: Circular array queries
- Rotate array k times
- Answer multiple index queries
**Key insight**: 
  - New position = `(i - k) % n`
  - Or rotate once: move last k elements to front

### `service_lane.ipynb`
**Pattern**: Range minimum query
- Find minimum value in range [i, j]
- Multiple queries on same array
**Key insight**: Simple iteration for each range (or use segment tree for optimization)

## 💡 Common Approach
```python
# Range checking
def count_in_range(arr, start, end, transform):
    count = 0
    for val in arr:
        position = transform(val)
        if start <= position <= end:
            count += 1
    return count

# Circular rotation
def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

# Range query
def range_min(arr, i, j):
    return min(arr[i:j+1])
```

## 🔗 Related Patterns
- Array manipulation
- Range queries
- Circular arrays
- Modulo arithmetic
