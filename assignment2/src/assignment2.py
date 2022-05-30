### Assignment 2 - Sentiment and NER
## 2.2 - Real vs Fake news
# By Line Stampe-Degn Møller
# Language Analytics, Cultural Data Science

## TASKS:
# Using the corpus of Fake vs Real news, write some code which does the following:
# - Split the data into two datasets - one of Fake news and one of Real news
# - For every headline
#    - Get the sentiment scores
#    - Find all mentions of geopolitical entites
#    - Save a CSV which shows the text ID, the sentiment scores, and column showing all GPEs in that text
# - Find the 20 most common geopolitical entities mentioned across each dataset - plot the results as a bar charts

## USAGE:
# In terminal, add:
# pip install vaderSentiment
# pip install spacytextblob
# python -m spacy download en_core_web_sm

# To run this script:
# python3 src/assignment2.py

# IMPORTS:
# Data analysis
import os
import pandas as pd
from collections import Counter
from tqdm import tqdm
# NLP
import spacy
nlp = spacy.load("en_core_web_sm")
# Sentiment analysis VADER
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
# Sentiment with spacyTextBlob
from spacytextblob.spacytextblob import SpacyTextBlob
nlp.add_pipe('spacytextblob')
# Visualisations
import matplotlib.pyplot as plt

# Filepath
filename = os.path.join("in", "tabular_examples", "fake_or_real_news.csv")

# load data
data = pd.read_csv(filename)

# SPLIT THE DATA INTO TWO DATASETS - ONE FOR FAKE NEWS AND ONE FOR REAL NEWS:
real_news = data[data["label"]=="REAL"]
fake_news = data[data["label"]=="FAKE"]

# Filename variables:
real = "real_news"
fake = "fake_news"

# Dataframe funtion:
def create_df(news, filename):
    # FILL IN DATAFRAME - FAKE NEWS:
    # - Sentiment assessment and mentions of geopolitical entities:
    
    # Create data frame with text ID
    news_df = news["Unnamed: 0"]
    
    # Convert into data frame
    news_df = pd.DataFrame(news_df)
    
    # Rename column with text ID
    news_df.rename(columns = {"Unnamed: 0":"text ID"}, inplace = True)
    
    # Get polarity and subjectivity scores
    sentiment_ass = []
    for headline in news["title"]:
        doc = nlp(headline)
        score = doc._.blob.sentiment_assessments.assessments
        sentiment_ass.append(score)
        
    # Add sent_ass to df
    news_df["Sentiment assessment"] = sentiment_ass

    # Find all mentions of geopolitical entites
    ents = []

    for posts in tqdm(nlp.pipe(news["title"], batch_size=500)):
        this_list = []
        # Get GPE for each headline
        for entity in posts.ents:
            # If entity is a GPE
            if entity.label_ == "GPE":
                # Append to this_list
                this_list.append(entity.text)
        ents.append(this_list)

    # Add GPE to dataframe
    news_df["GPEs"] = ents

    # Save dataframe to csv
    news_df.to_csv(f"out/{filename}_dataframe.csv", index = False)
    
# BUILD AND SAVE DATAFRAMES FOR REAL AND FAKE NEWS (using the create_df function from above):
create_df(real_news, fake)
create_df(fake_news, real)

# FIND 20 MOST COMMON GPES FOR THE REAL AND THE FAKE NEWS
def gpe_plot(news, filename):
    gpe = [] 
    for posts in tqdm(nlp.pipe(news["title"], batch_size=500)):
        # Get GPE for each headline
        for entity in posts.ents:
            # If entity is a GPE
            if entity.label_ == "GPE":
                gpe.append(entity.text)

    # Get the top 20 most common GPEs
    gpe_count = Counter(gpe).most_common(20)
    # Make into dataframe
    gpe_count = pd.DataFrame(gpe_count)
    # Rename the columns to GPE and Count
    gpe_count.rename(columns={0: "GPE", 1: "Count"}, inplace=True)

    # Create bar plot over 20 most common GPEs
    gpe_count.plot.bar(x="GPE", y="Count")
    # Save plot:
    plt.savefig(f"out/{filename}_gpe_plot.png")

# CREATE AND SAVE GPE PLOTS (using the gpe_plot function from above):
gpe_plot(real_news, real)
gpe_plot(fake_news, fake)
