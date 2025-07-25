## Unit Converter Application

This is a simple yet powerful Unit Converter application built with Python. It features a graphical user interface (GUI) developed using **Tkinter** and logs all conversion activities to a **MySQL(Command Line Prompt)** database for historical tracking.

---

## Features
- Temperature Conversion: Convert between Celsius and Fahrenheit.
- Length Conversion: Convert between Meters and Feet.
- Intuitive GUI: Easy-to-use graphical interface powered by Tkinter.
- Database Logging: All conversions are recorded in a MySQL database, storing the conversion type, original value, converted value, units, and a timestamp.

---

## Setup and Installation
- Install Python Extensions on Vs code 
- pip install tkinter
- pip install mysql-connector-python
- Create the Database named ecommerce_db 

---

## SCREENSHOT
- `Preview of unit converter.png`

---

## Technologies Used
- Python 
- Tkinter (for GUI)
- MySql Command Line Prompt (for MySQL database interaction)
  
---

## SQL
CREATE DATABASE ecommerce_db;
USE ecommerce_db;

## CREATE TABLE
CREATE TABLE conversions (
 - id INT AUTO_INCREMENT PRIMARY KEY,
 - conversion_type VARCHAR(50),
 - original_value FLOAT,
 - converted_value FLOAT,
 - original_unit VARCHAR(20),
 - converted_unit VARCHAR(20),
);

--- 

# Database Configuration 
DB_CONFIG = {
  - 'host': 'localhost',
  - 'user': 'root',  # e.g., 'root' or a dedicated user
  -  'password': 'Akshat9091', # e.g., 'password' or your actual password
  -  'database': 'unit_converter_db'
}

---

## Installation
Clone the Repository:
```sh
git clone https://github.com/AkshatKardak/Unit-Converter-Python.git
cd Unit-Converter-Python
```
---

## Contributors
Akshat Kardak - GitHub Profile **"https://github.com/AkshatKardak"**
