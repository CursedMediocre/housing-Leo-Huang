Housing API Project

Features
- Retrieve and add housing data.
- Automated database migrations.
- Persistent PostgreSQL storage with Docker.

---

Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd housing-api
   ```
2. Run the services with Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. Access the API at:
   ```plaintext
   http://localhost:5000
   ```

---
Endpoints
- **GET /houses**: Retrieve all houses.
- **POST /houses**: Add a new house.

Example `POST` request:
```json
{
  "longitude": -122.23,
  "latitude": 37.88,
  "housing_median_age": 41,
  "total_rooms": 880,
  "total_bedrooms": 129,
  "population": 322,
  "households": 126,
  "median_income": 8.3252,
  "median_house_value": 452600.0,
  "ocean_proximity": "NEAR BAY"
}
```

Testing
- Test the API with **Postman** or **cURL**.
- Example:
   ```bash
   curl http://localhost:5000/houses
   ```

---
