import tkinter
from tkinter import *
import webbrowser

#Opening GitHub
def open_github(event):
    webbrowser.open_new("https://github.com/rutaaaaab")

#Creating the GUI vvv

root = Tk()
root.title("Shohoj Calculator")
root.geometry("570x690")
root.resizable(False,False)
root.configure(bg="#000000")

# Defaults vvv

equation_for_show = ""
equation_for_code = ""
result_displayed = False

# Showing inputs in display vvv

def show(value):
    global equation_for_show,equation_for_code, result_displayed
    if result_displayed:
        equation_for_code = ""
        equation_for_show = ""
        result_displayed = False
    if value == "%":
        equation_for_code += "/100"
        equation_for_show += "%"
    elif value == "x":
        equation_for_code += "*"
        equation_for_show += "x"
    else:
        equation_for_code += value
        equation_for_show += value
    label_result.config(text = equation_for_show)

# Clearing Display vvv

def clear():
    global equation_for_show, equation_for_code, result_displayed
    equation_for_code = ""
    equation_for_show = ""
    result_displayed = False
    label_result.config(text = "")

# Undoing last input vvv

def undo():
    global equation_for_show, equation_for_code
    equation_for_code = equation_for_code[:-1]
    equation_for_show = equation_for_show[:-1]
    label_result.config(text = equation_for_show)

# Calculate vvv

def execute():
    global equation_for_show, equation_for_code, result_displayed
    result = ""
    if equation_for_code != "":
        try:
            result = eval(equation_for_code)
            result_displayed = True
        except:
            result = "ERROR"
            equation_for_code = ""
            equation_for_show = ""
    label_result.config(text = result)

# Keyboard bindings

def key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/().":
        show(key)
    elif key == "x" or key == "*":
        show("x")
    elif key == "=" or key == "\r":
        execute()
    elif key == "\x08":
        undo()

# Special key handling

def key_special(event):
    if event.keysym == "Return":
        execute()
    elif event.keysym == "BackSpace":
        undo()
    elif event.keysym == "Escape":
        clear()

# Bind keys to functions

root.bind("<Key>", key_press)
root.bind("<Return>", key_special)
root.bind("<BackSpace>", key_special)
root.bind("<Escape>", key_special)


# Displaybox vvv

label_result=Label(root, width = 25, height = 2, text = "", font = ("Arial", 30), bg = "#2f2f2f", fg = "#ffffff", anchor = "e")
label_result.pack()

# Buttons vvv

# First Row vvv

Button(root, text = "AC", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#1355db", relief = FLAT, command = lambda: clear()).place(x = 10, y = 108)
Button(root, text = "C", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#1355db", relief = FLAT, command = lambda: undo()).place(x = 150, y = 108)
Button(root, text = "%", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#838383", relief = FLAT, command = lambda: show("%")).place(x = 290, y = 108)
Button(root, text = "/", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#838383", relief = FLAT, command = lambda: show("/")).place(x = 430, y = 108)

# Second Row vvv

Button(root, text = "(", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#838383", relief = FLAT, command = lambda: show("(")).place(x = 10, y = 200)
Button(root, text = ")", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#838383", relief = FLAT, command = lambda: show(")")).place(x = 150, y = 200)
Button(root, text = "x", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#838383", relief = FLAT, command = lambda: show("x")).place(x = 290, y = 200)
Button(root, text = "-", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#838383", relief = FLAT, command = lambda: show("-")).place(x = 430, y = 200)

# Third Row vvv

Button(root, text = "7", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36", relief = FLAT, command = lambda: show("7")).place(x = 10, y = 292)
Button(root, text = "8", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36", relief = FLAT, command = lambda: show("8")).place(x = 150, y = 292)
Button(root, text = "9", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36", relief = FLAT, command = lambda: show("9")).place(x = 290, y = 292)
Button(root, text = "+", width = 5, height = 3, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#838383", relief = FLAT, command = lambda: show("+")).place(x = 430, y = 292)

# Fourth Row vvv

Button(root, text = "4", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36", relief = FLAT, command = lambda: show("4")).place(x = 10, y = 384)
Button(root, text = "5", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36", relief = FLAT, command = lambda: show("5")).place(x = 150, y = 384)
Button(root, text = "6", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36", relief = FLAT, command = lambda: show("6")).place(x = 290, y = 384)

# Fifth Row vvv

Button(root, text = "1", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36", relief = FLAT, command = lambda: show("1")).place(x = 10, y = 476)
Button(root, text = "2", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36", relief = FLAT, command = lambda: show("2")).place(x = 150, y = 476)
Button(root, text = "3", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36", relief = FLAT, command = lambda: show("3")).place(x = 290, y = 476)
Button(root, text = "=", width = 5, height = 3, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#c67100", relief = FLAT, command = lambda: execute()).place(x = 430, y = 476)

# Sixth Row vvv

Button(root, text = "00", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36", relief = FLAT, command = lambda: show("00")).place(x = 10, y = 568)
Button(root, text = "0", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36", relief = FLAT, command = lambda: show("0")).place(x = 150, y = 568)
Button(root, text = ".", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36", relief = FLAT, command = lambda: show(".")).place(x = 290, y = 568)

#Footer

footer = Label(root, text="< Created by Mushfique Tajwar >", font = ("Arial", 12), fg="white", cursor = "hand2", bg="#000000")
footer.pack(side="bottom", pady=10)
footer.bind("<Button-1>", open_github)

#Main Loop

root.mainloop()