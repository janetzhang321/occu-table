#Janet Zhang
#Pd 6 SoftDev DW
#Work 3: Occupational Jinja Training

from flask import Flask, render_template
import csv
from random import choice, uniform

janet= Flask(__name__)


myDict = {}


import csv
with open('occupations.csv') as csvfile:
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



@janet.route("/")
def home() : 
    return __name__ + "\tHello World"


@janet.route("/occupations")
def occupations() :
    return render_template( 'table.html', foo="Jobs", collection=myDict, yourJob = randOcc())

if __name__ == "__main__": 
	janet.debug = True
	janet.run()

