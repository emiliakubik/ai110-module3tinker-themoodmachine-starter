import string
import re

# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        TODO: Improve this method.

        Right now, it does the minimum:
          - Strips leading and trailing whitespace
          - Converts everything to lowercase
          - Splits on spaces

        Ideas to improve:
          - Remove punctuation
          - Handle simple emojis separately (":)", ":-(", "🥲", "😂")
          - Normalize repeated characters ("soooo" -> "soo")
        """
        cleaned = text.strip().lower()

        # Text emojis
        cleaned = cleaned.replace(':)', ' happy_emoji ')
        cleaned = cleaned.replace(':(', ' sad_emoji ')
        cleaned = cleaned.replace(':-(', ' sad_emoji ')
        
        # Unicode emojis (add spaces so they become separate tokens)
        cleaned = cleaned.replace('😂', ' laughing_emoji ')
        cleaned = cleaned.replace('🥲', ' crying_emoji ')
        cleaned = cleaned.replace('💀', ' skull_emoji ')

        # Normalize repeated characters (3+ -> 2)
        # Pattern: matches any character repeated 3 or more times
        # Replacement: replaces with the character repeated twice
        cleaned = re.sub(r'(.)\1{2,}', r'\1\1', cleaned)

        #removing punctuation
        cleaned = ''.join(char for char in cleaned if char not in string.punctuation) # removing punctuation
        tokens = cleaned.split()

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
      tokens = self.preprocess(text)
      score = 0

      # Strong words and emojis get 2 point
      strong_positive = {'love', 'amazing', 'awesome', 'happy_emoji', 'laughing_emoji'}
      strong_negative = {'hate', 'terrible', 'awful', 'sad_emoji'}

      for token in tokens:
        if token in strong_positive:
          score += 2
        elif token in self.positive_words:
           score += 1

        if token in strong_negative:
           score -= 2
        elif token in self.negative_words:
           score -= 1

      return score
                
        # TODO: Implement this method.
        #   1. Call self.preprocess(text) to get tokens.
        #   2. Loop over the tokens.
        #   3. Increase the score for positive words, decrease for negative words.
        #   4. Return the total score.
        #
        # Hint: if you implement negation, you may want to look at pairs of tokens,
        # like ("not", "happy") or ("never", "fun").

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        score = self.score_text(text) 
        tokens = self.preprocess(text)

        # check for both positive and negative words in sentence
        has_positive = any(t in self.positive_words for t in tokens)
        has_negative = any(t in self.negative_words for t in tokens)

        if has_positive and has_negative:
           return "mixed"
        elif score > 0:
           return "positive"
        elif score < 0:
           return "negative"
        else:
           return "neutral"

        # TODO: Implement this method.
        #   1. Call self.score_text(text) to get the numeric score.
        #   2. Return "positive" if the score is above 0.
        #   3. Return "negative" if the score is below 0.
        #   4. Return "neutral" otherwise.

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
