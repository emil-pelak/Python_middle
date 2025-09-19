import tkinter as tk
from tkinter.colorchooser import askcolor


def start_drawing(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y


def draw(event):
    global prev_x, prev_y, brush_color
    canvas.create_line(prev_x, prev_y, event.x, event.y, fill=brush_color,
                       width=2)
    prev_x, prev_y = event.x, event.y


def clear_canvas():
    canvas.delete("all")


def choose_color():
    global brush_color
    color = askcolor(title="Choose Color")
    if color[1]:
        brush_color = color[1]


# Create the main window
window = tk.Tk()
window.title("Simple Painting App")

# Create a Canvas widget
canvas = tk.Canvas(window, bg="white", width=400, height=400)
canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Binding mouse events to drawing functions
canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)

# Set default brush color to black
brush_color = "black"

# Create a Clear button
clear_button = tk.Button(window, text="Clear", command=clear_canvas)
clear_button.pack(padx=10, pady=10)

# Create a Color button
choose_color_button = tk.Button(window, text="Choose Color",
                                command=choose_color)
choose_color_button.pack(padx=10, pady=10)

# Start the main loop
window.mainloop()
