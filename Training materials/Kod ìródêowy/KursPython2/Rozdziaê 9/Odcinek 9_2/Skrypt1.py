import tkinter as tk

root = tk.Tk()
root.geometry('300x300')

label = tk.Label(text="Hello!", fg='white', bg='black', width=10, height=10)
label.pack()

button = tk.Button(text="Don't click!", width=20, height=5, bg='white',
                   fg='black')
button.pack()

label_name = tk.Label(text='Name')
entry_name = tk.Entry()

label_name.pack()
entry_name.pack()

label_message = tk.Label(text='Message')
text_message = tk.Text()

label_message.pack()
text_message.pack()

root.mainloop()
