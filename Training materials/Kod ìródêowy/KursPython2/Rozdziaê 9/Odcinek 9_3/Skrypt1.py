import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(master=root, width=150, height=150, bg='black')
# frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame1.place(x=0, y=0)

frame2 = tk.Frame(master=root, width=100, height=100, bg='blue')
# frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame2.place(x=75, y=75)

frame3 = tk.Frame(master=root, width=50, height=50, bg='red')
# frame3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame3.place(x=150, y=150)

for x in range(3):

    root.columnconfigure(x, weight=1, minsize=75)
    root.rowconfigure(x, weight=1, minsize=50)

    for y in range(3):
        frame = tk.Frame(master=root, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=x, column=y)
        label = tk.Label(master=frame, text=f"Row {x}\nColumn {y}")
        label.pack()

root.mainloop()
