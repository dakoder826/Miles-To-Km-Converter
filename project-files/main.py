from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=500)
window.config(padx=160, pady=20)

is_equal_to = Label(text="is equal to", font=("Times New Roman", 10))
is_equal_to.grid(column=0, row=1)

mile_entry = Entry(width=10)
mile_entry.grid(column=1, row=0)

km_output = Label(text="0", font=("Times New Roman", 10))
km_output.grid(column=1, row=1)


def calculate():
    final_answer = round(int(mile_entry.get()) * 1.609344)
    km_output.config(text=final_answer)


calculate_button = Button(text="Calculate", command=calculate, font=("Times New Roman", 10))
calculate_button.grid(column=1, row=2)

mile_label = Label(text="Miles", font=("Times New Roman", 10))
mile_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Times New Roman", 10))
km_label.grid(column=2, row=1)
window.mainloop()
