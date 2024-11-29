# Phishing URL Detection Web Application

## Overview

A web-based application that uses machine learning to detect and assess suspicious and phishing URLs. Leverages advanced algorithms to enhance online security by identifying potential threats.

## Features

- URL phishing detection
- Comprehensive threat assessment
- Machine learning-powered analysis
- Web interface for easy URL checking

## Tech Stack

- **Backend**: Python, Flask
- **Data Processing**: Pandas
- **Machine Learning**: Scikit-learn
- **Web Framework**: Flask

## Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/phishing-url-detector.git
   cd phishing-url-detector
   ```

2. Create virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask server
   ```bash
   python app.py
   ```

2. Open browser and navigate to `http://localhost:5000`

## Project Structure

```
phishing-url-detector/
├── app.py            # Main Flask application
├── model.py          # Machine learning model
├── data/             # Dataset directory
├── templates/        # HTML templates
├── static/           # CSS, JS files
└── requirements.txt  # Project dependencies
```

## Machine Learning Model

- Uses supervised learning algorithms
- Trained on comprehensive phishing URL dataset
- Features include:
  - URL length
  - Domain age
  - HTTPS status
  - Suspicious keywords

## Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push and create pull request

## License

MIT License

## Contact
```
Email: nitiny1524@gmail.com

```

