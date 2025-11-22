import random
import re
from collections import defaultdict, Counter

class TrigramModel:
    def __init__(self):
        """
        Initializes the TrigramModel.
        """
        #TODO: Initialize any data structures you need to store the n-gram counts.
        self.counts = defaultdict(lambda: defaultdict(Counter))
        self.probs = defaultdict(lambda: defaultdict(dict))                 

    def fit(self, text):
        """
        Trains the trigram model on the given text.

        Args:
            text (str): The text to train the model on.
        """
        #TODO: Implement the training logic.
        if not text.strip():
            return
        
        # 1. Cleaning the text (e.g., converting to lowercase, removing punctuation).
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text)

        # 2. Tokenizing the text into words.
        tokens = text.split()

        # 3. Padding the text with start and end tokens.
        tokens = ['<s>', '<s>'] + tokens + ['</s>']

        # 4. Counting the trigrams.
        for i in range(len(tokens) - 2):
            w1, w2, w3 = tokens[i], tokens[i+1], tokens[i+2]
            self.counts[w1][w2][w3] += 1

        # 5. Covert counts to probabilites
        for w1 in self.counts:
            for w2 in self.counts[w1]:
                total = sum(self.counts[w1][w2].values())
                self.probs[w1][w2] = {
                    w3: count / total for w3, count in self.counts[w1][w2].items()
                }


    def generate(self, max_length=50):
        """
        Generates new text using the trained trigram model.

        Args:
            max_length (int): The maximum length of the generated text.

        Returns:
            str: The generated text.
        """
        #TODO: Implement the generation logic.
        if not self.probs:
            return ""

        # 1. Starting with the start tokens.
        w1, w2 = "<s>", "<s>"
        output = []

        # 2. Repeating until the end token is generated or the maximum length is reached.
        for _ in range(max_length):
            # If no continuation exists for this context, stop
            if w2 not in self.probs[w1]:
                break

            # Probabilistically choose the next word
            choices, weights = zip(*self.probs[w1][w2].items())
            w3 = random.choices(choices, weights=weights)[0]

            # Stop if end token is reached
            if w3 == "</s>":
                break

            output.append(w3)
            w1, w2 = w2, w3

        return " ".join(output)
        