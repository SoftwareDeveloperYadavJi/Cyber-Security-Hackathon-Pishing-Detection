from flask import Flask, request, render_template
import joblib
import os

app = Flask(__name__)

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

    # Log the input URL
    print(f"Input URL: {url}")

    # Process the URL to extract features using the fitted vectorizer
    features = vectorizer.transform([url])

    # Log the feature vector
    print(f"Feature Vector: {features.toarray()}")

    # Predict using the loaded model
    prediction = loaded_model.predict(features)
    
    # Log the prediction
    print(f"Prediction: {prediction}")

    # Correctly determine the result based on the prediction
    result = "Phishing" if prediction[0].lower() == 'phishing' else "Legitimate"

    # Log the result
    print(f"Result to be rendered: {result}")

    # Pass the result to the template
    return render_template('result.html', prediction=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
