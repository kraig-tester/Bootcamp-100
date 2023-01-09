import tkinter

# windows
window = tkinter.Tk()
window.title("First window")
window.minsize(width = 500, height=300)
window.config(padx=20, pady=20)
#labels
my_label = tkinter.Label(text="I am a label.",font=("Arial", 24, "bold"))
my_label.config(padx=20, pady=20)
# my_label.pack()
my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)

# my_label.config(text="Some new text")
my_label["text"] = "New text"


# buttons
def button_clicked():
    my_label["text"] = input.get()


button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
#button.place(x=100, y=50)
button.grid(column=1, row=1)

button_2 = tkinter.Button(text="test button")
button_2.grid(column=2, row=0)
# entry(input)
input = tkinter.Entry(width=10)
# input.pack()
# input.place(x=100, y=80)
input.grid(column=3, row=2)

# return value as string
input_value = input.get()

window.mainloop()