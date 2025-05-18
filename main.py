import pandas as pd
from modules.geocode import geocodeLocations
from modules.preprocess import preprocess
from modules.network import autoencoderModel, clusterData
from modules.mapPlot import plotClusters

# Load data
df = pd.read_csv("data\global air pollution dataset.csv")
df = geocodeLocations(df)

# Preprocess
df, X = preprocess(df)

# Autoencode and Cluster
encodedX = autoencoderModel(X)
labels = clusterData(encodedX)

# Visualise
mapped = plotClusters(df, labels)
mapped.save('air_quality_map.html')