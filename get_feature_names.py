# -*- coding: utf-8 -*-

import pandas as pd

def get_feature_names():

    df = pd.read_csv('new_test.csv')
    features = list(df.columns)
    
    return features
