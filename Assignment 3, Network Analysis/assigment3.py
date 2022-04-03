### Assignment 3
# By Line Stampe-Degn Møller
# Language Analytics, Cultural Data Science

## USAGE:

#To run this script:
#python/python3 assigment3.py network_data/1H4.csv


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
plt.rcParams["figure.figsize"] = (20,20)



#Read filename from command line argument
# https://www.tutorialspoint.com/python/python_command_line_arguments.htm

try:
	input_file = sys.argv[1]
except:
	#if not filename provided, we will take 1 by default
	input_file = "network_data/1H4.csv"

'''
# Read CSV file

with open(filename, newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
	for row in spamreader:
		print(', '.join(row))
'''

# Read TSV file
#edges_df = pd.read_csv(input_file, delimiter="\t")
edges_df = pd.read_csv(input_file, delimiter="\t", usecols=[0,2,3])

#print(edges_df)
#print(type(edges_df))

#Filter (optional, keep 1 of the two following lines commented)

filtered = edges_df
#filtered = edges_df[edges_df["Weight"]>10]


print(filtered)

print("NO PROBLEMS until here")

G = nx.from_pandas_edgelist(filtered, "Source", "Target", "Weight")

print(G)

nx.draw_networkx(G, with_labels=True, node_size=20, font_size=10)

#SAVE A SIMPLE VISUALIZATION

#Make sure the folder ../viz exists already for saving the image

outpath_viz = os.path.join('viz',' network.png')
plt.savefig(outpath_viz, dpi=300, bbox_inches="tight")



#Centrality measures

ev = nx.eigenvector_centrality(G)

eigenvector_df = pd.DataFrame(ev.items())

eigenvector_df.sort_values(1, ascending=False)

bc = nx.betweenness_centrality(G)
betweenness_df = pd.DataFrame(bc.items()).sort_values(1, ascending=False)


print(eigenvector_df)

print(betweenness_df)

#WRITE OUTPUT
#https://docs.python.org/3/library/csv.html

outputs = []

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Name', 'Degree', 'betweenness_centrality', "eigenvector_centrality"])

    for i in range(len(eigenvector_df)):
    	name = eigenvector_df[0][i]
    	degree = "?"
    	eigenvector_cen = eigenvector_df[1][i]
    	#Search for the corresponding betweenness_centrality
    	betweenness_cen = 0
    	for j in range(len(betweenness_df)):
    		if name == betweenness_df[0][j]: # If same name, take betweenness_centrality value, from the second df
    			betweenness_cen = betweenness_df[1][j]

    	writer.writerow([name, degree, betweenness_cen, eigenvector_cen])
