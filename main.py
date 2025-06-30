from flask import Flask, render_template
import json
from config import server_config

app = Flask(__name__)

@app.route('/')
def dashboard():
    filename = f'/home/{server_config}/weather_web/data/pred_out.json'
    with open(filename) as f:
        data = json.load(f)
    return render_template("dashboard.html", data=data)

@app.route('/details')
def details():
    filename = f'/home/{server_config}/weather_web/data/pred_out.json'
    with open(filename) as f:
        data = json.load(f)
    return render_template("details.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)

