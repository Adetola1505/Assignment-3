# Program Name: Assignment2.py
# Course: IT3883/Section XXX
# Student Name: Maryam Adigun-Hammed
# Assignment Number: Lab 2
# Due Date: MM/DD/YYYY
# Purpose: Convert MPG to km/L automatically as the user types.
# Resources: Python tkinter documentation and assignment instructions.

import tkinter as tk
from tkinter import ttk

CONVERSION_FACTOR = 0.425143707

def main():
    # Create the GUI window
    window = tk.Tk()
    window.title("MPG to km/L Converter")
    window.geometry("390x200")

    frame = ttk.Frame(window, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="MPG to km/L Converter",
              font=("Arial", 14, "bold")).pack(pady=10)

    mpg_value = tk.StringVar()
    result_value = tk.StringVar(value="Enter an MPG value")

    ttk.Label(frame, text="Miles per Gallon (MPG):").pack()
    ttk.Entry(frame, textvariable=mpg_value).pack(pady=5)

    # Update conversion whenever input changes
    def convert(*args):
        try:
            mpg = float(mpg_value.get())
            if not 0 <= mpg < float("inf"):
                result_value.set("Enter a valid non-negative number")
                return
            result = mpg * CONVERSION_FACTOR
            result_value.set(f"{result:.4f} km/L")
        except ValueError:
            result_value.set("Enter a valid MPG number")

    mpg_value.trace_add("write", convert)

    ttk.Label(frame, textvariable=result_value,
              font=("Arial", 12)).pack(pady=15)

    window.mainloop()

if __name__ == "__main__":
    main()
