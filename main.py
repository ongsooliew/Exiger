#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 05:02:57 2021

@author: ongsooliew
"""
#import libraries
import yaml
import logging
import json 
import requests
import pandas as pd
from datetime import datetime
from utils.myfunctions import parse_and_clean


#Read user config file
environment='prod_env'
config_parameters = yaml.safe_load(open("config.yaml"))
excelfile_dir= config_parameters[environment]['excelfile_dir']
output_dir= config_parameters[environment]['output_dir']
logfile_dir= config_parameters[environment]['logfile_dir']


#Setup Log File
runtime= str(datetime.now())
logging.basicConfig(filename= logfile_dir + f'{runtime}.log', 
                    level=logging.INFO, filemode='w', 
                    format='%(asctime)s - %(levelname)s - %(message)s')


#Read excelfile for ISO-DATE pairs
input_df= pd.read_excel(excelfile_dir)
excelfile_count=len(input_df)


#Loop through ISO-DATE Pairs
success_count=0

for ind,row in input_df.iterrows():
    
    dt= row['date']
    iso_code = row['iso']

    #Make API Call and parse response
    try:
        logging.info(f"Retrieving data for {iso_code}-{dt}")       
        api_query=f"https://covid-api.com/api/reports?date={dt}&iso={iso_code}"
        headers = {"accept": "application/json","X-CSRF-TOKEN": ""}      
        
        response = requests.request("GET", api_query, headers=headers)
        logging.info(f"API status code: {response.status_code}")
        
        df=parse_and_clean(response.text)
           
    except Exception as e:
        logging.error(str(e))
        break

        
    #Save file 
    filename= iso_code+'_'+dt
    df.to_excel(output_dir+ f'{filename}.xlsx', index=False)
    
    logging.info(f'{filename}.xlsx saved.')
    success_count+=1
    
    
logging.info(f"Downloaded and saved data for {success_count} out of {excelfile_count} ISO-Date Pairs")




        
        

