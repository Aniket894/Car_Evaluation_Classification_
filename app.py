from flask import Flask, render_template, request
import pickle
import numpy as np
import joblib

app = Flask(__name__)


model = joblib.load(open('notebooks/GradientBoostingClassifier (1).joblib','rb'))

# model = pickle.load(open('notebooks/GradientBoostingClassifier.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['Get','POST'])
def predict():

    if request.method == 'POST':

        buying = int(request.form['buying'])
        maint = int(request.form['maint'])
        doors = int(request.form['doors'])
        persons =int(request.form['persons'])
        lug_boot = int(request.form['lug_boot'])
        safety = int(request.form['safety'])
        # Get data from form
        user_input = [[buying,maint,doors,persons,lug_boot, safety]]
        
        # Assuming the input needs to be preprocessed by the encoder
        
        features = np.array([[buying, maint, doors, persons, lug_boot, safety]])

            # Predict using the model
        prediction = model.predict(features)

        return render_template('results.html', prediction=prediction[0])

        
    else:
        return render_template('index.html')

        
        

if __name__ == '__main__':
    app.run(debug=True)
