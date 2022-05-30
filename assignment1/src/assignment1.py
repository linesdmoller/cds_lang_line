### Assignment 1 - Collocation Tool
# By Line Stampe-Degn Møller
# Language Analytics, Cultural Data Science

## TASKS:
# - Take a user-defined search term and a user-defined window size.
# - Take one specific text which the user can define.
# - Find all the context words which appear ± the window size from the search term in that text.
# - Calculate the mutual information score for each context word.
# - Save the results as a CSV file with (at least) the following columns: the collocate term; how often it appears as a collocate; how often it appears in the text; the mutual information score.

## USAGE:
# To run this script:
# python3 src/assignment1.py

## In terminal, add:
# pip install spacy
# python -m spacy download en_core_web_sm

# IMPORTS:
# Import libraries
import spacy
import os
import string
import math
import csv

nlp = spacy.load("en_core_web_sm")

### 1. Take a user-defined search term and a user-defined windows size

# Define search word, pos (word class) and window size:
keyword = "sailor"
pos = "NOUN"
window_size = 3  # Before and after keyword (3 + keyword + 3)

### 2. Take one specific text which the user can define

# Load one text from the data folder
#!rm Conrad_Nostromo_1904.txt*
#!wget https://raw.githubusercontent.com/computationalstylistics/100_english_novels/master/corpus/Conrad_Nostromo_1904.txt
txt = open("in/100_english_novels/corpus/Conrad_Nostromo_1904.txt").read()

# Check the data type and print the first part of the text to know what format we're working with:
print(f"The data type is a: {type(txt)}")  # Result: 'str' (a string), which is the expected data type to move forward with.
print("#################")
print("ORIGINAL TEXT (sample):")
print(txt[:500])  # Sample from first part of string

# Normalization of text string:
# Make everything lower case
txt_lower = txt.lower()

# Remove all new lines
txt_no_newlines = " ".join(txt_lower.split("\n"))
#print(txt_no_newlines[0:200])

# Remove all punctuations
txt_no_punctuations = txt_no_newlines.translate(str.maketrans('', '', string.punctuation))  # https://datagy.io/python-remove-punctuation-from-string/
    # Comment: by removing all punctuation, I'm also removing some meaning, fx. genitive case: "sailors" vs. "sailor's".
#print(txt_no_punctuations[:200])

# Remove all double spaces
txt_clean = " ".join(txt_no_punctuations.split("  "))
#print(txt_clean[0:200])

# Put through a spaCy pipeline (tokenization = separate into words and characters).
print("\n Curently working on tokenization - this may take a while...")
doc = nlp(txt_clean)

# Check output
print("CLEAN TEXT (sample):")
print(doc[:200])  # Sample from first part of string

### 3. Find all the context words which appear +- the window size from the search term in that text

colloc = []  # Empty list for list for colloc words related to the keyword.

# Finding colloc words and saving them in list
for token in doc:
    if token.text == keyword and token.pos_ == pos:
        before = token.i - window_size        # Defining start index as [window_size] spaces BEFORE the index of the keyword.
        after = token.i + window_size + 1     # Defining end index as [window_size] spaces AFTER the index of the keyword (+1 for keyword).
        span = doc[before:after]              # Defining the span as the content of the doc string between the index spaces defined earlier.
        colloc.append([token, span])          # Saving lists of context words in list.
    else:
        pass
    
### 4. Calculate the mutual information score for each context word

## Example of MI calculation:
# from https://www.english-corpora.org/mutualInformation.asp

## Formula:
# MI = log ( (AB * sizeCorpus) / (A * B * span) ) / log (2)

# Suppose we are calculating the MI for the collocate color near purple in BNC.

# - A = frequency of node word (e.g. purple): 1262
# - B = frequency of collocate (e.g. color): 115
# - AB = frequency of collocate near the node word (e.g. color near purple): 24
# - sizeCorpus= size of corpus (# words; in this case the BNC): 96,263,399
# - span = span of words (e.g. 3 to left and 3 to right of node word): 6
# - log (2) is literally the log10 of the number 2: .30103

# MI = 11.37 = log ( (24 * 96,263,399) / (1262 * 115 * 6) ) / .30103

print("\n Curently calculating the Mutual Information scores - this may take a while...")

def calc_freq(token, text):
    # Calculate the frequency of a token on a text document:
    freq = 0
    for word in text:
        if word.text == token.text:
            freq += 1
    return freq


def calc_colloc_freq(token, colloc):
    freq = 0
    # Calculate the frequency of a token on a colloc span:
    for c in colloc:
        span = c[1]
        for word in span:
            if token.text == word.text:
                freq += 1
    return freq

sizeCorpus = len(doc)
span_size = 2 * window_size
log2  = 0.30103

output = []  # Empty list for output (result of MI calculations)

for c in colloc:
    span = c[1] # Since the structure of the colloc list is [token, span] the index [1] indicates the span.

    for word in span:
        if word.text == keyword:
            pass
        else:
            A = calc_freq(c[0], doc)
            B = calc_freq(word, doc)
            AB = calc_colloc_freq(word, colloc)
            # Calculate the Mutual Information score:
            MI = math.log(( (AB * sizeCorpus) / (A * B * span_size) ) / log2)  # https://www.geeksforgeeks.org/log-functions-python/

            # Append [term], [freq], [doc_freq], [mut_inf_sco]
            appendix = [word.text, AB, B, MI]
            if appendix not in output:
                output.append(appendix)

# Sort output highest-lowest based on the MI score
sorted_output = sorted(output, key=lambda x:x[3], reverse=True)  # The index [3] indicates the MI score in the output list

### 5. Save the results as a CSV file:

header = ['term', 'freq', 'doc_freq', 'mut_inf_sco']

with open('out/MI_scores.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # Write the header
    writer.writerow(header)

    # Write multiple rows
    for out in sorted_output:
        writer.writerow(out)

print("\n MI scores are now saved as csv file in the 'out' folder.")
        
