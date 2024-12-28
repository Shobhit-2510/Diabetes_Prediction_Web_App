# Diabetes Prediction Web Application

This repository contains the code for a web application that predicts the likelihood of diabetes based on user input. The model uses machine learning to provide a probabilistic estimate of diabetes risk. The web app is built using **Streamlit**, making it interactive and user-friendly.

## Features

- **User-Friendly Interface**: Easy-to-use input fields for patient details.
- **Machine Learning Model**: Predicts the likelihood of diabetes based on input parameters.
- **Interactive Visualization**: Displays results dynamically.
- **Deployment**: Hosted online using Streamlit's cloud platform.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Dataset](#dataset)
5. [Model](#model)
6. [Deployment](#deployment)
7. [Contributing](#contributing)
8. [License](#license)

## Overview

This application predicts diabetes using a machine learning model trained on patient data such as age, BMI, blood pressure, and glucose levels. The app allows users to input health parameters, and it provides a prediction along with confidence scores.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Shobhit-2510/diabetes-prediction-webapp.git
   cd diabetes-prediction-webapp
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the application locally or visit the hosted URL: [Diabetes Prediction Web App](https://diabetespredictionwebapp-tg4kxyj5sy7fck3jaexbpg.streamlit.app/).
2. Enter the required health parameters in the input fields.
3. Click the "Predict" button to view the results.

## Dataset

The model is trained on a publicly available diabetes dataset, such as the [PIMA Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database). This dataset includes features like:

- Number of pregnancies
- Glucose concentration
- Blood pressure
- Skin thickness
- Insulin levels
- BMI
- Diabetes pedigree function
- Age

## Model

The predictive model is built using:

- **Algorithm**: Support Vector Machine Classifier
- **Libraries**: Scikit-learn, Pandas, NumPy

Steps involved:

1. Data Preprocessing: Cleaning, normalization, and handling missing values.
2. Model Training: Training on 80% of the dataset with cross-validation.
3. Model Evaluation: Evaluated using metrics like accuracy, precision, recall, and F1-score.
4. Deployment: Saved the trained model using `pickle` for integration with the app.

## Deployment

The app is deployed using Streamlit's cloud platform. To redeploy:

1. Push your code to a GitHub repository.
2. Link the repository to Streamlit Cloud.
3. Streamlit will handle the deployment and hosting automatically.

## Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to explore, use, and contribute to this project!
