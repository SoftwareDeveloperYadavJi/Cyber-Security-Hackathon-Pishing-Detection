from flask import Flask, request, render_template, jsonify
import joblib
import os
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load the model and vectorizer
model_path = 'phishing_model.pkl'
vectorizer_path = 'vectorizer.pkl'

if not os.path.exists(model_path):
    raise FileNotFoundError(f"The model file '{model_path}' does not exist.")
if not os.path.exists(vectorizer_path):
    raise FileNotFoundError(f"The vectorizer file '{vectorizer_path}' does not exist.")

loaded_model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('url')
    features = vectorizer.transform([url])
    prediction = loaded_model.predict(features)
    result = "Phishing" if prediction[0].lower() == 'phishing' else "Legitimate"
    return render_template('result.html', prediction=result)

@app.route('/check-url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data['url']
    features = vectorizer.transform([url])
    prediction = loaded_model.predict(features)
    result = "Phishing" if prediction[0].lower() == 'phishing' else "Legitimate"
    logging.debug(f"URL checked: {url}, Result: {result}")
    return jsonify({'isPhishing': result == "Phishing"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

