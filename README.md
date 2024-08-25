# Salary Prediction Using Flask 💼💰

Welcome to the **Salary Prediction** project! This repository showcases a web-based application using Flask to predict salaries based on various input features such as experience, test scores, and interview performance. The project aims to provide a user-friendly interface for salary predictions, making it easier for HR departments and job applicants to estimate potential salaries.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Flask Web Application](#flask-web-application)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Installation](#installation)

## Project Overview

Salary prediction plays a significant role in career planning and recruitment. This project employs a machine learning model to predict salaries based on key features such as years of experience, test scores, and interview performance. The project is built using Flask to provide an interactive web interface for predictions.

## Features

- **Interactive Web Interface**: Users can input details through a form and get instant salary predictions.
- **Data Preprocessing**: The model includes handling of missing values and feature scaling.
- **Machine Learning Model**: A pre-trained model using Linear Regression to ensure accurate predictions.
- **Error Handling**: Robust error handling to manage unexpected input and processing issues.

## Dataset

The project uses a dataset containing records of job applicants and their associated salaries. The key features in the dataset include:

- `experience`: Number of years of experience.
- `test_score (out of 10)`: Performance in a standardized test.
- `interview_score (out of 10)`: Rating from the interview process.
- `salary ($)`: Actual salary (used for training and validation).

## Flask Web Application

The Flask web application serves as the frontend for the model:

- **Home Route (`/`)**: Renders the main page (`index.html`) where users can input their details.
- **Predict Route (`/predict`)**: Processes the input data, applies the machine learning model, and displays the predicted salary.

## Model Architecture

The project employs a Linear Regression model to predict salaries. The model is trained on the dataset with features like experience, test scores, and interview scores. The model is saved using pickle for quick loading and prediction during runtime.

## Results

The model achieves accurate predictions with a focus on minimizing errors:

- **Metrics**: Evaluated using Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared values.
- The model provides predictions that closely match the actual salaries in the dataset.

## Installation

To set up this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Salary-Prediction-Flask.git
   cd Salary-Prediction-Flask
