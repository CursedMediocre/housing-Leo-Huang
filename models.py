from app import db

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
