# Evaluation

Please provide a 1-page summary of your design choices for the Trigram Language Model.

This should include:

* How you chose to store the n-gram counts.
* How you handled text cleaning, padding, and unknown words.
* How you implemented the `generate` function and the probabilistic sampling.
* Any other design decisions you made and why you made them.

---

# Evaluation Summary

## Design Choices

* **Text Cleaning**: Converted to lowercase and removed punctuation using regex to ensure consistent tokens.
* **Padding**: Added `<s>, <s>` at the start and `</s>` at the end to capture sentence boundaries.
* **Data Structures**: Used nested `defaultdict` and `Counter` for efficient trigram counting and probability normalization.
* **Generation Strategy**: Started from `<s>, <s>` and sampled next words using `random.choices` weighted by trigram probabilities. Stopped at `</s>` or `max\_length`.
* **Edge Cases**: Handled empty input and short text gracefully, always returning a string.

## Testing

* **Unit Tests**: Verified three scenarios:

  1. Normal sentence → generates valid text.
  2. Empty input → returns empty string.
  3. Short input → still generates valid string.

* All tests passed (`python -m pytest tests/test_ngram.py`).

<img width="1472" height="302" alt="Screenshot 2025-11-22 142456" src="https://github.com/user-attachments/assets/a20ba552-a340-4457-96eb-45df960e0d98" />

