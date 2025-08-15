from flask import Flask, render_template, request
import requests
import mysql.connector
from datetime import datetime

# ====== FLASK APP ======
app = Flask(__name__)

# ====== CUSTOM JINJA FILTER ======
@app.template_filter('datetimeformat')
def datetimeformat(value):
    """Convert a Unix timestamp to YYYY-MM-DD HH:MM format."""
    return datetime.fromtimestamp(value).strftime("%Y-%m-%d %H:%M")

# ====== CONFIG ======
API_KEY = "474910e127be904d06254ebb9480ffe5"  # Replace with your OpenWeather API key
BASE_URL = "https://api.openweathermap.org/data/2.5/"
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",  # Replace with your MySQL root password
    "database": "weather_app"
}

APP_AUTHOR = "Aditya Pathak"
PM_ACCELERATOR_DESCRIPTION = """
The Product Manager Accelerator Program is designed to support PM professionals through every stage of their careers.
From students looking for entry-level jobs to Directors seeking leadership roles, our program empowers PMs at all levels.
Learn more at: <a href="https://www.linkedin.com/company/product-manager-accelerator" target="_blank">Visit LinkedIn</a>
"""

# ====== CONNECT TO MYSQL ======
db = mysql.connector.connect(**DB_CONFIG)
cursor = db.cursor()

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

def get_weather(location):
    current_url = f"{BASE_URL}weather?q={location}&appid={API_KEY}&units=metric"
    current_res = requests.get(current_url).json()

    if current_res.get("cod") != 200:
        return None

    temp = current_res["main"]["temp"]
    weather_desc = current_res["weather"][0]["description"]

    forecast_url = f"{BASE_URL}forecast?q={location}&appid={API_KEY}&units=metric"
    forecast_res = requests.get(forecast_url).json()

    return {
        "location": location,
        "temperature": temp,
        "description": weather_desc,
        "forecast": forecast_res
    }

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error_msg = None

    if request.method == "POST":
        location = request.form.get("location")
        if location:
            weather_data = get_weather(location)
            if weather_data:
                cursor.execute("""
                    INSERT INTO weather_data (location, date_time, temperature, weather_desc, forecast)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    weather_data["location"],
                    datetime.now(),
                    weather_data["temperature"],
                    weather_data["description"],
                    str(weather_data["forecast"])
                ))
                db.commit()
            else:
                error_msg = "Location not found. Please try again."

    return render_template("index.html",
                           author=APP_AUTHOR,
                           description=PM_ACCELERATOR_DESCRIPTION,
                           weather=weather_data,
                           error=error_msg)

if __name__ == "__main__":
    app.run(debug=True)
