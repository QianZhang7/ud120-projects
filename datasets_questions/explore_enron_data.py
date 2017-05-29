#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)

print len(enron_data[enron_data.keys()[0]])

counter = 0
for person in enron_data.keys():
    if enron_data[person]['poi'] == 1:
        counter = counter + 1
        
print counter

import pandas as pd
poi_names = pd.read_csv("../final_project/poi_names.txt")

print len(poi_names)

print enron_data['PRENTICE JAMES']

print enron_data['COLWELL WESLEY']