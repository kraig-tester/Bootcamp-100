import tkinter


# buttons
def calculate():
    result_l["text"] = f"{round(float(user_input.get()) * 1.609)}"


# windows
window = tkinter.Tk()
window.title("Miles to Km converter")
window.minsize(width = 200, height=100)
window.config(padx=20, pady=20)

miles_l = tkinter.Label(text="Miles")
miles_l.grid(column=2, row=0)

km_l = tkinter.Label(text="Km")
km_l.grid(column=2, row=1)

equal_l = tkinter.Label(text="is equal to")
equal_l.grid(column=0, row=1)

result_l = tkinter.Label(text="0")
result_l.grid(column=1, row=1)

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)

window.mainloop()