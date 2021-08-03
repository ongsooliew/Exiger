# Exiger Challenge

Main.py contains ETL code, which perform the followings:
- read config.yaml to get directory of excel file, ISO-DATE Pairs.xlsx
- Loop through and make API call for each ISO-DATE pair
- JSON response, from API call, is parsed and saved to output/
- Log generated will be written to "log file/", on a per run basis
- utils folder contains user defined functions (UDF) to help parse the JSON response, and unittest.
- Requirements.txt contain python libraries necessary to run the software
