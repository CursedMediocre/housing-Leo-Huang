import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Configuration de Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    "DATABASE_URL", "postgresql://postgres:password@localhost/housing"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de la base de données
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modèle House
class House(db.Model):
    __tablename__ = 'houses'
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    housing_median_age = db.Column(db.Integer, nullable=False)
    total_rooms = db.Column(db.Integer, nullable=False)
    total_bedrooms = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    households = db.Column(db.Integer, nullable=False)
    median_income = db.Column(db.Float, nullable=False)
    median_house_value = db.Column(db.Float, nullable=False)
    ocean_proximity = db.Column(db.String(50), nullable=False)

# Route GET /houses
@app.route('/houses', methods=['GET'])
def get_houses():
    houses = House.query.all()
    result = [
        {
            "id": house.id,
            "longitude": house.longitude,
            "latitude": house.latitude,
            "housing_median_age": house.housing_median_age,
            "total_rooms": house.total_rooms,
            "total_bedrooms": house.total_bedrooms,
            "population": house.population,
            "households": house.households,
            "median_income": house.median_income,
            "median_house_value": house.median_house_value,
            "ocean_proximity": house.ocean_proximity,
        }
        for house in houses
    ]
    return jsonify(result)

# Route POST /houses
@app.route('/houses', methods=['POST'])
def add_house():
    data = request.get_json()
    new_house = House(**data)
    db.session.add(new_house)
    db.session.commit()
    return jsonify({"message": "House added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
