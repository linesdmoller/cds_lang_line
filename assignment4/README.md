# Assignment 4: Text Classification
**Language Analytics, Cultural Data Science**

By: Line Stampe-Degn Møller

Contributors: None

Link to this repository: (https://github.com/linesdmoller/cds_lang_line/tree/main/assignment4)

## PROJECT DESCRIPTION:
*This project is assignment 4 in the supplementary course, 'Language Analytics' in 'Cultural Data Science', at Aarhus University.*
- Link to assignment description: (https://github.com/CDS-AU-DK/cds-language/blob/main/assignments/assignment4.md)

**Task outline - pt 1; classification with machine learning:**

The first script should perform benchmark classification using standard machine learning approaches
- This means CountVectorizer() or TfidfVectorizer(), LogisticRegression classifier
- Save the results from the classification report to a text file

**Task outline - pt 2; classification with deep learning:**

The second script should perform classification using the kind of deep learning methods we saw in class
- Keras Embedding layer, Convolutional Neural Network
- Save the classification report to a text file

## METHODS:

xx

## USAGE:
In order to reporduce this project, one must first download the input dataset from the sign up link in this document; [Link](https://www.simula.no/sites/default/files/publications/files/cbmi2019_youtube_threat_corpus.pdf), and add the data to the 'in' folder in this project. One might also need to delete the blank file.

I presume the data has also been made available for th examiner by our professor.

The folder structure in the 'in' folder should be: "in/toxic/VideoCommentsThreatCorpus.csv".

**Run pt 1:**

To run this script in the terminal, navigate to the folder outside the 'src' folder and run:

python3 src/assignment4pt1.py

**Run pt 1:**

To run this script in the terminal, navigate to the folder outside the 'src' folder and run:

python3 src/assignment4pt2.py


## DISCUSSION OF RESULTS:
The output of this project is;
- A csv file containing a classification report from the machine learing approach in pt 1 (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment4/out/cl_report_pt1.txt)).
- A csv file containing a classification report from the deep learing approach in pt 2 (see [Link](https://github.com/linesdmoller/cds_lang_line/blob/main/assignment4/out/cl_report_pt2.txt)).
xx
