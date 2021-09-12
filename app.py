from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
import subprocess

app = Flask(__name__)


@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return gm(request.args.get('data'))

@app.route('/')
def index():
    return render_template('index.html', graphJSON=gm())
def gm(data='Humidity'):
    df = pd.read_csv("./data/df.csv")
    df = df.assign(metric = df[data])

    fig = px.line(df.assign(metric=df[data]), x="Time", y='metric')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return  graphJSON

@app.route('/on')
def update():
    subprocess.call(['python3 scripts/test_data.py'], shell=True)
    return '', 204  # no content

if __name__ == "__main__":
    app.run()