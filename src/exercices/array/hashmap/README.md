# HashMap/Hash Table Techniques

## 🎯 Concept
Hash tables (dictionaries/maps) provide O(1) average-case lookup time, making them perfect for:
- **Frequency counting**: Count occurrences of elements
- **Duplicate detection**: Check if element already exists
- **Fast lookups**: Quick access to previously seen data
- **Set operations**: Union, intersection, difference

## 📚 Problems in this folder:

### `3sum_no_repete_equals_zero.ipynb`
- **Technique**: HashSet to avoid duplicate triplets
- **Pattern**: Three-sum with uniqueness constraint
- **Key insight**: Use set to track seen combinations

### `exists_dup_in_array.ipynb`
- **Technique**: HashSet for duplicate detection
- **Pattern**: Contains duplicate check
- **Key insight**: Add elements to set, return true if already exists

### `most_frequent_migratory_bird.ipynb`
- **Technique**: HashMap for frequency counting
- **Pattern**: Find most frequent element
- **Key insight**: Count frequencies, find maximum

### `remove_dup_in_array.ipynb`
- **Technique**: HashSet to track unique elements
- **Pattern**: Remove duplicates while preserving order
- **Key insight**: Only add to result if not seen before

### `socks_pairs.ipynb`
- **Technique**: HashMap for counting pairs
- **Pattern**: Count pairs from frequencies
- **Key insight**: pairs = frequency // 2

## 💡 Common Patterns:
1. **Frequency Counter**: `counter[key] = counter.get(key, 0) + 1`
2. **Seen Set**: `if item in seen: return True; seen.add(item)`
3. **Two Sum Pattern**: `if target - num in seen: return True`
4. **Group by Key**: `groups[key].append(value)`