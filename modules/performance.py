import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import (
    mean_absolute_error, mean_squared_error, r2_score,
    confusion_matrix, classification_report, ConfusionMatrixDisplay
)

def map_aqi_to_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for SG"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

def performance(df, predictedCol, trueCol='AQI Value'):
    df = df.copy()

    y_true = df[trueCol]
    y_pred = df[predictedCol]

    # Regression metrics
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)

    print("Regression Performance:")
    print(f"MAE: {mae:.2f}")
    print(f"MSE: {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R²: {r2:.2f}")

    # Regression plots
    plt.figure(figsize=(8, 6))
    plt.scatter(y_true, y_pred, alpha=0.5, edgecolor='k')
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--')
    plt.xlabel('Actual AQI Value')
    plt.ylabel('Predicted AQI Value')
    plt.title('Predicted vs Actual AQI')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    residuals = y_true - y_pred
    plt.figure(figsize=(8, 5))
    plt.hist(residuals, bins=30, color='slateblue', edgecolor='black')
    plt.title('Residuals Distribution')
    plt.xlabel('Residual (Actual - Predicted)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    # Classification metrics from AQI categories
    df['TrueCategory'] = df[trueCol].apply(map_aqi_to_category)
    df['PredictedCategory'] = df[predictedCol].apply(map_aqi_to_category)

    labels = ['Good', 'Moderate', 'Unhealthy for SG', 'Unhealthy', 'Very Unhealthy', 'Hazardous']

    cm = confusion_matrix(df['TrueCategory'], df['PredictedCategory'], labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(cmap=plt.cm.Blues, xticks_rotation=45)
    plt.title("Confusion Matrix (Predicted AQI Category)")
    plt.tight_layout()
    plt.show()

    print("Classification Report (on categorized AQI):")
    print(classification_report(df['TrueCategory'], df['PredictedCategory'], labels=labels, zero_division=0))
