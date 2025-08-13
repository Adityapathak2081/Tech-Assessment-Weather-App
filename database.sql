mysql> CREATE DATABASE weather_app;
ERROR 1007 (HY000): Can't create database 'weather_app'; database exists

mysql> USE weather_app;
Database changed
mysql> DROP TABLE IF EXISTS weather_data;
Query OK, 0 rows affected (0.05 sec)

mysql> CREATE TABLE weather_data (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     location VARCHAR(100),
    ->     date_time DATETIME,
    ->     temperature FLOAT,
    ->     weather_desc VARCHAR(255),
    ->     forecast TEXT
    -> );
Query OK, 0 rows affected (0.06 sec)

mysql> CREATE DATABASE weather_db;
Query OK, 1 row affected (0.01 sec)

mysql> USE weather_db;
Database changed

mysql> CREATE TABLE weather_data (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     location VARCHAR(100),
    ->     date_time DATETIME,
    ->     temperature FLOAT,
    ->     weather_desc VARCHAR(255),
    ->     forecast TEXT
    -> );
Query OK, 0 rows affected (0.06 sec)

mysql> SHOW TABLES;
+----------------------+
| Tables_in_weather_db |
+----------------------+
| weather_data         |
+----------------------+
1 row in set (0.01 sec)
