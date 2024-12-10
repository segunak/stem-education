# Guess, Check, Adjust: Training AI One Step at a Time

This project contains three Python files that gradually transform random text generation into a more context-aware and tunable model. By adjusting parameters and experimenting with different settings, you'll see how AI "learns" to produce more coherent text.

## Instructions

1. **Run `01_basic_predictor.py`:**  
   Start here to see the baseline—purely random words. This shows you what happens before adding any "intelligence."

2. **Move on to `02_markov_improved.py`:**  
   Here, you'll introduce **Markov chains** (`window_size`) and tweak **temperature** to see how considering previous words and controlling "creativity" improves coherence.  
   - Try the default settings first.  
   - Then experiment with `window_size=2` and `temperature=0.5` to produce more coherent text.

3. **Explore `03_interactive.py`:**  
   Now you have full control. Choose `output_length`, `window_size`, `temperature`, and a starting word.  
   - Use the suggested starting words (e.g., "Alice", "May", "On", "I", "The").  
   - Adjust parameters and observe how it affects the style, coherence, and creativity of the output.

## Data

`data.txt` contains a small dataset of sentences. The model learns from these sentences, predicting the next word based on patterns it finds.

**Tip:** Experiment with different settings. Compare results. Discuss patterns. This hands-on approach will give you a feel for how larger AI models work on a grand scale.
