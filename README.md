# 🌬️ Air Quality Analysis and Prediction

This project analyzes and visualizes air quality data across global locations. It predicts AQI values using a neural network **regressor**, evaluates model performance with interactive charts, and maps both actual and predicted air quality using **interactive Folium maps**.

---

## 🚀 Key Features

✅ Preprocesses AQI data with outlier handling and scaling  
✅ Trains a **dense regression neural network** to predict AQI  
✅ Evaluates predictions using:
- R², MAE, MSE
- Actual vs. Predicted scatter plot
- Residual histogram

✅ Visualizes actual vs. predicted AQI on interactive **folium maps**  
✅ Saves output maps as HTML for easy sharing  

---

## 🧠 Model Summary

| Layer         | Units | Activation |
|---------------|-------|------------|
| Dense (Input) | 16    | ReLU       |
| Dense         | 8     | ReLU       |
| Dense (Output)| 1     | Linear     |

- **Loss**: Mean Squared Error  
- **Optimizer**: Adam  
- **EarlyStopping**: Patience = 5 (monitors val_loss)  
- **Evaluation**: R² score, MAE, MSE  

---

## 🔍 Workflow Overview

1. **Load** and cache geolocation data (`city`, `country`)
2. **Preprocess** data: drop NA, normalise pollutant AQI values
3. **Train** a neural network on AQI prediction (regression)
4. **Evaluate** predictions with plots and regression metrics
5. **Plot** results:
   - Actual AQI on a map
   - Predicted AQI on a map
   - Confusion matrix (if classification is used)

---

## 📊 Visual Output

### 📌 Performance Charts:
- **Actual vs. Predicted Scatter Plot**
- **Residual Histogram**
- **R², MAE, MSE** (printed)

### 🗺️ Interactive Folium Maps:
- `actual_aqi_map.html`
- `predicted_aqi_map.html`

Each map uses colored markers based on AQI category, with a built-in legend:

| AQI Category      | Color     |
|------------------|-----------|
| Good             | Green     |
| Moderate         | Yellow    |
| Unhealthy (Sensitive) | Orange |
| Unhealthy        | Red       |
| Very Unhealthy   | Purple    |
| Hazardous        | Maroon    |

---

## ⚙️ Setup Instructions

1. **Clone this repo**

```bash
git clone https://github.com/Gus-McB/Air_Quality_Project.git
cd Air_Quality_Project
