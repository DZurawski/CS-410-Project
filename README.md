# E-mail Importance Ranker and Retrospective Summarizer
This is the course project and the technology review for CS 410 - Text Information Systems at the University of Illinois.
The function of this tool is to classify an email as important or not important using spaCy and summarize the important topics from the corpus.
**Video Presentation:** <Link to be added>

### Project team
- Daniel Zurawski - dzuraws2@illinois.edu (Coordinator) 
- Gassan Soukaev - soukaev2@illinois.edu
- Vedprakash Mishra - vrm2@illinois.edu 

## Background/Problem Statement:
- “Too many emails” is a common problem in today’s work environment. Although collaboration tools like Slack and MS Team attempts to reduce email clutter, Emails remain the primary mode of communication with most big project groups.
- With hundreds of emails per day, it is easy to drown ourselves in the chaotic interactions and losing the big picture of the job responsibilities.
- It would be a boon to have a text analysis module that can analyze all the incoming and outgoing emails for past X days (usually weekly or monthly) and provide a summary of all the interactions along with value-added features such as
>- Frequently used key words backed by a few top examples => this will provide common themes for weeks and months (Weekly/Monthly summary)
>- Email statistics with basic graph analysis of well-connected group of people with an importance score, which subsequently can be used to identify and bring important emails on the top of the stack

# System requirements and Usage
## Pre-requisites
- Python/NLP Packages: [spaCy](https://spacy.io), [NumPy](http://www.numpy.org), [Pandas](https://pandas.pydata.org), [pickle](https://docs.python.org/3/library/pickle.html)
- spaCy language model: [en_core_web_lg](https://spacy.io/models/en#section-en_core_web_lg) (Installation command: python -m spacy download en_core_web_md)

## Delivery Package 
- The main deliverable of this project is **etools** package that provide functionality to score any input email document based on the similarity with the trained dataset that is manually evaluated by the project team members. We have also provided example usage in the provided python notebooks.
- All the project files are contained in the **Course Project** folder of this project
>- etools package (main tool)
>>- environment.py
>>- ranker.py
>>- summarizer.py
>>- tfidf.pkl
>>- emails_*.xslx
>- introduction.ipynb (testing & evaluation notebook)

## Code Walk through
introduction.ipynb
- This is the file that the user would need to run
- It imports ranker and summarizer
- Finally it loads the test file and prints the scores for sample emails as well as the most significant words and sentences

environment.py
- This file loads spacy language model which is a CNN trained on English blogs, comments, and news stories
- It also opens "pickled" pre-trained model that we trained on emails that were manually classified as important or not important by the team

ranker.py
- This file loads the training file, trains a spacy model and provides email scoring capability
It contains the following functions:
- clean function: it cleans input strings (removes white space, changes to lowercase, etc.)
- score function: it provides a similarity score for input email
- is_important function: it provides a similarity score for input email but as a boolean value (true or false)

summarizer.py
- clean function: it cleans input strings (removes white space, changes to lowercase, etc.)
- significant_words function: returns a list of the top *words*: most significant words to *document*.
- significant_sentences function: returns a list of the top *sentences*: most significant sentences to *document*.
- summarizing_sentences function: return a list of the top *sentences*: best summarizing sentences to *document*.

## Team contributions
### Requirement analysis and evaluation of toolkits for this project
- Team conducted brainstorming sessions to evolve the idea through requirement analysis and a high-level project plan
- Dan proposed & took spaCy toolkit through evaluation for thie project implementation
- Gassan proposed & took NLTK toolkit through evaluation for thie project implementation
- Ved performed evaluation of MetaPy to complete perspective and ensure the right selection of tool based on text mining capability for implementation.  
- Based on the output of evaluation & individual POC implementations, spaCy won hands-down due to powerfull, scalable features complemented with machine-learning capability for potential enhancements 

### Dataset seletion and preparation
- We selected 25,000 uniform randomly selected e-mails from entire bank of Enron corpus
- After data wrangling and clean, each of us picked 300 distint emails for manual categorization into important and unimportant categories for training and evalution of classifier
- We chose to utilized whole set of 25,000 emails for summarization module

### Implementation 
- We collectively chose spaCy implementation of classifier by Dan to collaboratively develop upon given the simplicity and yet powerful features it offered
- Ved manually tested the package of classifier and summarizer through introduction.ipynb as a wrapper and one set of manually categorized 300 emails.  
- Gassan wrote evaluation module to evaluate the result of classifier
- Testing & evaluation feedback provided inputs for finetuning of classifier and summarizer which Dan incorporated in the code.

## Potential Enhancements
- Integrate with the Mailbox and show summary of top important emails in specific time period: week/month
- List of important/top contacts based on frequent senders/recievers that has important email content 
- Suggestions on de-registering from distribution lists
- Suggestions on email templates based on common phrases/formats used frequently



## FAQs
### What is the function of the tool?

We plan to create a suite of utilities that will help users handle many e-mails. The utilities will be able to rank the importance of e-mails with respect to the content and sender. The utilities will also be able to summarize a corpus of e-mails received during a specified time period using a set of keywords.

### Who will benefit from such a tool?

A working professional often receive too many e-mails to reasonably address within a day. Our tool will help these users by identifying the most urgent e-mails. People also occasionally forget the specific discussion areas of e-mails received during special periods of time. Our tool provides keywords to help users recall what was being accomplished during a time period. This summary can be an effective retrospective tool for better planning in the weeks to come.

### Does this kind of tools already exist? If similar tools exist, how is your tool different from them? Would people care about the difference?

There exist machine learning programs that can detect if e-mails are spam. Our tool is different in that it ranks the e-mails based on importance, so it remains up to the user whether or not an e-mail is important. Also, our tool takes into account the sender of the e-mail, whereas similar existing tools only account for the content of the e-mail. This factor may indicate that our methods will yield greater accuracy in ranking e-mail importance and, thus, users will be more satisfied with our tool.

### What existing resources can you use?

Currently, there are many available modules for text mining e-mails, including MeTapy, Sklearn, SpaCy and NLTK. These modules will be useful for identifying and ranking the e-mails. Also, the Enron Corpus of e-mails will be a useful resource for testing and training our utilities.

### What techniques/algorithms will you use to develop the tool? 

We plan to use variants of the BM25 for ranking the importance of e-mails. Our tool will infer query terms by using e-mails that the user has reported as an example of an important e-mail. We also plan to use graph theory algorithms to identify the importance of an e-mail based on frequent sender/receiver relationships.






