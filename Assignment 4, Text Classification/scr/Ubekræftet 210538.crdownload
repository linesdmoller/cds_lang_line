# Assignment 4: Text Classification, pt 1; classification with machine learning
## By Line Stampe-Degn Møller

## Assignment description and data:
### https://github.com/CDS-AU-DK
### https://github.com/CDS-AU-DK/cds-language/blob/main/assignments/assignment4.md

## Assignment tasks:

### The first script should perform benchmark classification using standard machine learning approaches
#### This means CountVectorizer() or TfidfVectorizer(), LogisticRegression classifier
#### Save the results from the classification report to a text file

###########################################################

## PACKAGES
# system tools
import os
import sys
sys.path.append(os.path.join("."))

# data munging tools
import pandas as pd
import utils.classifier_utils as clf

# Machine learning stuff
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# handle warnings
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
    os.environ["PYTHONWARNINGS"] = "ignore"

## DATA
filename = os.path.join("in", "VideoCommentsThreatCorpus.csv")
data = pd.read_csv(filename)

# Check shape of data
shape = data.shape
print("Shape:\n",shape)

# Check label count
label_count = data["label"].value_counts()
print("\nlabel_count:\n",label_count)

# Create a balanced dataset for training
data_balanced = clf.balance(data, 1000)

# Check new shape
new_shape = data_balanced.shape
print("\nnew_shape:\n",new_shape)

# Checking new label count - should be a 50/50 split
new_label_count = data_balanced["label"].value_counts()
print("\nnew_label_count:\n",new_label_count)

# Splitting dataset into x and y for training
X = data_balanced["text"]
y = data_balanced["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X,               # texts for the model
                                                    y,               # classification labels
                                                    test_size=0.2,   # create an 80/20 split
                                                    random_state=42) # random state for reproducibility

# VECTORIZING AND FEATURE EXTRACTION
# Create a vectorizer object
vectorizer = TfidfVectorizer(ngram_range = (1,2),     # unigrams and bigrams (1 word and 2 word units)
                             lowercase =  True,       # why use lowercase?
                             max_df = 0.95,           # remove very common words
                             min_df = 0.05,           # remove very rare words
                             max_features = 100)      # keep only top 500 features

# Turning the data into vectors
# first we fit to the training data...
X_train_feats = vectorizer.fit_transform(X_train)

#... then do it for our test data
X_test_feats = vectorizer.transform(X_test)

# get feature names
feature_names = vectorizer.get_feature_names()

# CLASSIFYING AND PREDICTING
classifier = LogisticRegression(random_state=42).fit(X_train_feats, y_train)

# Using the classifyer to make predictions
y_pred = classifier.predict(X_test_feats)

# Predictions for the first 20 data points
print("\nPredictions for the first 20 data points:\n",y_pred[:20])

# Inspecting the model in order to see which features are most informative when trying to predict a label
print("\n20 most informative features of each label:")
clf.show_features(vectorizer, y_train, classifier, n=20)

# EVALUATION - how well does the model perform when comparing the predictions to the actual.
clf.plot_cm(y_test, y_pred, normalized=True)

# Make a classification report
report = metrics.classification_report(y_test, y_pred)
print("\nClassification report:\n",report)

# SAVE CLASSIFICATION REPORT
with open('out/cl_report_pt1.txt', 'w', encoding='UTF8') as f:
    f.write(report)
