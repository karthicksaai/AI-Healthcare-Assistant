import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Step 1: Data Preprocessing
data = pd.read_csv('synthetic_health_dataset.csv')
data_numeric = data.drop(columns=['Timestamp'])
data_numeric.fillna(method='ffill', inplace=True)

# Normalize data
scaler = MinMaxScaler()
data_normalized = scaler.fit_transform(data_numeric)

def create_sequences(data, seq_length):
    X = []
    y = []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

sequence_length = 24  # Sequence length for hourly data in a day
X, y = create_sequences(data_normalized, sequence_length)

# Split data into train and test sets
split_ratio = 0.8
split_index = int(split_ratio * len(X))
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Step 2: Define and Train LSTM Model
model = Sequential([
    LSTM(50, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Step 3: Detect Anomalies
# Predictions on test data
predictions = model.predict(X_test)

predictions_reshaped = predictions.reshape(predictions.shape[0], predictions.shape[1], 1)
mse = np.mean(np.power(X_test - predictions_reshaped, 2), axis=1)

# Threshold for anomaly detection (adjust based on MSE distribution)
threshold = 0.15
anomalies = mse > threshold

#print(anomalies.shape)
# Print timestamps with detected anomalies
# Print timestamps with detected anomalies
# Count occurrences of anomalies for each hour
anomaly_counts = {}
for i, is_anomaly in enumerate(anomalies):
    if is_anomaly.any():
        timestamp = data.iloc[sequence_length + split_index + i]['Timestamp']
        anomaly_hour = timestamp.split()[1].split(':')[0]  # Extract hour part from timestamp
        anomaly_counts[anomaly_hour] = anomaly_counts.get(anomaly_hour, 0) + 1

# Find hour(s) with the maximum count of anomalies
max_anomaly_count = max(anomaly_counts.values())
max_anomaly_hours = [hour for hour, count in anomaly_counts.items() if count == max_anomaly_count]

# Print the hour(s) with the maximum count of anomalies
print("Hour(s) with the maximum number of anomalies:", max_anomaly_hours)
