# Assignment 1 - Colocation Tool
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

## USAGE:
In order to reporduce this project, one must first download the input dataset from here; [Link](https://github.com/computationalstylistics/100_english_novels), and add the data to the 'in' folder in this project. One might also need to delete the blank file.

To run this script in the terminal, navigate to the folder outside the 'src' folder and run:

python3 src/assignment1.py

## DISCUSSION OF RESULTS:
The output of this project is;
- A csv file containing a dataframe of the Mutual Information scores for each word (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment1/out/MI_scores.csv).


