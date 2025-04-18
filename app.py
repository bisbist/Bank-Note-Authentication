from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
import pickle

app=Flask(__name__)

classifier=pickle.load(open('classifier.pkl','rb'))
print(classifier)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_note_authentication():

    # Get values from form
    variance = float(request.form['variance'])
    skewness = float(request.form['skewness'])
    curtosis = float(request.form['curtosis'])
    entropy = float(request.form['entropy'])

    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])

    return render_template("index.html",prediction_text="The Bank Note Authentication prediction is {}".format(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
