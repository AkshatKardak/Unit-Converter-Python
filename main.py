import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# --- Database Configuration (UPDATE THESE WITH YOUR ACTUAL CREDENTIALS) ---
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',  
    'password': 'Akshat9091', 
    'database': 'unit_converter_db'
}

def connect_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to database: {err}")
        return None

def save_conversion_to_db(conversion_type, original_value, converted_value, original_unit, converted_unit):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            sql = """
            INSERT INTO conversions (conversion_type, original_value, converted_value, original_unit, converted_unit)
            VALUES (%s, %s, %s, %s, %s)
            """
            data = (conversion_type, original_value, converted_value, original_unit, converted_unit)
            cursor.execute(sql, data)
            conn.commit()
            print("Conversion saved to database successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error saving conversion: {err}")
        finally:
            cursor.close()
            conn.close()


class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("400x350")

        self.create_widgets()

    def create_widgets(self):
        
        self.title_label = tk.Label(self.root, text="Welcome to the Unit Converter", font=("Arial", 14, "bold"))
        self.title_label.pack(pady=10)

       
        self.conversion_type_frame = tk.LabelFrame(self.root, text="Choose Conversion Type", padx=10, pady=10)
        self.conversion_type_frame.pack(pady=10, padx=20, fill="x")

        self.conversion_choice = tk.StringVar(self.root)
        self.conversion_choice.set("1")

        self.temp_radio = tk.Radiobutton(self.conversion_type_frame, text="1. Temperature (Celsius <-> Fahrenheit)",
                                         variable=self.conversion_choice, value="1", command=self.show_conversion_options)
        self.temp_radio.pack(anchor="w")

        self.length_radio = tk.Radiobutton(self.conversion_type_frame, text="2. Length (Meters <-> Feet)",
                                          variable=self.conversion_choice, value="2", command=self.show_conversion_options)
        self.length_radio.pack(anchor="w")

        
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=10, padx=20, fill="x")

        self.value_label = tk.Label(self.root, text="Enter the value:")
        self.value_label.pack()

        self.value_entry = tk.Entry(self.root)
        self.value_entry.pack(pady=5)

        self.result_label = tk.Label(self.root, text="Result: ")
        self.result_label.pack(pady=10)

        self.convert_button = tk.Button(self.root, text="Convert", command=self.perform_conversion)
        self.convert_button.pack(pady=10)

       
        self.show_conversion_options()

    def show_conversion_options(self):
        
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        current_type = self.conversion_choice.get()

        self.sub_choice = tk.StringVar(self.root)

        if current_type == '1': 
            self.sub_choice.set("1") 
            tk.Label(self.options_frame, text="Temperature Conversion:").pack(anchor="w")
            tk.Radiobutton(self.options_frame, text="1. Celsius to Fahrenheit",
                           variable=self.sub_choice, value="1").pack(anchor="w")
            tk.Radiobutton(self.options_frame, text="2. Fahrenheit to Celsius",
                           variable=self.sub_choice, value="2").pack(anchor="w")
        elif current_type == '2': 
            self.sub_choice.set("1") 
            tk.Label(self.options_frame, text="Length Conversion:").pack(anchor="w")
            tk.Radiobutton(self.options_frame, text="1. Meters to Feet",
                           variable=self.sub_choice, value="1").pack(anchor="w")
            tk.Radiobutton(self.options_frame, text="2. Feet to Meters",
                           variable=self.sub_choice, value="2").pack(anchor="w")

    def perform_conversion(self):
        try:
            value = float(self.value_entry.get())
            current_type = self.conversion_choice.get()
            sub_choice = self.sub_choice.get()
            result = 0
            original_unit = ""
            converted_unit = ""

            if current_type == '1': 
                if sub_choice == '1': 
                    result = (value * 9/5) + 32
                    original_unit = "Celsius"
                    converted_unit = "Fahrenheit"
                    self.result_label.config(text=f"Result: {value}°C is equal to {result:.2f}°F")
                elif sub_choice == '2': 
                    result = (value - 32) * 5/9
                    original_unit = "Fahrenheit"
                    converted_unit = "Celsius"
                    self.result_label.config(text=f"Result: {value}°F is equal to {result:.2f}°C")
                else:
                    messagebox.showerror("Error", "Invalid temperature conversion choice.")
                    return
                save_conversion_to_db("Temperature", value, result, original_unit, converted_unit)

            elif current_type == '2': 
                if sub_choice == '1': 
                    result = value * 3.28084
                    original_unit = "Meters"
                    converted_unit = "Feet"
                    self.result_label.config(text=f"Result: {value} meters is equal to {result:.2f} feet")
                elif sub_choice == '2': 
                    result = value / 3.28084
                    original_unit = "Feet"
                    converted_unit = "Meters"
                    self.result_label.config(text=f"Result: {value} feet is equal to {result:.2f} meters")
                else:
                    messagebox.showerror("Error", "Invalid length conversion choice.")
                    return
                save_conversion_to_db("Length", value, result, original_unit, converted_unit)

            else:
                messagebox.showerror("Error", "Invalid conversion type choice.")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a numeric value.")
        except Exception as e:
            messagebox.showerror("An Error Occurred", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()       
