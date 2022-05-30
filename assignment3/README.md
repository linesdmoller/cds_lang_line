# Assignment 3 - Network Analysis
**Language Analytics, Cultural Data Science**

By: Line Stampe-Degn Møller

Contributors: None

Link to this repository: (https://github.com/linesdmoller/cds_lang_line/tree/main/assignment3)

## PROJECT DESCRIPTION:
*This project is assignment 3 in the supplementary course, 'Language Analytics' in 'Cultural Data Science', at Aarhus University.*
- Link to assignment description: (https://github.com/CDS-AU-DK/cds-language/blob/main/assignments/assignment3.md)

**Task outline:**
Using the corpus of Fake vs Real news, write some code which does the following:
- Split the data into two datasets - one of Fake news and one of Real news
- For every headline
   - Get the sentiment scores
   - Find all mentions of geopolitical entites
   - Save a CSV which shows the text ID, the sentiment scores, and column showing all GPEs in that text
- Find the 20 most common geopolitical entities mentioned across each dataset - plot the results as a bar charts

## METHODS:

xx

## USAGE:
In order to reporduce this project, one must first add the input dataset, "fake_or_real_news", to the 'in' folder in this project. One might also need to delete the blank file.
The dataset has been handed out by our professor and should be available to the examiner.

The folder structure in the 'in' folder should be: "in/tabular_examples/fake_or_real_news.csv".

To run this script in the terminal, navigate to the folder outside the 'src' folder and run:

python3 src/assignment3.py

## DISCUSSION OF RESULTS:
The output of this project is;
- A csv file containing a dataframe of the fake news (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment2/out/fake_news_dataframe.csv)).
- A csv file containing a dataframe of the real news (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment2/out/real_news_dataframe.csv)).
- A png file of a gpe plot of the fake news (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment2/out/fake_news_gpe_plot.png)).
- A png file of a gpe plot of the real news (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment2/out/real_news_gpe_plot.png)).

xx
