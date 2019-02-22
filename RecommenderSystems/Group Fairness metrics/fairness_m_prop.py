#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:21:59 2018

@author: edgar ceh

This program implements the metric fainess_m_proportionality
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


def count_above_threshold(row, threshold=3.5):
    #print(row[0],row[1])
    count = 0
    if row[0] > threshold:
        count = count + 1
    if row[1] > threshold:
        count = count + 1
    
    return count
    

def fairness_m_proportionality():
    
    g_p = df['m_prop'].sum()
    g_size = df.shape[0]
    
    print(g_p, g_size)
    return g_p / float(g_size)
    
    
if __name__ == "__main__":
    
    df = pd.DataFrame.from_dict(data)
    #print(df)
    
    df.set_index('id', inplace=True)
    
    df['above_t'] = df.apply(count_above_threshold, axis=1)
    print(type(df))
    
    at_least_m = 1
    m_prop_count = lambda x: 1 if x >= at_least_m else 0
    
    df['m_prop'] = df['above_t'].map(m_prop_count)
    #print(df)

    print(fairness_m_proportionality())
