from keras.api.models import Model
from keras.api.layers import Input, Dense
from sklearn.cluster import DBSCAN


numClass = len(label.classes_) #For the AQI categories 

model = Model.Sequential([
    layers.Dense(64, activation='relu', input_shape=(x.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(numClass, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

training = model.fit(x, y, epochs=20, batch_size=32, validation_split=0.2)

loss, accuracy = model.evaluate(x, y)
print(f"Loss: {loss}, Accuracy: {accuracy}")
predict = model.predict(x)


def autoencoderModel(X, encoding_dim=2):
    inputLayer = Input(shape=(X.shape[1],))
    encoded = Dense(8, activation='relu')(inputLayer)
    encoded = Dense(encoding_dim, activation='linear')(encoded)
    decoded = Dense(8, activation='relu')(encoded)
    decoded = Dense(X.shape[1], activation='linear')(decoded)

    autoencoder = Model(inputLayer, decoded)
    encoder = Model(inputLayer, encoded)
    autoencoder.compile(optimizer='adam', loss='mse')
    autoencoder.fit(X, X, epochs=50, batch_size=32, verbose=0)

    return encoder.predict(X)

def clusterData(encodedX):
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    return dbscan.fit_predict(encodedX)