#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 05:21:52 2021

@author: ongsooliew
"""
import json 
import pandas as pd

def parse_and_clean(js):
    #Parse API response
    parsed_data = json.loads(js)
    flatten=pd.json_normalize(parsed_data['data'])
    flatten.rename(columns={'region.iso': 'iso', 
                            'confirmed': 'num_confirmed', 
                            'deaths' : 'num_deaths',
                            'recovered' : 'num_recovered'}, inplace=True)
    df=flatten[['date','iso','num_confirmed', 'num_deaths', 'num_recovered']]
    
    return df


def test_parse_and_clean(): #check if function is able to parse dummy json file correctly
    json_file = open('Dummy_Data/dummy.json')
    data= json.load(json_file)
    df= parse_and_clean(data)
    assert len(df) == 58
    
    
    
if __name__ == "__main__":
     test_parse_and_clean()