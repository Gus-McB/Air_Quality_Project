from keras.api.models import Model
from keras.api.layers import Input, Dense
from sklearn.cluster import DBSCAN

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
    dbscan = DBSCAN(eps=0.3, min_samples=5)
    return dbscan.fit_predict(encodedX)