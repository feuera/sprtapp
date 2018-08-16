from flask import Flask
from flask import render_template
from flask import jsonify 
import activityio as aio
import pandas as pd
from glob import glob

pre = '../stravaD/activities/'
dfF = '1190103531.fit'

app = Flask(__name__)

@app.route('/dat')
def getData(fstr=dfF):
    df = aio.read(pre+fstr)
    return jsonify(list(df.hr))

@app.route('/')
def hello_world():
    f = glob('../stravaD/activities/*.fit')
    fn = [x.split('/')[-1] for x in f]
    return render_template('./main.html', files=fn)

