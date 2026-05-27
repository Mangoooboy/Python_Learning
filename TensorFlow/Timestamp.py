import pandas as pd

# Load CSV
data = pd.read_csv("CSV file/Esp8266-BMP180.csv")

# Show original timestamp
print("Original Time Column:")
print(data['Time'].head())

# Convert string to datetime
data['Time'] = pd.to_datetime(data['Time'])

print("\nConverted Datetime:")
print(data['Time'].head())

# Extract Hour
data['Hour'] = data['Time'].dt.hour

# Extract Minute
data['Minute'] = data['Time'].dt.minute

print("\nExtracted Hour and Minute:")
print(data[['Time', 'Hour', 'Minute']].head())