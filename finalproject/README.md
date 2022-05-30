# Final Project - Game of Thrones sentiment on Reddit
**Language Analytics, Cultural Data Science**

By: Line Stampe-Degn Møller

Contributors: None

Link to this repository: (https://github.com/linesdmoller/cds_lang_line/tree/main/finalproject)

## PROJECT DESCRIPTION:
*This project is a self-assigned project submitted as a final project in the supplementary course, 'Language Analytics' in 'Cultural Data Science', at Aarhus University.*

**Goal:**
The goal of this project is to analyse how fans of the TV-show, Game of Thrones, feel about each of the eight seasons of the show. This will presumably give insight into which seasons the fans like and dislike the most.

## METHODS:
The dataset used in this project stems from; (https://www.kaggle.com/datasets/nikhilkhetan/game-of-thrones).

I approach the goal of this project first of all by downloading a dataset of web-scraped comments about Game of Thrones from Reddit. I then sort these into seperate lists by tokenizing and search for token combinations of fx "season 1", "1st season" or "first season" (same for the other seasons). Through spacytextblob, I then tokenize and do sentiment analysis on the comments by calculating their polarity score and subjectivity score. I also count the amount of comments about each season. I turn each list into seperate dataframes for the eight seasons and save them as csv files. I then calculate the average polarity and subjectivity score for each season and create and save a dataframe (csv) of those avergae scores and the amount of comments per season. Finally, I make create and save three plots: average polarity scores per seaosn, average subjectivity score per season, and amount of comments per season.

**About sentiment analysis with spacytextblob:**
- Polarity: negative vs. positive (-1.0 => +1.0)
- Subjectivity: objective vs. subjective (+0.0 => +1.0)

## USAGE:
In order to reporduce this project, one must first download the input dataset from here; [Link](https://www.kaggle.com/datasets/nikhilkhetan/game-of-thrones), and add the data to the 'in' folder in this project. One might also need to delete the blank file.

To run this script in the terminal, navigate to the folder outside the 'src' folder and run:

python3 src/finalproject.py

## DISCUSSION OF RESULTS:
The output of this project is;
- Eight csv files containing dataframes of the content of each comment, their polarity and subjectivity scores (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/finalproject/out/dataframes) - NOTE: you might need to scroll far to the right past the comments to see the scores).
- A csv file containing a summarized dataframe of the average polarity and subjectivity scores and the amount of comments about each season (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/finalproject/out/dataframes/all_seasons_avg_df.csv)).
- A png file containing a plot of average polarity for each season (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/finalproject/out/plots/avg_pol_all_seasons_plot.png)).
- A png file containing a plot of average subjectivity for each season (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/finalproject/out/plots/avg_subj_all_seasons_plot.png)).
- A png file containing a bar plot of the amount of comments about each season (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/finalproject/out/plots/comments_per_season_plot.png)).

Acording to the average polarity scores of each season, the seasons with the most positive reactions ranked highest-lowest are:
- Season 1
- Season 7
- Season 6
- Season 8
- Season 5
- Season 3
- Season 2
- Season 4

It makes sense that season 1 is on the top. However, contrary to my assumption, season 8 is not all the way at the bottom of the list.

If we look at the amount of comments for each season, the most discussed seasons on Reddit ranked are:
- Season 8
- Season 1
- Season 7
- Season 2
- Season 6
- Season 5
- Season 4
- Season 3

According to this ranking, the two first and the two last seasons are the most duscussed seasons on the forum. This makes a lot of sense, since these are the ones people first start out watching, and then the big finale of the show (which has been critisized a lot by fans of the show).

According to the average subjectivity score plot, people expressed the most subjective comments about season 3 and 4. In the more objective end of the spectrum, we find season 1 and 2. This is a little bit surprising, since I was assuming season 8 would rank higher, with more subjective (negative) comments.

This project aimed at investigating fans' reaction to each of the eight seasons of the TV-show, Game of Thrones, via sentiment analysis. Though it has to be said, that since the dataset is relatively small (about 2000 comments), and only a handfull who mention a specific season (153 comments), the data is not a representative sample. 
This means, that the output of the project is also not representative enough to conclude much from. However, this project can easily be reexecuted with another larger dataset. Therfore, the project is still very much relevant in the exploration of how one might investigate a sentimental discourse in feedback from a consumer crowd via programming. 
An analysis like this is widely applicable in the marketing field where a brand might want to know how the consumers generally respond to their products.
