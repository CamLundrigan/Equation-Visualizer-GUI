import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, lambdify

# Function to handle button press
def plot_equation():
    equation = equation_entry.get()  # Get the equation from the entry box
    try:
        # Parse and validate the equation
        parsed_eq = sympify(equation)
        func = lambdify(('x', 'y'), parsed_eq, modules=['numpy'])

        # Generate x, y values
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x, y)
        Z = func(X, Y)

        # Plotting
        fig, ax = plt.subplots(1, 2, figsize=(12, 6))
        
        # Contour Plot
        ax[0].contour(X, Y, Z, levels=20, cmap='viridis')
        ax[0].set_title("Contour Plot")
        ax[0].set_xlabel("x")
        ax[0].set_ylabel("y")
        
        # Surface Plot
        ax3d = fig.add_subplot(122, projection='3d')
        ax3d.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
        ax3d.set_title("Surface Plot")
        ax3d.set_xlabel("x")
        ax3d.set_ylabel("y")
        ax3d.set_zlabel("z")
        
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Invalid equation: {e}")

# GUI Setup
app = tk.Tk()
app.title("Equation Plotter")

frame = ttk.Frame(app, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Add input field for equation
ttk.Label(frame, text="Enter Equation (e.g., x**2 + y**2):").grid(row=0, column=0, sticky=tk.W)
equation_entry = ttk.Entry(frame, width=40)
equation_entry.grid(row=0, column=1, padx=5, pady=5)

# Add a button to trigger the plotting
plot_button = ttk.Button(frame, text="Plot", command=plot_equation)
plot_button.grid(row=1, column=0, columnspan=2, pady=10)

app.mainloop()
