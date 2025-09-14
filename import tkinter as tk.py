import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        
        if height <= 0 or weight <= 0:
            messagebox.showerror("Error", "Height and weight must be positive numbers.")
            return
        
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        
        label_result.config(text=f"BMI: {bmi:.2f} ({category})")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# GUI window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x200")

# Labels & Inputs
tk.Label(window, text="Enter Weight (kg):").pack(pady=5)
entry_weight = tk.Entry(window)
entry_weight.pack(pady=5)

tk.Label(window, text="Enter Height (m):").pack(pady=5)
entry_height = tk.Entry(window)
entry_height.pack(pady=5)

# Button
tk.Button(window, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

# Result
label_result = tk.Label(window, text="", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

window.mainloop()
