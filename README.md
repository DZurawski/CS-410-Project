# E-mail Importance Ranker and Retrospective Summarizer
*This is the final course project for **CS 410 - Text Retrieval & Mining** course at the University of Illinois at Urbana-Champaign.*

The function of this tool is to classify email(s) as important or not important using the spaCy toolkit and provide the user with a summary of the important topics from the corpus.
A working professional often receive too many e-mails to reasonably address within a day. Our tool will help these users by identifying the most urgent e-mails. People also occasionally forget the specific discussion areas of e-mails received during special periods of time. Our tool provides important summaries to help users recall what was being accomplished during a time period. This summary can be an effective retrospective tool for better planning in the weeks to come.

**Video Presentation:** https://youtu.be/qMoXzIW6nfk

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

## System requirements and Usage
### Pre-requisites
- Python/NLP Packages: [spaCy](https://spacy.io), [NumPy](http://www.numpy.org), [Pandas](https://pandas.pydata.org), [pickle](https://docs.python.org/3/library/pickle.html)
- spaCy language model: [en_core_web_lg](https://spacy.io/models/en#section-en_core_web_lg) (Installation command: python -m spacy download en_core_web_lg)

### Delivery Package 
- The main deliverable of this project is **etools** package that provide functionality to score any input email document based on the similarity with the trained dataset that is manually evaluated by the project team members. We have also provided example usage in the provided python notebooks.
- All the project files are contained in the **Course Project** folder of this project
>- etools package (main tool)
>>- environment.py
>>- ranker.py
>>- summarizer.py
>>- tfidf.pkl
>>- emails_*.xslx
>- introduction.ipynb (testing & evaluation notebook)

### How to use
- Consider an example usage in the provided **introduction.ipynb**
>- import ranker and summarizer from the provided etool package
>- Load the input email document(s) for scoring and categorization. The provided example is loading one of the 3 datasets that we manually created. The only 2 columns(fields) of the input file we would be using are Content (email text) and Important (manually categorized value) 
>- Pass the input email(s) text to summarizer and print significant words/sentences
>- Pass the input email(s) text to ranker and print score (range:0(unimportant) to 1(important)) and resulting category: important or unimportant

- We have also provided a cranfield evaluation in **cranfield-evaluation-module.ipynb**
>- Import the ranker and summarizer functions
>- Perform the spot check and scoring
>- Since we have utilized the first 2 sets of manual classified data for training, we utilize the third set for evaluation
>- For every email in the test document we utilize the classifier to categorize into important or important & compare the result with manual results
>- Calculate the values in Human-Machine metrics and subsequently calculate Accuracy, Precision and Recall.  

### Code Walk through

**environment.py**
- Loads spaCy language model (en_core_web_lg) which is a CNN trained on English blogs, comments, and news stories
- Opens "pickled" pre-trained model that we trained on emails that were manually classified as important or unimportant

**ranker.py**
- Loads the training file, trains a spacy model and provides email scoring capability
It contains the following functions:
- clean function: cleans the input document and prepares it for text mining (removes stop word & white space, changes to lowercase, etc.)
- score function: provides a similarity score (float: 0 (imp) - 1 (un-imp)) for input email based on cosine similarity with the trained data set
- is_important function: provides a Boolean value of classification on whether the input email is important or not based on the similarity score (true means important)

**summarizer.py**
- clean function: cleans the input document and prepares it for text mining (removes stop word & white space, changes to lowercase, etc.)
- significant_words function: returns a list of the most significant words in the input document(s)
- significant_sentences function: returns a list of the most significant sentences in the input document(s)
- summarizing_sentences function: returns a list of the best summarizing sentences in the input document(s)

**introduction.ipynb**
- example usage of the etools classification and summarization of the input email document(s)

**cranfield-evaluation-module.ipynb**
- compares the implemented etools classifier output with the human classified output and provides accuracy, precision and recall to judge the effectiveness of etools. 

## Team contributions
### Requirement analysis and evaluation of toolkits for this project
- Team conducted multiple brainstorming sessions to evolve the idea through requirement analysis and a high-level project plan
- *Dan* proposed & took spaCy toolkit through evaluation for this project implementation and tech review
- *Gassan* proposed & took NLTK toolkit through evaluation for this project implementation and tech review
- *Ved* performed evaluation of MetaPy to complete perspective and ensure the right selection of tool happens based on text mining capabilities suited for the implementation.  
- Based on the output of evaluation & individual POC implementations, spaCy won hands-down due to powerful, scalable features complemented with the machine-learning capabilities for the potential enhancements 

### Dataset selection and preparation
- We selected 25,000 uniform randomly selected e-mails from the entire bank of Enron email corpus
- After data wrangling and cleaning efforts, each of us picked 300 distinct emails for the manual classification of emails into important and unimportant categories for training and evaluation of the classifier
- We chose to utilize the whole set of 25,000 emails for summarization module

### Implementation 
- We collectively selected spaCy implementation of classifier by *Dan* to collaboratively develop upon, mainly due to the simplicity and yet powerful features spaCy offered
- *Ved* manually tested the package of classifier and summarizer through introduction.ipynb as a wrapper and one set of manually categorized 300 emails. Noted and shared the observations with the team.  
- *Gassan* wrote an evaluation module to evaluate the result of classifier to quantitatively measure the accuracy and precision of the classifier
- Testing & evaluation feedback provided inputs for finetuning of classifier and summarizer which *Dan* incorporated into the code

## Potential Enhancements
- Integrate with the Mailbox and show summary of top important emails in specific time period: week/month
- List of important/top contacts based on frequent senders/receivers that has important email content 
- Suggestions on de-registering from distribution lists
- Suggestions on email templates based on common phrases/formats used frequently


