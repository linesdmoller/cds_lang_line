# Assignment 3 - Network Analysis
**Language Analytics, Cultural Data Science**

By: Line Stampe-Degn Møller

Contributors: None

Link to this repository: (https://github.com/linesdmoller/cds_lang_line/tree/main/assignment3)

## PROJECT DESCRIPTION:
*This project is assignment 3 in the supplementary course, 'Language Analytics' in 'Cultural Data Science', at Aarhus University.*
- Link to assignment description: (https://github.com/CDS-AU-DK/cds-language/blob/main/assignments/assignment3.md)

**Task outline:**
If the user enters a single filename as an argument on the command line:
- Load that edgelist
  - Perform network analysis using networkx
  - Save a simple visualisation
  - Save a CSV which shows the following for every node:
    - name; degree; betweenness centrality; eigenvector_centrality
- If the user enters a directory name as an argument on the command line:
  - Do all of the above steps for every edgelist in the directory
  - Save a separate visualisation and CSV for each file

## METHODS:

In this assignment, I am writing a general .py script which can be used for network analysis, using the library, networkx.

## USAGE:
In order to reporduce this project, one must first add the input dataset, "network_data", to the 'in' folder in this project. One might also need to delete the blank file.
The dataset has been handed out by our professor and should be available to the examiner.

The folder structure in the 'in' folder (with the file, "1H4.csv", as an example) should be: "in/network_data/1H4.csv".

To run this script in the terminal, navigate to the folder outside the 'src' folder and run:

python3 src/assignment3.py in/network_data/1H4.csv

(NOTE: "network_data/1H4.csv" in the command line can be replaced with any file in the 'in' folder)

## DISCUSSION OF RESULTS:
The output of this project is;
- A csv file showing name, degree, betweenness centrality and eigenvector_centrality for every node (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment2/out/fake_news_dataframe.csv)).
- A png file showing a visualisation of the ntwork analysis (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment3/out/network.png)).

The plottet network shows, that all except two words are essentially connected. The two words that are not included in the big cluster are "Archbishop" and "SirMichael".
