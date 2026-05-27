import pandas as pd

# Read CSV file
data = pd.read_csv("CSV file/Esp8266-BMP180.csv")

# Show first 5 rows
print(data.head())

# Show column names
print(data.columns)

# Show information about dataset
print(data.info())