### Final project - Game of Thrones sentiment on Reddit
# By Line Stampe-Degn Møller
# Language Analytics, Cultural Data Science

## USAGE:
# In terminal, add:
# pip install spacy
# python -m spacy download en_core_web_sm
# pip install spacytextblob

# Data source:
# https://www.kaggle.com/datasets/nikhilkhetan/game-of-thrones
# - Download and add the data to the 'in' folder.
#   - The correct data should be a csv file called "GameofThrones.csv".

# To run this script:
# python3 src/finalproject.py

# IMPORTS:
# Data analysis
import os
import pandas as pd
from collections import Counter
from tqdm import tqdm
import numpy as np

# NLP
import spacy
nlp = spacy.load("en_core_web_sm")

# sentiment with spacyTextBlob
from spacytextblob.spacytextblob import SpacyTextBlob
nlp.add_pipe('spacytextblob')

# visualisations
import matplotlib.pyplot as plt

#____________________________________________________

# Load data:
filepath = "in/GameofThrones.csv"
df = pd.read_csv(filepath,encoding="ISO-8859-1")

# Check sample of data:
print("Sample of data:")
print(df[:5])

# CALCULATE POLARITY AND SUBJECTIVITY SCORES:
# Divide scores of comments about each season into separate lists
# Empty lists:
season1 = []
season2 = []
season3 = []
season4 = []
season5 = []
season6 = []
season7 = []
season8 = []

print("INFO: Currently tokenizing and calculating polarity and subjectivity scores - this may take a while...")

comment_no = 0
for i in df["body"]:  # For every comment in the original dataframe
    doc = nlp(str(i).lower()) # Tokenization through Spacy (lowercase so fx "season 1" and "Season 1" match)
    
    for i in range(len(doc)-1): # for range(0, l-1)

        # Get current and next word for multi-word matching
        current_token = doc[i]
        next_token = doc[i+1]

        if (current_token.text == "season" and next_token.text == "1") or (current_token.text in ["1st", "first"] and next_token.text == "season"): # If "season 1" or "1st season"      
            # Calculate scores
            pol_score = doc._.blob.polarity
            subj_score = doc._.blob.subjectivity
            # Append to list
            season1.append((comment_no, doc, pol_score, subj_score))

        if (current_token.text == "season" and next_token.text == "2") or (current_token.text in ["2nd", "second"] and next_token.text == "season"): # If "season n" or "Nth season"      
            # Calculate scores
            pol_score = doc._.blob.polarity
            subj_score = doc._.blob.subjectivity
            # Append to list
            season2.append((comment_no, doc, pol_score, subj_score))

        if (current_token.text == "season" and next_token.text == "3") or (current_token.text in ["3rd", "third"] and next_token.text == "season"): # If "season n" or "Nth season"      
            # Calculate scores
            pol_score = doc._.blob.polarity
            subj_score = doc._.blob.subjectivity
            # Append to list
            season3.append((comment_no, doc, pol_score, subj_score))

        if (current_token.text == "season" and next_token.text == "4") or (current_token.text in ["4th", "fourth"] and next_token.text == "season"): # If "season n" or "Nth season"      
            # Calculate scores
            pol_score = doc._.blob.polarity
            subj_score = doc._.blob.subjectivity
            # Append to list
            season4.append((comment_no, doc, pol_score, subj_score))

        if (current_token.text == "season" and next_token.text == "5") or (current_token.text in ["5th", "fifth"] and next_token.text == "season"): # If "season n" or "Nth season"      
            # Calculate scores
            pol_score = doc._.blob.polarity
            subj_score = doc._.blob.subjectivity
            # Append to list
            season5.append((comment_no, doc, pol_score, subj_score))

        if (current_token.text == "season" and next_token.text == "6") or (current_token.text in ["6th", "sixth"] and next_token.text == "season"): # If "season n" or "Nth season"      
            # Calculate scores
            pol_score = doc._.blob.polarity
            subj_score = doc._.blob.subjectivity
            # Append to list
            season6.append((comment_no, doc, pol_score, subj_score))

        if (current_token.text == "season" and next_token.text == "7") or (current_token.text in ["7th", "seventh"] and next_token.text == "season"): # If "season n" or "Nth season"      
            # Calculate scores
            pol_score = doc._.blob.polarity
            subj_score = doc._.blob.subjectivity
            # Append to list
            season7.append((comment_no, doc, pol_score, subj_score))

        if (current_token.text == "season" and next_token.text == "8") or (current_token.text in ["8th", "eighth"] and next_token.text == "season"): # If "season n" or "Nth season"      
            # Calculate scores
            pol_score = doc._.blob.polarity
            subj_score = doc._.blob.subjectivity
            # Append to list
            season8.append((comment_no, doc, pol_score, subj_score))
            
        else:
            pass
            
    comment_no = comment_no + 1

