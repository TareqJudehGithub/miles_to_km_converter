from tkinter import Tk, Label, Entry, Button, Text


# Miles to Km converter:
def miles_to_km():
    miles = float(miles_entry.get())
    km = round(miles * 1.6)
    result_label.config(text=f"{km}")


# New window instance from Tk() class:
window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=30, pady=30)
# labels:
miles_label = Label(text=" Miles", font=("Arial", 10, "normal"))
miles_label.grid(column=3, row=0)

km_label = Label(text="Km", font=("Arial", 10, "normal"))
km_label.grid(column=3, row=1)

result_label = Label(text=0, font=("Arial", 10, "normal"))
result_label.grid(column=2, row=1, sticky="W")

is_equal_label = Label(text="Is equal to  ", font=("Arial", 10, "normal"))
is_equal_label.grid(column=0, row=1)

# Entries:
miles_entry = Entry(width=10)
miles_entry.focus()
miles_entry.grid(column=2, row=0)

# Buttons:
calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=2, row=2)


window.mainloop()