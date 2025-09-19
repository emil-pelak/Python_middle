import tkinter as tk


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height * height)
        result_label.config(text=f"Your BMI: {bmi:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid weight and height.")


# Create the main window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x250")

# Create input labels and entry fields for weight and height
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
weight_entry = tk.Entry(window)
weight_entry.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

height_label = tk.Label(window, text="Height (m):")
height_label.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
height_entry = tk.Entry(window)
height_entry.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Create a button to calculate the BMI
calculate_button = tk.Button(window, text="Calculate BMI",
                             command=calculate_bmi)
calculate_button.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a label to display the BMI result
result_label = tk.Label(window, text="")
result_label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Start the main loop
window.mainloop()
