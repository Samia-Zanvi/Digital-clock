from tkinter import *
from time import strftime

def time():
        # Fetch time in "Hour:Minute:Second AM/PM" format
    current_time = strftime("%H:%M:%S %p")
    # Fetch date in "Day-Month-Year" format
    current_date = strftime("%d-%m-%Y")
    # Combine time and date into a single string
    label.config(text=f"{current_time}\n{current_date}")
    label.after(1000, time)  # Call this function again after 1 second

root = Tk()
root.geometry("450x200")
root.title("Digital Clock")

label = Label(root, font=("Arial", 50, 'bold'), background="pink", foreground="white")
label.pack(anchor="center")

time()  # Initialize the clock

root.mainloop()
