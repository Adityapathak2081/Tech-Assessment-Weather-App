# Tech-Assessment-Weather-App
This project is split into two levels. At first I've built a weather app that will take in user-input and then gather data from outside sources (API retrieval) to provide the user with relevant real-time information based on their requests. Second focuses on persistence with CRUD functionality as well as additional API calls and error handling.


LEVEL -1 :
This project has a few code components in it.

1) main.py - python code that creates the database and table before our weather app can run. Its main use is to prepare the database for the     app.
   
2) app.py - this python code fetches weather, displays it, and saves it to the database.It basically follows these steps:
     a) Takes location input from the user.
     b) Uses the OpenWeather API to fetch the Current weather and the 5-day forecast of every 3 hours.
     c) Displays the weather details on the screen.
     d) Saves the data into the MySQL database.
   This file will be used for giving input and user interation.
