import mysql.connector

# Step 1: Connect to MySQL (change these to your MySQL credentials)
db = mysql.connector.connect(
    host="localhost",         # usually 'localhost'
    user="root",              # your MySQL username
    password="password"  # your MySQL password
)

cursor = db.cursor()

# Step 2: Create database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS weather_app")
print("✅ Database 'weather_app' created or already exists.")

# Step 3: Use that database
cursor.execute("USE weather_app")

# Step 4: Create table if not exists
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
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
print("✅ Table 'weather_data' created or already exists.")

# Step 5: Close connection
db.close()
