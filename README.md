# 🌍 Air Quality Mapping and Clustering Project

This project analyses global air pollution data and uses **clustering algorithms** to identify and visualize areas with the best and worst air quality based on geographical location.

---

## 📌 Project Goals

- Clean and preprocess air pollution data.
- Geocode each location using `City` and `Country` to obtain coordinates.
- Use a clustering model (e.g., DBSCAN) to identify regions with similar pollution levels.
- Plot the results on an interactive map to visualize air quality hotspots and safe zones.

---

## 📁 Dataset

- **Source**: [Global Air Pollution Dataset on Kaggle](https://www.kaggle.com/datasets/hasibalmuzdadid/global-air-pollution-dataset)
- **Contents**:
  - Air pollution readings: PM2.5, PM10, NO2, SO2, CO, O3, etc.
  - City, Country, and Air Quality Category (`Good`, `Poor`, `Hazardous`, etc.)

---

## 🧰 Tech Stack

- **Python 3**
- **Pandas** – Data handling
- **Geopy** – Location geocoding
- **scikit-learn** – DBSCAN clustering
- **Folium** – Interactive map visualization

---

## 📦 Installation

   ```bash
   git clone https://github.com/Gus-McB/air-quality-clustering.git
   cd air-quality-clustering
