
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import statsmodels.api as sm
from sklearn import linear_model

app = Flask(__name__)
model = joblib.load(open('rfc_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = np.array(int_features)
    prediction = model.predict([final_features])
    output = prediction
    if(output == 1):
        output = "EVET"
    elif(output == 0):
        output = "HAYIR"
    else:
        pass
    return render_template("index.html", prediction_text='COVID-19 Test Sonucunuz: {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)