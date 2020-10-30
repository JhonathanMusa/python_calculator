from tkinter import Tk, Label, DoubleVar, Entry, Button, Text

# Window properties
window = Tk()
window.config(background="#BFB999")
window.title("Calculator App")
window.geometry("400x300")
window.resizable(width=False, height=False)

# operation functions


def add_operation():
    value1 = float(value1_input.get())
    value2 = float(value2_input.get())
    result = value1 + value2
    result_value.set(int(result))


def less_operator():
    value1 = float(value1_input.get())
    value2 = float(value2_input.get())
    result = value1 - value2
    result_value.set(int(result))


def clear():
    value1_input.set("")
    value2_input.set("")
    result_value.set("")


def multiply():
    value1 = float(value1_input.get())
    value2 = float(value2_input.get())
    result = value1 * value2
    result_value.set(int(result))

def divide():
    value1 = float(value1_input.get())
    value2 = float(value2_input.get())
    result = value1 / value2
    result_value.set(int(result))


# labels properties


# input number 1 entry
value1_input = DoubleVar()
value_entry = Entry(window, textvariable=value1_input, width=20)
value_entry.grid(column=0, row=0, padx=15, pady=15, ipady=5)
value_entry.delete(0, 'end')

# input number 2 entry
value2_input = DoubleVar()
value2_entry = Entry(window, textvariable=value2_input, width=20)
value2_entry.grid(column=1, row=0, padx=15, pady=15, ipady=5)
value2_entry.delete(0, 'end')

# result
result_value = DoubleVar()
result_entry = Entry(window, textvariable=result_value, width=30)
result_entry.grid(column=0, row=1, padx=15, pady=15, ipady=5)
result_entry.delete(0, 'end')

# buttons 
btn_add = Button(window, text="+", width=10, bg="#A65A49", fg="white", command=add_operation)
btn_add.grid(column=0, row=3, padx=15, pady=15,)

btn_less = Button(window, text="-", width=10,  bg="#A65A49", fg="white", command=less_operator)
btn_less.grid(column=1, row=3, padx=15, pady=15)

btn_mult = Button(window, text="*", width=10,  bg="#A65A49", fg="white", command=multiply)
btn_mult.grid(column=0, row=4, padx=15, pady=15)

btn_div = Button(window, text="/", width=10,  bg="#A65A49", fg="white", command=divide)
btn_div.grid(column=1, row=4, padx=15, pady=15)

btn_clear = Button(window, text="C", width=10,  bg="#A65A49", fg="white", command=clear)
btn_clear.grid(column=1, row=1, padx=15, pady=15)




window.mainloop()
