# State Tracking Problems

## 📈 Concept
Problems that require maintaining and updating state as you process a sequence of events or inputs.

## 🎯 Key Patterns
- **State machines**: Track discrete states (above/below, inside/outside)
- **Transition detection**: Recognize when state changes
- **Accumulated metrics**: Count transitions or time in states
- **Event-driven**: Process sequence of events/actions

## 📚 Problems

### `counting_valleys.ipynb`
**Pattern**: State machine with transition counting
- Track elevation (above/below sea level)
- Detect state transitions
- Count valleys (transitions from below to sea level)
**Key insight**: 
  - Valley ends when elevation returns to 0 from negative
  - Track current elevation and previous state

## 💡 Common Approach
```python
def track_state(sequence):
    state = initial_state
    count = 0
    
    for event in sequence:
        previous_state = state
        state = update_state(state, event)
        
        # Detect specific transition
        if is_target_transition(previous_state, state):
            count += 1
    
    return count
```

### Example: Counting Valleys
```python
def countingValleys(steps, path):
    level = 0
    valleys = 0
    
    for step in path:
        prev_level = level
        level += 1 if step == 'U' else -1
        
        # Valley ends when returning to sea level from below
        if prev_level < 0 and level == 0:
            valleys += 1
    
    return valleys
```

## 🔗 Related Patterns
- Finite state machines
- Event processing
- Stream processing
- Threshold detection
