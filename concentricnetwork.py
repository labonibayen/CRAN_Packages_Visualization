from flask import Flask
from flask import Flask, render_template
from json import loads, dumps
import pandas as pd

app = Flask(__name__)

@app.route("/concentricnetwork")
def hello():
    filename = '~/concentricnetwork/static/data.csv'
    data = pd.read_csv(filename, header=0)
    final_data = data.to_json(orient="records")
    return render_template('index.html', myData=final_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
