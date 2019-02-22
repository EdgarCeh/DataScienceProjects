#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:21:59 2018

@author: edgar ceh

This program implements the metric fainess_m_envy
from the paper:
    "Fairness in package-to-group recommendations", Serbos et al.

"""

import pandas as pd

# This test data represents a group of 4 users (58,72,13,141)
# with ratings for a package of 2 items (47, 386) from different categories
# and the corresponding ratings

data = {'id':[58, 72, 13, 141], 
        '47':[4.297310, 5.0, 5.0, 3.744998],
        '386':[6.588911, 4.539560, 4.671606, 4.410989]}


def extract_percentage(col):
    
    val_list = col.tolist()
    val_list_sorted = sorted(val_list, reverse=True)
    top_items = int(len(val_list) * percentage)
    top_items = val_list_sorted[:top_items]
    top_items_list.append(top_items)
    
def find_envy(row):
    
    cats = row.tolist()
    print(cats)
    number_of_true = 0
    
    for i in range(len(cats)):
        if cats[i] in top_items_list[i]:
            number_of_true = number_of_true + 1
    
    if number_of_true >= m_items:
        return True
    else:
        return False
    

def fairness_m_envy():
    g_p = df['m_envy'].sum()
    g_size = df.shape[0]
    
    return g_p / float(g_size)
    
    
if __name__ == "__main__":
    
    df = pd.DataFrame.from_dict(data)
    #print(df)
    
    df.set_index('id', inplace=True)
    print(df)
    
    percentage = 0.25 #Top % of items
    m_items = int(df.shape[1] / 2)
    print('minumum items: ',m_items)
    top_items_list = []
    df.apply(extract_percentage, axis=0)
   
    df['m_envy'] = df.apply(find_envy, axis=1)
    
    print(fairness_m_envy())

    