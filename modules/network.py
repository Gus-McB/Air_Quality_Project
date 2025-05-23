from keras.api.models import Sequential
from keras.api.layers import Dense
from keras.api.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

def buildRegressor(X, y):
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build the model
    model = Sequential([
        Dense(16, activation='relu', input_shape=(X.shape[1],)),
        Dense(8, activation='relu'),
        Dense(1, activation='linear')  # Single output for regression
    ])

    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

    # Early stopping
    early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

    # Train model
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2,
              callbacks=[early_stop], verbose=1)

    # Evaluate
    loss, mae = model.evaluate(X_test, y_test, verbose=1)
    print(f"Test MAE: {mae:.2f}")

    return model
