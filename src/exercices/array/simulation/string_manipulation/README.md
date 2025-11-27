# String Manipulation Problems

## 🔤 Concept
Problems involving string transformations using specific operations like append, delete, or replace.

## 🎯 Key Patterns
- **Operation counting**: Determine minimum operations needed
- **Transformation feasibility**: Check if transformation is possible
- **Common prefix/suffix**: Leverage shared parts
- **Operation sequences**: Find optimal sequence of operations

## 📚 Problems

### `append_and_delete.ipynb`
**Pattern**: String transformation with operation limit
- Transform string s to string t
- Operations: delete from end, append to end
- Must use exactly k operations
**Key insight**: 
  - Find common prefix length
  - Calculate deletions needed + additions needed
  - Check if k operations can achieve it (accounting for extra operations)

## 💡 Common Approach
```python
def transform_string(s, t, k):
    # Find common prefix
    common = find_common_prefix(s, t)
    
    # Calculate operations needed
    deletions = len(s) - common
    additions = len(t) - common
    min_ops = deletions + additions
    
    # Check if exactly k operations possible
    if k >= min_ops and (k - min_ops) % 2 == 0:
        return "Yes"
    if k >= len(s) + len(t):  # Can delete all and rebuild
        return "Yes"
    return "No"
```

## 🔗 Related Patterns
- Edit distance
- Longest common subsequence
- String algorithms
