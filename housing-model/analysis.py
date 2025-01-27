import pandas as pd

# Charger les données
data = pd.read_csv('./data/housing.csv')

# Aperçu
print(data.info())
print(data.describe())

# Nettoyage
data = data.dropna()  # Gérer les valeurs manquantes
data = data[data['median_house_value'] < 500000]  # Filtrer les outliers

# Sauvegarder les données nettoyées
data.to_csv('./data/cleaned_housing.csv', index=False)
