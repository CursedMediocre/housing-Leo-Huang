import psycopg2

try:
    conn = psycopg2.connect(
        dbname="housing",
        user="postgres",
        password="password",  # Remplacez par votre mot de passe
        host="localhost",
        port="5432"
    )
    print("Connexion réussie à PostgreSQL !")
    conn.close()
except Exception as e:
    print(f"Erreur de connexion : {e}")
