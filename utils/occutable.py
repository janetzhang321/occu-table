#Janet Zhang
#Pd 6 SoftDev DW
#Work 3: Occupational Jinja Training

import csv
from random import choice, uniform



myDict = {}



with open('data/occupations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        job = row['Job Class']
        percent = float(row['Percentage'])
        if (job != 'Total'): myDict[job] = percent



def randOcc():
    benchmark = uniform(0, sum(myDict.itervalues())) #random number between 0 and the sum of the values of each key 
    total = 0.0
    for key in myDict:
        total+=myDict[key]
        if benchmark < total:
            return key
    return key
