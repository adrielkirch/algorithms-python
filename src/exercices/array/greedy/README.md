# Greedy Algorithms

## 🎯 Concept
Greedy algorithms make locally optimal choices at each step, hoping to find a global optimum:
- **Local optimization**: Make the best choice available at each step
- **No backtracking**: Once a choice is made, never reconsider it
- **Proof required**: Must prove that local choices lead to global optimum

## 📚 Problems in this folder:

### `min_buy_and_max_sell_profit.ipynb`
- **Technique**: Greedy - track minimum price seen so far
- **Pattern**: Buy low, sell high optimization
- **Key insight**: Always buy at lowest price encountered, sell at current price

### `eletronic_max_usb_keyboard_price.ipynb`
- **Technique**: Greedy - maximize spending within budget
- **Pattern**: Knapsack-like optimization with budget constraint
- **Key insight**: Choose most expensive items within budget

### `basket_min_max_records_counter.ipynb`
- **Technique**: Greedy - track records as they're broken
- **Pattern**: Running minimum/maximum tracking
- **Key insight**: Update records only when current value beats previous record

## 💡 Common Patterns:
1. **Running Optimum**:
   ```python
   best = float('inf')  # or -inf for maximum
   for item in items:
       if item < best:  # or > for maximum
           best = item
           # record the choice
   ```

2. **Interval Scheduling**:
   ```python
   # Sort by end time, pick non-overlapping
   intervals.sort(key=lambda x: x[1])
   ```

3. **Resource Allocation**:
   ```python
   # Sort by efficiency/cost ratio
   items.sort(key=lambda x: x.value / x.cost, reverse=True)
   ```

## ✅ When to Use Greedy:
- Problem has optimal substructure
- Greedy choice property holds
- Can prove correctness (often by contradiction)
- Examples: MST, shortest path, activity selection