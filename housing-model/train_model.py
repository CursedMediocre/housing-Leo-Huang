import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Charger les données nettoyées
data = pd.read_csv('./data/cleaned_housing.csv')

# Préparer les variables
X = data.drop('median_house_value', axis=1)
y = data['median_house_value']

# Diviser les données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Évaluer le modèle
predictions = model.predict(X_test)
print(f'MSE: {mean_squared_error(y_test, predictions)}')

# Sauvegarder le modèle
joblib.dump(model, './model/housing_model.pkl')