# Amount of comments about each season:
print("Amount of comments about each season:")
print(f"S1: {len(season1)}")
print(f"S2: {len(season2)}")
print(f"S3: {len(season3)}")
print(f"S4: {len(season4)}")
print(f"S5: {len(season5)}")
print(f"S6: {len(season6)}")
print(f"S7: {len(season7)}")
print(f"S8: {len(season8)}")

      
# CREATE AND SAVE INDIVIDUAL DATAFRAMES OF SCORES FOR EACH SEASON
# Column names:
column_names = ["comment_no", "comment", "pol_score", "subj_score"]

# Dataframes for each season:
season1_df = pd.DataFrame(season1, columns = column_names)
season2_df = pd.DataFrame(season2, columns = column_names)
season3_df = pd.DataFrame(season3, columns = column_names)
season4_df = pd.DataFrame(season4, columns = column_names)
season5_df = pd.DataFrame(season5, columns = column_names)
season6_df = pd.DataFrame(season6, columns = column_names)
season7_df = pd.DataFrame(season7, columns = column_names)
season8_df = pd.DataFrame(season8, columns = column_names)

# Save dataframes as csv:
# List of all season dataframes:
all_seasons_df = [season1_df, season2_df, season3_df, season4_df, season5_df, season6_df, season7_df, season8_df]
# List of season titels
season_name = ["season1", "season2", "season3", "season4", "season5", "season6", "season7", "season8"]

# Save dataframes:
counter = 0
for season in all_seasons_df:
    season.to_csv(f"out/dataframes/{season_name[counter]}_df.csv", index=False)
    counter = counter + 1

      
# CREATE AND SAVE DATAFRAME OF AVERAGE SCORES FOR ALL SEASONS:
# Empty list for average scores of all seasons:
all_seasons_avg = []

# Calculate average scores:
season_counter = 1
for season in all_seasons_df:
    pol_score_sum = 0
    subj_score_sum = 0
    
    for score in season["pol_score"]:
        pol_score_sum = pol_score_sum + score
    for score in season["subj_score"]:
        subj_score_sum = subj_score_sum + score
    
    pol_score_avg = pol_score_sum/(len(season))
    subj_score_avg = subj_score_sum/(len(season))
    
    all_seasons_avg.append((season_counter, len(season), pol_score_avg, subj_score_avg))
    
    season_counter = season_counter + 1

# Creating the dataframe:
# Column names:
column_names_avg = ["season", "comment_count", "pol_score", "subj_score"]

# Dataframe of average scores per season:
all_seasons_avg_df = pd.DataFrame(all_seasons_avg, columns = column_names_avg)

# Save dataframe:
all_seasons_avg_df.to_csv(f"out/dataframes/all_seasons_avg_df.csv", index=False)


# List of all avergae polarity scores per season
all_pol_scores_avg = []
for score in all_seasons_avg_df["pol_score"]:
    all_pol_scores_avg.append(score)

# List of all avergae subjectivity scores per season
all_subj_scores_avg = []
for score in all_seasons_avg_df["subj_score"]:
    all_subj_scores_avg.append(score)

# List of amount of comments about each season
all_comment_counts = []
for comment_count in all_seasons_avg_df["comment_count"]:
    all_comment_counts.append(comment_count)
      

# PLOTS OF POLARITY, SUBJECTIVTY AND AMOUNT OF COMMENTS PER SEASON:
# Make and save polarity plot:
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title("Average polarity")
ax.set_xlabel("Season")
ax.set_ylabel("Score")
ax.plot(season_name, all_pol_scores_avg, label="polarity")
ax.legend()
plt.savefig(f'out/plots/avg_pol_all_seasons_plot.png',dpi=100)

# Make and save subjectivity plot:
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title("Average subjectivity")
ax.set_xlabel("Season")
ax.set_ylabel("Score")
ax.plot(season_name, all_subj_scores_avg, label="subjectivity")
ax.legend()
plt.savefig(f'out/plots/avg_subj_all_seasons_plot.png',dpi=100)

# Make and save bar chart of amount of comments about each season:
fig, axs = plt.subplots(figsize=(10, 5))
axs.set_title("Amount of comments about each season")
axs.set_xlabel("Season")
axs.set_ylabel("Comments")
axs.bar(season_name, all_comment_counts)
plt.savefig(f'out/plots/comments_per_season_plot.png',dpi=100)