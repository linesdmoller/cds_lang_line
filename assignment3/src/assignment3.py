### Assignment 3 - Network Analysis
# By Line Stampe-Degn Møller
# Language Analytics, Cultural Data Science

## TASKS:
# If the user enters a single filename as an argument on the command line:
# - Load that edgelist
#   - Perform network analysis using networkx
#   - Save a simple visualisation
#   - Save a CSV which shows the following for every node:
#     - name; degree; betweenness centrality; eigenvector_centrality
# - If the user enters a directory name as an argument on the command line:
#   - Do all of the above steps for every edgelist in the directory
#   - Save a separate visualisation and CSV for each file

## USAGE:
# In terminal, add:
# pip install spacy
# python -m spacy download en_core_web_sm
# pip install networkx

# To run this script:
# python3 src/assignment3.py in/network_data/1H4.csv

# (NOTE: "network_data/1H4.csv" in the command line can be replaced with any file in the 'in' folder)

# IMPORTS

# System tools
import os
import csv
import sys

# Data analysis
import pandas as pd
from collections import Counter
from itertools import combinations 
from tqdm import tqdm

# NLP
import spacy
nlp = spacy.load("en_core_web_sm")

# Network analysis tools
import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (3,3)

# Read filename from command line argument

try:
    input_file = sys.argv[1]
except:
    # If not filename provided, we will take 1 by default
    input_file = "in/network_data/1H4.csv"

'''
# Read CSV file

with open(filename, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
'''

# Read CSV file
edges_df = pd.read_csv(input_file, delimiter="\t", usecols=[0,2,3])

#print(edges_df)
#print(type(edges_df))

# Filter (optional, keep 1 of the two following lines commented):
filtered = edges_df
#filtered = edges_df[edges_df["Weight"]>10]

print(filtered)

G = nx.from_pandas_edgelist(filtered, "Source", "Target", "Weight")

print(G)

nx.draw_networkx(G, with_labels=True, node_size=1, font_size=3)

# SAVE A SIMPLE VISUALIZATION:

outpath_viz = os.path.join("out/network.png")
plt.savefig(outpath_viz, dpi=300, bbox_inches="tight")

#Degrees

degrees = G.degree

degrees_df = pd.DataFrame(degrees, columns = ["Name", "Degrees"])


#Centrality measures

ev = nx.eigenvector_centrality(G)

eigenvector_df = pd.DataFrame(ev.items(), columns = ["Name", "Betweenness_centrality"])

bc = nx.betweenness_centrality(G)
betweenness_df = pd.DataFrame(bc.items(), columns = ["Name", "Eigenvector_centrality"])

#print(degrees_df)

#print(eigenvector_df)

#print(betweenness_df)


df = degrees_df.merge(eigenvector_df).merge(betweenness_df)

#print(df)

df.to_csv("out/output.csv")
