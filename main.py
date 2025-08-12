import mysql.connector

db = mysql.connector.connect(
    host="localhost",      
    user="root",       
    password="password"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS weather_app")
print("✅ Database 'weather_app' created or already exists.")
cursor.execute("USE weather_app")

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_input VARCHAR(100),
    location_name VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT,
    temperature FLOAT,
    feels_like FLOAT,
    humidity INT,
    wind_speed FLOAT,
    description VARCHAR(100),
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    """)
print("✅ Table 'weather_data' created or already exists.")

db.close()

