# Scrap
This is the data collection for the project.

sql_examples.sql provided examples for queries on the database

## CRAWL
queryGenerator.py crawls the webpage from policy.ckcest.cn/data/es/search

To use the script:
1. manually update website cookie at line 77
2. set #number of requests to generate at line 72
3. run $ python ./queryGenerator.py 

## Generate Dataset:
SepTxt.py seperates the ENTIRE dataset by year to {year}.txt files
Simply run $ python ./SepTxt.py to seperate dataset

TextToPromptedSample.py formulates dataset to different contrastive tasks, to operate the program:
1.customize file name at line 195
2.tune the ratio of tasks: classify : summary : generate = taskratioC : taskratioS : 1-taskratioC-taskratioS
3.run python $ python ./TextToPromptedSample.py to generate json datasets.