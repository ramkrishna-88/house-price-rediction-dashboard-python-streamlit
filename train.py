import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load data
data = pd.read_csv(r"D:\house prediction.csv")

# Keep required columns
data = data[['total_sqft', 'bath', 'balcony', 'size', 'price']]

# Drop missing values
data = data.dropna()

# ✅ Convert "size" → bedrooms (extract number from "2 BHK")
data['bedrooms'] = data['size'].str.extract('(\d+)')
data['bedrooms'] = pd.to_numeric(data['bedrooms'], errors='coerce')

# Convert sqft to number
def convert_sqft(x):
    try:
        return float(x)
    except:
        return None

data['total_sqft'] = data['total_sqft'].apply(convert_sqft)

# Drop invalid rows again
data = data.dropna()

# ✅ Features & target (NOW bedrooms exists)
X = data[['total_sqft', 'bedrooms', 'bath', 'balcony']]
y = data['price']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained successfully!")