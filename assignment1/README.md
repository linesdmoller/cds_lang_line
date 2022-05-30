# Assignment 1 - Collocation Tool
**Language Analytics, Cultural Data Science**

By: Line Stampe-Degn Møller

Contributors: None

Link to this repository: (https://github.com/linesdmoller/cds_lang_line/tree/main/assignment1)

## PROJECT DESCRIPTION:
*This project is assignment 1 in the supplementary course, 'Langage Analytics' in 'Cultural Data Science', at Aarhus University.*
- Link to assignment description: (https://github.com/CDS-AU-DK/cds-language/blob/main/assignments/assignment1.md)

**Task outline:**
- Take a user-defined search term and a user-defined window size.
- Take one specific text which the user can define.
- Find all the context words which appear ± the window size from the search term in that text.
- Calculate the mutual information score for each context word.
- Save the results as a CSV file with (at least) the following columns: the collocate term; how often it appears as a collocate; how often it appears in the text; the mutual information score.

## METHODS:
The dataset used in this project stems from; (https://github.com/computationalstylistics/100_english_novels).

Words which frequently co-occur together in a given context are known as collocates. The task of this assignment is to perform collocational analysis using simple string processing and NLP tools. the main NLP library used in this process is the Spacy library. I calculate the strength of the assiciation between collocates using the formula described below. I then sort the collocates by MI-score from highest to lowest an save the data as a csv.

**MI-score calculation formula:**

MI = log ( (AB * sizeCorpus) / (A * B * span) ) / log (2)

Example of calculation:

Suppose we are calculating the MI for the collocate color near purple in BNC.

- A = frequency of node word (e.g. purple): 1262
- B = frequency of collocate (e.g. color): 115
- AB = frequency of collocate near the node word (e.g. color near purple): 24
- sizeCorpus= size of corpus (# words; in this case the BNC): 96,263,399
- span = span of words (e.g. 3 to left and 3 to right of node word): 6
- log (2) is literally the log10 of the number 2: .30103

MI = 11.37 = log ( (24 * 96,263,399) / (1262 * 115 * 6) ) / .30103


## USAGE:
In order to reporduce this project, one must first download the input dataset from here; [Link](https://github.com/computationalstylistics/100_english_novels), and add the data to the 'in' folder in this project. One might also need to delete the blank file.

To run this script in the terminal, navigate to the folder outside the 'src' folder and run:

python3 src/assignment1.py

## DISCUSSION OF RESULTS:
The output of this project is;
- A csv file containing a dataframe of the Mutual Information scores for each word (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment1/out/MI_scores.csv).


