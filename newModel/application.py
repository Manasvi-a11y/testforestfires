import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

application = Flask(__name__)
app = application

# Build absolute paths safely
base_path = os.path.dirname(__file__)
ridge_path = os.path.join(base_path, 'models', 'ridge.pkl')
scaler_path = os.path.join(base_path, 'models', 'scaler.pkl')

# Load model and scaler
ridge_model = pickle.load(open(ridge_path, 'rb'))
standard_scaler = pickle.load(open(scaler_path, 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == "POST":
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data_scaled)

        return render_template('home.html',result=result[0])
    else:
        return render_template('home.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
