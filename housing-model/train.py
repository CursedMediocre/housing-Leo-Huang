import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import pandas as pd

# Enable MLflow autologging
mlflow.sklearn.autolog()

# Load dataset
data = pd.read_csv("data/housing.csv")  # Ensure your dataset is correctly placed
X = data.drop(columns=["median_house_value"])  # Features
y = data["median_house_value"]  # Target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Start MLflow experiment
with mlflow.start_run():
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict & evaluate
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    # Log metric manually (optional, since autologging does it)
    mlflow.log_metric("mae", mae)

    # Save and log model
    mlflow.sklearn.log_model(model, "model")

print("Training complete. Check MLflow for details.")
