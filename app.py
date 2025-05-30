from flask import Flask, request, render_template
from joblib import load
import os

app = Flask(__name__)

#Load the model
model = load('model/honey_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        year = int(request.form['year'])
        prediction = model.predict([[year]])[0]
        return render_template('index.html', 
                               prediction=f'Predicted honey production for {year} is {prediction:,.2f} lbs',
                               year = year)
    except Exception as e:
        return render_template('index.html',
                               error=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
        