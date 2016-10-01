#Janet Zhang
#Pd 6 SoftDev DW
#Work 3: Occupational Jinja Training

from flask import Flask, render_template
from utils import occutable


janet= Flask(__name__)

@janet.route("/")
def home() : 
    return __name__ + "\tHello World"


@janet.route("/occupations")
def occupations() :
    return render_template( 'table.html', foo="Jobs", collection=myDict, yourJob = randOcc())

if __name__ == "__main__": 
	janet.debug = True
	janet.run()


