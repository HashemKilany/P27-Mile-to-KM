from tkinter import *


def miles_kilos():
    miles_value = entry_box.get()
    km_value = round(float(miles_value) * 1.609344,3)
    result_label.config(text=km_value)


window = Tk()
window.minsize(width=300, height=200)
window.title('Mile to KM converter')
window.config(padx=50, pady=50)

entry_box = Entry(width=10)
entry_box.grid(column=2, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)
miles_label.config(padx=10, pady=10)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=10)

result_label = Label(text="0")
result_label.grid(column=2, row=1)
result_label.config(padx=10, pady=10)

km_label = Label(text="Km")
km_label.grid(column=3, row=1)
km_label.config(padx=10, pady=10)

calc_button = Button(text="Calculate", command=miles_kilos)
calc_button.grid(column=2, row=3)

window.mainloop()
