import spacy
import pickle

# Spacy Language object. Used to create Document pipelines from strings.
# The "en_core_web_md" model is a convolutional neural network trained on
# English web blogs, comments and news stories.
NLP = spacy.load("en_core_web_lg")

# Trained TF-IDF vectorizer from scikit-learn. Trained on Enron corpus e-mails.
# 25,000 uniform randomly selected e-mails from entire bank of Enron corpus.
with open("etools/tfidf.pkl", "rb") as file:
    TFIDF = pickle.load(file)