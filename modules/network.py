from keras.api.models import Sequential
from keras.api.layers import Dense
from keras.api.utils import to_categorical
from keras.api.callbacks import EarlyStopping
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def buildClassifier(X, y):
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    y_categorical = to_categorical(y_encoded)

    X_train, X_test, y_train, y_test = train_test_split(X, y_categorical, test_size=0.2, random_state=42)

    model = Sequential([
        Dense(16, activation='relu', input_shape=(X.shape[1],)),
        Dense(8, activation='relu'),
        Dense(y_categorical.shape[1], activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, callbacks=[early_stop], verbose=1)

    loss, accuracy = model.evaluate(X_test, y_test, verbose=1)
    print(f"Test Accuracy: {accuracy:.2f}")

    return model, label_encoder
