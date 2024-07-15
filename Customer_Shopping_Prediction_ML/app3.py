# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 20:02:21 2024

@author: madha
"""

from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import os

app = Flask(__name__)

x_path=os.path.dirname(os.path.abspath(__file__))

# Load the model, scaler, and label encoders
model = joblib.load(os.path.join(x_path,'kmeans_model5.pkl'))
scaler = joblib.load(os.path.join(x_path,'scaler5.pkl'))
label_encoders = joblib.load(os.path.join(x_path,'label_encoders5.pkl'))

@app.route('/')
def welcom():
    return render_template('index3.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Convert data into DataFrame
    df = pd.DataFrame(data, index=[0])
    
    # Encoding categorical variables
    for column in ['gender', 'category', 'payment_method', 'shopping_mall']:
        le = label_encoders[column]
        df[column] = le.transform(df[column])
    
    # Feature scaling
    df[['age', 'quantity', 'price']] = scaler.transform(df[['age', 'quantity', 'price']])
    
    # Making predictions
    prediction = model.predict(df)
    
    return jsonify({'predicted_cluster': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
