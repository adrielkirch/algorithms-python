# Game Logic Problems

## 🎮 Concept
Problems that simulate game scenarios with specific rules, constraints, and winning conditions.

## 🎯 Key Patterns
- **Rule enforcement**: Follow game rules precisely
- **Optimal strategy**: Find best moves/decisions
- **Constraint satisfaction**: Respect game constraints
- **Win condition checking**: Determine if goal is achieved

## 📚 Problems

### `angry_professor.ipynb`
**Pattern**: Threshold-based decision
- Check if enough students arrive on time
- Binary outcome based on threshold
**Key insight**: Simple counting + comparison

### `jump_on_the_clouds.ipynb`
**Pattern**: Greedy pathfinding
- Always prefer longer jumps when safe
- Minimize number of moves
- Avoid dangerous positions
**Key insight**: Greedy choice (jump 2 if possible, else 1)

### `jumping_on_clouds_revisited.ipynb`
**Pattern**: Circular traversal with energy
- Fixed jump distance in circular array
- Energy decreases based on cloud type
- Complete full circle
**Key insight**: Modulo arithmetic for circular movement

## 💡 Common Approach
```python
def solve_game(state, rules):
    position = start
    moves = 0
    
    while not reached_goal(position):
        # Find best valid move
        move = choose_move(position, rules)
        position = apply_move(position, move)
        moves += 1
    
    return moves
```

## 🔗 Related Patterns
- Greedy algorithms
- Dynamic programming
- Path optimization
