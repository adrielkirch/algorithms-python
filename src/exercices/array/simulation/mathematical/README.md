# Mathematical Calculation Problems

## 🔢 Concept
Problems that involve mathematical formulas, calculations, and numerical transformations based on specific rules.

## 🎯 Key Patterns
- **Formula application**: Apply mathematical formulas correctly
- **Special cases**: Handle edge cases and exceptions
- **Precision**: Maintain correct rounding/formatting
- **Rule-based calculation**: Follow specific mathematical rules

## 📚 Problems

### `beautiful_days.ipynb`
**Pattern**: Conditional counting with number reversal
- Calculate absolute difference with reversed number
- Check divisibility
**Key insight**: Number reversal + modulo check

### `day_of_programmer.ipynb`
**Pattern**: Date calculation with historical rules
- Handle Julian/Gregorian calendar transition
- Leap year rules vary by era
**Key insight**: Different rules for different year ranges

### `grading_round_up.ipynb`
**Pattern**: Conditional rounding
- Round up only if within threshold
- Only applies above minimum value
**Key insight**: Multiple conditions before rounding

### `mini_max_sum.ipynb`
**Pattern**: Array sum variations
- Find minimum and maximum possible sums
- Exclude one element at a time
**Key insight**: Total - max element = min sum

### `positive_negative_zero_ratios_calculation.ipynb`
**Pattern**: Classification and ratio
- Categorize elements
- Calculate proportions
**Key insight**: Count categories, divide by total

### `share_bill_bon_appetit.ipynb`
**Pattern**: Financial calculation with exclusions
- Calculate fair share excluding items
- Refund calculation
**Key insight**: Total - excluded item, then divide

## 💡 Common Approach
```python
def calculate(inputs, rules):
    # Apply formula or rules
    result = apply_formula(inputs)
    
    # Handle special cases
    if special_condition(inputs):
        result = adjust(result)
    
    # Format output
    return format_result(result)
```

## 🔗 Related Patterns
- Number theory
- Arithmetic operations
- Conditional logic
