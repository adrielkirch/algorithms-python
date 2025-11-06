# Simulation Problems

## 🎯 Concept
Simulation problems require step-by-step modeling of real-world processes:
- **Process modeling**: Follow rules/constraints exactly as described
- **State tracking**: Maintain current state through iterations
- **Rule-based**: Apply given rules systematically
- **Implementation-heavy**: Focus on correct implementation rather than algorithms

## 📚 Problems in this folder:

### `apple_orange_thrown_distance.ipynb`
- **Technique**: Simulate fruit throws and count hits
- **Pattern**: Range checking simulation
- **Key insight**: Check if landing position falls within target range

### `counting_valleys.ipynb`
- **Technique**: Simulate hiking path, track elevation changes
- **Pattern**: State machine (above/below sea level)
- **Key insight**: Count valleys when returning to sea level from below

### `day_of_programmer.ipynb`
- **Technique**: Simulate calendar calculation
- **Pattern**: Date/time calculation with special rules
- **Key insight**: Handle leap years and calendar transitions

### `grading_round_up.ipynb`
- **Technique**: Simulate grading rules
- **Pattern**: Conditional rounding based on rules
- **Key insight**: Round up only if within 3 points of next multiple of 5

### `mini_max_sum.ipynb`
- **Technique**: Calculate all possible 4-element sums
- **Pattern**: Array sum variations
- **Key insight**: Min sum = total - max element, Max sum = total - min element

### `positive_negative_zero_ratios_calculation.ipynb`
- **Technique**: Count and calculate ratios
- **Pattern**: Classification and ratio calculation
- **Key insight**: Classify elements and compute proportions

### `share_bill_bon_appetit.ipynb`
- **Technique**: Simulate bill sharing calculation
- **Pattern**: Financial calculation with exceptions
- **Key insight**: Calculate fair share excluding items not consumed

## 💡 Common Patterns:
1. **State Machine**:
   ```python
   state = initial_state
   for event in events:
       if state == STATE_A and condition:
           state = STATE_B
           # handle state transition
   ```

2. **Rule Application**:
   ```python
   def apply_rules(input_data):
       result = []
       for item in input_data:
           if rule1(item):
               result.append(transform1(item))
           elif rule2(item):
               result.append(transform2(item))
   ```

3. **Process Simulation**:
   ```python
   def simulate_process(steps):
       current_state = initial_state
       for step in steps:
           current_state = update_state(current_state, step)
       return current_state
   ```

## ✅ When to Use:
- Problem describes a real-world process
- Rules are clearly defined and must be followed exactly
- Focus is on correct implementation rather than optimization
- Often found in competitive programming as "easy" problems