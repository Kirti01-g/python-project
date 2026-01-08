import tkinter as tk
from time import strftime

def update_time():
    time_string = strftime('%H:%M:%S')
    clock_label.config(text=time_string)
    clock_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.configure(bg='black')

clock_label = tk.Label(root, font=('Arial', 80, 'bold'), background='black', foreground='cyan')
clock_label.pack(expand=True)

update_time()
root.mainloop()