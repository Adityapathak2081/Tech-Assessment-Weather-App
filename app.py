import requests
import mysql.connector
from datetime import datetime

# ====== CONFIG ======
API_KEY = "474910e127be904d06254ebb9480ffe5"  # Replace with your OpenWeather API key
BASE_URL = "https://api.openweathermap.org/data/2.5/"
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",  # Replace with your MySQL root password
    "database": "weather_app"
}

# ====== CONNECT TO MYSQL ======
db = mysql.connector.connect(**DB_CONFIG)
cursor = db.cursor()
# ====== CREATE TABLE IF NOT EXISTS ======
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(100),
    date_time DATETIME,
    temperature FLOAT,
    weather_desc VARCHAR(255),
    forecast JSON
)
""")

# ====== FUNCTION: Get weather ======
def get_weather(location):
    # Current weather
    current_url = f"{BASE_URL}weather?q={location}&appid={API_KEY}&units=metric"
    current_res = requests.get(current_url).json()

    if current_res.get("cod") != 200:
        print(f"❌ Error: {current_res.get('message')}")
        return None

    temp = current_res["main"]["temp"]
    weather_desc = current_res["weather"][0]["description"]

    # 5-day forecast
    forecast_url = f"{BASE_URL}forecast?q={location}&appid={API_KEY}&units=metric"
    forecast_res = requests.get(forecast_url).json()

    return {
        "location": location,
        "temperature": temp,
        "description": weather_desc,
        "forecast": forecast_res
    }

# ====== MAIN PROGRAM ======
location = input("Enter location (City or Zip): ")
data = get_weather(location)

if data:
    # Display results
    print(f"\n📍 Location: {data['location']}")
    print(f"🌡️ Temperature: {data['temperature']}°C")
    print(f"🌤️ Condition: {data['description']}")
    print("\n📅 5-Day Forecast (3-hour intervals):")
    for item in data["forecast"]["list"][:10]:  # show first 10 entries (~1.25 days)
        dt = datetime.fromtimestamp(item["dt"]).strftime("%Y-%m-%d %H:%M")
        temp = item["main"]["temp"]
        desc = item["weather"][0]["description"]
        print(f"{dt} | {temp}°C | {desc}")

    # Save to MySQL
    cursor.execute("""
        INSERT INTO weather_data (location, date_time, temperature, weather_desc, forecast)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        data["location"],
        datetime.now(),
        data["temperature"],
        data["description"],
        str(data["forecast"])  # store JSON as string
    ))
    db.commit()

    print("\n✅ Data saved to MySQL successfully.")

# ====== CLOSE ======
cursor.close()
db.close()