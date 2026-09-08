import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Step 1: Generate training samples
def generate_data():
    x = np.linspace(-20, 20, 1000)  # Generate 1000 samples between -20 and +20
    y = 5 * x**3 - 10 * x**2 - 20 * x + 10  # Polynomial equation
    return x, y

# Step 2: Normalize the data to the range [-1, 1]
def normalize_data(x, y):
    x_scaler = MinMaxScaler(feature_range=(-1, 1))
    y_scaler = MinMaxScaler(feature_range=(-1, 1))
    
    x_normalized = x_scaler.fit_transform(x.reshape(-1, 1)).flatten()
    y_normalized = y_scaler.fit_transform(y.reshape(-1, 1)).flatten()
    
    return x_normalized, y_normalized, x_scaler, y_scaler

# Step 3: Split the data into training, validation, and test sets
def split_data(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.05, random_state=42)
    return x_train, x_val, x_test, y_train, y_val, y_test

# Step 4: Build the DNN model
def build_model():
    model = models.Sequential([
        layers.Dense(32, activation='relu', input_shape=(1,)),  # First hidden layer
        layers.Dense(64, activation='relu'),  # Second hidden layer
        layers.Dense(128, activation='relu'),  # Third hidden layer
        layers.Dense(1)  # Output layer
    ])
    return model

# Step 5: Train the model
def train_model(model, x_train, y_train, x_val, y_val):
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=[tf.keras.metrics.R2Score(name='r2')])
    history = model.fit(x_train, y_train, epochs=100, validation_data=(x_val, y_val), verbose=1)
    return history

# Step 6: Plot training and validation metrics
def plot_metrics(history):
    plt.figure(figsize=(12, 5))

    # Plot training and validation accuracy (R² score)
    plt.subplot(1, 2, 1)
    plt.plot(history.history['r2'], label='Training R²')
    plt.plot(history.history['val_r2'], label='Validation R²')
    plt.xlabel('Epochs')
    plt.ylabel('R² Score')
    plt.title('Training and Validation R² Score')
    plt.legend()

    # Plot training and validation loss
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.legend()

    plt.show()

# Main function
def main():
    # Step 1: Generate data
    x, y = generate_data()

    # Step 2: Normalize data
    x_normalized, y_normalized, x_scaler, y_scaler = normalize_data(x, y)

    # Step 3: Split data
    x_train, x_val, x_test, y_train, y_val, y_test = split_data(x_normalized, y_normalized)

    # Step 4: Build the model
    model = build_model()
    model.summary()  # Display the model architecture and number of parameters

    # Step 5: Train the model
    history = train_model(model, x_train, y_train, x_val, y_val)

    # Step 6: Plot metrics
    plot_metrics(history)

    # Step 7: Evaluate the model on test data
    test_loss, test_r2 = model.evaluate(x_test, y_test, verbose=0)
    print(f"Test Loss: {test_loss}")
    print(f"Test R² Score: {test_r2}")

if __name__ == "__main__":
    main()