
import tkinter as tk
from tkinter import ttk

# Create the main application window
app = tk.Tk()
app.title("Equation Plotter")

# GUI layout
frame = ttk.Frame(app, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Equation label and entry box
ttk.Label(frame, text="Enter Equation:").grid(row=0, column=0, sticky=tk.W, pady=5)
equation_entry = ttk.Entry(frame, width=40)
equation_entry.grid(row=0, column=1, padx=5, pady=5)

# Placeholder for button functionality
def placeholder_function():
    print("Button clicked!")

# Plot button
plot_button = ttk.Button(frame, text="Plot", command=placeholder_function)
plot_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
app.mainloop()