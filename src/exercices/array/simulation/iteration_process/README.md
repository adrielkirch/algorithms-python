# Iteration Process Problems

## 🔄 Concept
Problems that involve simulating a process through repeated iterations until a termination condition is met.

## 🎯 Key Patterns
- **Loop until exhaustion**: Continue until no more elements can be processed
- **State modification**: Each iteration modifies the problem state
- **Result accumulation**: Collect results from each iteration step
- **Termination conditions**: Know when to stop iterating

## 📚 Problems

### `cut_the_sticks.ipynb`
**Pattern**: Iterative reduction
- Remove minimum length from all sticks each iteration
- Count remaining sticks after each cut
- Continue until no sticks remain
**Key insight**: Track count before removal, not after

### `viral_advertising.ipynb`
**Pattern**: Growth simulation
- Simulate day-by-day viral spread
- Each person shares with multiple people
- Track cumulative likes over time
**Key insight**: Only half of shared people like the ad

## 💡 Common Approach
```python
result = []
while not_finished(state):
    # Record current state
    result.append(measure(state))
    # Modify state
    state = transform(state)
return result
```

## 🔗 Related Patterns
- State machines
- Process simulation
- Temporal modeling
