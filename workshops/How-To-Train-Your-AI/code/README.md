# Guess, Check, Adjust: Training AI One Step at a Time

This workshop demonstrates how AI learns through three progressive steps:

## Files & Purpose

1. **01_basic_predictor.py**: Shows pure randomness
   * No parameters to adjust
   * Demonstrates why we need smarter approaches
   * Run multiple times to see complete randomness

2. **02_markov_improved.py**: Introduces smart prediction
   * Set `window_size` (3-6 recommended)
   * Adjust `temperature` (0.7-0.8 optimal)
   * Watch debug output to see AI thinking

3. **03_interactive.py**: Full AI training experience
   * Control multiple parameters
   * See training progress
   * Get real-time feedback
   * Experiment with different settings

## Recommended Settings

For best results:

* **First Try**: Use defaults to see why parameters matter
* **Better Results**: 
  - window_size=5-6
  - temperature=0.7-0.8
* **Experimental**:
  - Higher temperature (>1.2) for creative text
  - Larger window_size (>6) for more context

## Tips for Success

* Start with suggested settings
* Watch debug output to understand choices
* Try multiple combinations
* Compare outputs to understand impact
* Remember: Real AI uses same concepts at massive scale!
