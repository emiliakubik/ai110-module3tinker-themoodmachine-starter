# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
Describe whether you used the rule based model, the ML model, or both.  
Example: “I used the rule based model only” or “I compared both models.”

I compared both models but only made changes to the rule based model

**Intended purpose:**  
What is this model trying to do?  
Example: classify short text messages as moods like positive, negative, neutral, or mixed.

Decide the mood of a user given a short message that they send

**How it works (brief):**  
For the rule based version, describe the scoring rules you created.  
For the ML version, describe how training works at a high level (no math needed).

4 possible moods: positive, negative, mixed, and neutral
Given key words that are either classified as positive or negative, those words and their given weights are added up to create a score for the message. If the score is positive, the mood is positive. If the score is negative, the mood is negative. If the score is 0, the mood is neutral. And lastly, if the message contains both positive and negative words, it is considered to have a mood of mixed. Another addition that was made to this model was taking into account negating words which can flip the sentiment of the keywords.



## 2. Data

**Dataset description:**  
Summarize how many posts are in `SAMPLE_POSTS` and how you added new ones.

There were 5 posts orginally, and I added 5 more, to make a total of 10 sample posts.
I went down the list of the 4 moods and tried to think of one for each. Neutral was the hardest because I wasn't necessarily sure how to make sure it was truly neutral so I used copilot for help on brainstorming that one.

**Labeling process:**  
Explain how you chose labels for your new examples.  
Mention any posts that were hard to label or could have multiple valid labels.

I wrote my posts with their intended moods in mind. To me, "Feeling tired but kind of hopeful" could be mixed or neutral depending on how you look at it. 

**Important characteristics of your dataset:**  
Examples you might include:  

- Contains slang or emojis  
- Includes sarcasm  
- Some posts express mixed feelings  
- Contains short or ambiguous messages

Messages with words that negate other words.

**Possible issues with the dataset:**  
Think about imbalance, ambiguity, or missing kinds of language.

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
Describe the modeling choices you made.  
Examples:  

- How positive and negative words affect score  
- Negation rules you added  
- Weighted words  
- Emoji handling  
- Threshold decisions for labels

There are strong positive and negative words that would impact the score by 2, whereas the rest of the positive and negative only affected the score by 1. Handled emojis by turning them into words (ex: 'laughing_emoji'). 

**Strengths of this approach:**  
Where does it behave predictably or reasonably well?

It behaves well on the simple "as-expected" examples and the ones with negation

**Weaknesses of this approach:**  
Where does it fail?  
Examples: sarcasm, subtlety, mixed moods, unfamiliar slang.

sarcasm and unfamiliar slang

## 4. How the ML Model Works (if used)

**Features used:**  
Describe the representation.  
Example: “Bag of words using CountVectorizer.”

**Training data:**  
State that the model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
Did you observe changes in accuracy when you added more examples or changed labels?

**Strengths and weaknesses:**  
Strengths might include learning patterns automatically.  
Weaknesses might include overfitting to the training data or picking up spurious cues.

## 5. Evaluation

**How you evaluated the model:**  
Both versions can be evaluated on the labeled posts in `dataset.py`.  
Describe what accuracy you observed.

the rule based model was given a 0.83 accuracy

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.

"I am not happy about this" -> negative
"Feeling tired but kind of hopeful" -> negative

**Examples of incorrect predictions:**  
Provide 2 or 3 examples and explain why the model made a mistake.  
If you used both models, show how their failures differed.

"Feeling tired but kind of hopeful" -> predicted=negative, true=mixed
"I'm dead 💀" -> neutral

## 6. Limitations

Describe the most important limitations.  
Examples:  

- The dataset is small  
- The model does not generalize to longer posts  
- It cannot detect sarcasm reliably  
- It depends heavily on the words you chose or labeled

From what I understand, there is not possible way to handle sarcasm with the rule base model

## 7. Ethical Considerations

Discuss any potential impacts of using mood detection in real applications.  
Examples: 

- Misclassifying a message expressing distress  
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages

Responding with the wrong sentiment in a dire situation 

## 8. Ideas for Improvement

List ways to improve either model.  
Possible directions:  

- Add more labeled data  
- Use TF IDF instead of CountVectorizer  
- Add better preprocessing for emojis or slang  
- Use a small neural network or transformer model  
- Improve the rule based scoring method  
- Add a real test set instead of training accuracy only

Add more keywords to both positive and negative lists.