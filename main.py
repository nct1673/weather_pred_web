from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def dashboard():
    with open("/home/chen/Desktop/weather_web/data/pred_out.json") as f:
        data = json.load(f)
    # return render_template("/home/chen/Desktop/weather_web/templates/dashboard.html", data=data)
    return render_template("dashboard.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)

