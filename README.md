# Air Quality Analysis and Prediction

This project analyzes and visualizes air quality data to identify regions with poor air conditions and classify the severity of air pollution using a dense neural network classifier.

## 📌 Features

- Preprocessing of raw AQI data (CO, Ozone, NO₂, PM2.5)
- Geolocation using city and country with caching
- Data normalization using `StandardScaler`
- Classification of AQI Category using a dense neural network
- Confusion matrix and performance metrics
- Interactive map output visualizing air quality by region

## 🧠 Model Overview

The model is a **dense classification neural network** built with Keras:
- Loss Function: `categorical_crossentropy`
- Optimizer: `adam`
- Evaluation: Accuracy on a held-out test set
- Uses EarlyStopping to avoid overfitting

## 🛠️ Setup

1. **Install dependencies**:

```bash
pip install -r requirements.txt
