# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:24:08 2019

@author: Angelo Gaerlan
"""


import numpy as np
import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors


#All possible features for a Candy
chocolate = 1
fruity = 0
caramel = 0
peanutyalmondy = 0
nougant = 0
crispedricewafer = 1
hard = 0
bar = 1
pluribus = 0

#Variable for the number of nth closest point 
number_neighbors = 10

#Read the file
df = pd.read_csv('candy_shortened.csv')

#Dataframe that contains the features 
X = df[['chocolate', 'fruity', 'caramel', 'peanutyalmondy', 'nougat', 'crispedricewafer', 'hard', 'bar', 'pluribus']]

#Dataframe which contains the labels which are Candy names. 
y = df['competitorname']

#Train the nearest neighbors classifer
knn = KNeighborsClassifier(n_neighbors=1).fit(X,y)

#Input the features to the kneighbors method. 
neigh_dist, neigh_index = knn.kneighbors([[chocolate, fruity, caramel, peanutyalmondy, nougant, crispedricewafer, hard, bar,pluribus ]],n_neighbors=number_neighbors)

#print out the nth nrearest neighbors from the query point.
#prints the candy names which are most alike to that of the input features
for i in range(len(neigh_index[0])):
    print('Candy #{}: {}'.format(i+1,y.iloc[neigh_index[0][i]]))




