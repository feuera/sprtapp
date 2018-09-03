from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import activityio as aio
import pandas as pd
from glob import glob

pre = '../stravaD/activities/'
dfF = '1190103531.fit'

app = Flask(__name__)



@app.route('/dat/')
def getData():
    fstr = request.args.get('a', dfF, type=str)
    print(pre+fstr)
    df = aio.read(pre+fstr)
    d = [[i, x] for i,x in enumerate(df.hr[df.hr.notna()])]
    gpsD = [[x[1].lat, x[1].lon] for x in df.iterrows()]
    return jsonify({'hr':[d], 'gps':gpsD})

@app.route('/')
def hello_world():
    f = glob('../stravaD/activities/*.fit')
    fn = [x.split('/')[-1] for x in f]
    return render_template('./main.html', files=fn)

