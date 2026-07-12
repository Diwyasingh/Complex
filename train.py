import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

# Read the CSV
df = pd.read_csv("Fire experiment-table.csv", skiprows=6)

# Inputs
X = df[["density", "wind", "[step]"]]

# Output
y = df["count turtles"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestRegressor(
    n_estimators=50,
    max_depth=10,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
print("R² Score:", r2_score(y_test, predictions))
print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))

# Save model
joblib.dump(model, "model.pkl")

print("Model saved successfully!")