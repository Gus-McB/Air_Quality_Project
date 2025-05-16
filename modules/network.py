import tensorflow as tf
from tensorflow import keras
from keras import layers, models
import pandas as pd
from preprocess import preprocess
from geocode import geocode_locations
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('data\global air pollution dataset.csv')
print(df.columns)
df = geocode_locations(df)
df, features = preprocess(df)

tar = df['AQI Category']
label = LabelEncoder()
y = label.fit_transform(tar)
x = features.values

numClass = len(label.classes_) #For the AQI categories 

model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(x.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(numClass, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

training = model.fit(x, y, epochs=20, batch_size=32, validation_split=0.2)

loss, accuracy = model.evaluate(x, y)
print(f"Loss: {loss}, Accuracy: {accuracy}")
predict = model.predict(x)

