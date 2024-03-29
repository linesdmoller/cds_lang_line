# Assignment 2 - Sentiment and NER (2.2: Real vs Fake news)
**Language Analytics, Cultural Data Science**

By: Line Stampe-Degn Møller

Contributors: None

Link to this repository: (https://github.com/linesdmoller/cds_lang_line/tree/main/assignment2)

## PROJECT DESCRIPTION:
*This project is assignment 2 in the supplementary course, 'Language Analytics' in 'Cultural Data Science', at Aarhus University.*
- Link to assignment description: (https://github.com/CDS-AU-DK/cds-language/blob/main/assignments/assignment2.md)

**Task outline:**
Using the corpus of Fake vs Real news, write some code which does the following:
- Split the data into two datasets - one of Fake news and one of Real news
- For every headline
   - Get the sentiment scores
   - Find all mentions of geopolitical entites
   - Save a CSV which shows the text ID, the sentiment scores, and column showing all GPEs in that text
- Find the 20 most common geopolitical entities mentioned across each dataset - plot the results as a bar charts

## METHODS:

For this project, I use the NLP library, Spacy, to find what is known as named entities. I then use spacytextblob to calculate the sentiment score for a stretch of natural language.

## USAGE:
In order to reporduce this project, one must first add the input dataset, "fake_or_real_news", to the 'in' folder in this project. One might also need to delete the blank file.
The dataset has been handed out by our professor and should be available to the examiner.

The folder structure in the 'in' folder should be: "in/tabular_examples/fake_or_real_news.csv".

To run this script in the terminal, navigate to the folder outside the 'src' folder and run:

python3 src/assignment2.py

## DISCUSSION OF RESULTS:
The output of this project is;
- A csv file containing a dataframe of the fake news (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment2/out/fake_news_dataframe.csv)).
- A csv file containing a dataframe of the real news (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment2/out/real_news_dataframe.csv)).
- A png file of a gpe plot of the fake news (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment2/out/fake_news_gpe_plot.png)).
- A png file of a gpe plot of the real news (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment2/out/real_news_gpe_plot.png)).

The plots show that Russia, U.S. and Syria are among the highest ranked in spreading of fake news. On the oter hand, Iran, U.S. and Syria are the highest ranked in spreading of real news. The United states are plotted as separate GPEs ("U.S.", "US", "America", etc.) - if we were to bundle these together, the number of GPEs for The United States would be even higher, probably ranking them as NO. 1 on both the fake and the real news plot.
