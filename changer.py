from tkinter import *
from tkinter import ttk
import re
from pyperclip import copy as copyToClipboard

def copy_to_clipboard():
    text = input_text.get(1.0, "end-1c")
    copyToClipboard(text)

def upper():
    text = input_text.get(1.0, "end-1c")
    input_text.delete('1.0', END)
    text = text.upper()
    input_text.insert(1.0, text)
    deselect(upper_text_value)


def lower():
    text = input_text.get(1.0, "end-1c")
    input_text.delete('1.0', END)
    text = text.lower()
    input_text.insert(1.0, text)
    deselect(lower_text_value)

def capitalize():
    text = input_text.get(1.0, "end-1c")
    input_text.delete('1.0', END)
    deselect(capitalize_text_value)

    # if a sentence doesn't have any punctuation marks
    if text[-1] not in ".!?":
        text = text.capitalize()
        input_text.insert(1.0, text)
        return

    # finding indexes of punctuation marks
    dots_list = []
    for i in re.finditer(r'[.!?]', string=text):
        dots_list.append(i.start())

    # splitting text into list items according to punctuation marks' indexes
    temp_list = []
    first = 0
    for i in dots_list:
        temp_list.append(text[first: i + 1])
        first = i + 1

    # capitalizing every first letter of the list items
    for i in range(len(temp_list)):
        letter = re.findall("[A-z]", temp_list[i])[0]
        temp_list[i] = list(temp_list[i])
        temp_list[i][temp_list[i].index(letter)] = letter.capitalize()
        temp_list[i] = "".join(temp_list[i])
    text = "".join(temp_list)

    # clearing lists
    dots_list = []
    temp_list = []
    input_text.insert(1.0, text)


def capitalize_all():
    text = input_text.get(1.0, "end-1c")
    input_text.delete('1.0', END)
    text = text.title()
    input_text.insert(1.0, text)
    deselect(capitalize_all_text_value)

# deselecting other buttons

def deselect(current):
    button_values_list = [upper_text_value, lower_text_value,
                          capitalize_text_value, capitalize_all_text_value, format_text_value]
    # removing current button value from the list to allow it to stay active
    button_values_list.remove(current)
    for i in button_values_list:
        i.set(False)


def replace():
    text = input_text.get(1.0, "end-1c")
    find = find_input.get()
    replace = replace_input.get()
    text = input_text.get(1.0, "end-1c")
    input_text.delete('1.0', END)
    changed_text = text.replace(find, replace)
    input_text.insert(1.0, changed_text)
    find_input.delete(0, END)
    replace_input.delete(0, END)

def format_text():
    deselect(format_text_value)
    text = input_text.get(1.0, "end-1c")
    input_text.delete('1.0', END)
    temp_list = text.split(" ")

    # making a slice of list to delete additional empty spaces
    empty_list = []
    for i, item in enumerate(temp_list):
        empty_list = temp_list[i].split("\n")
        for j in empty_list[:]:
            if len(j) == 0:
                empty_list.remove(j)

        temp_list[i] = "\n".join(empty_list)
        
    for i in temp_list[:]:
        if len(i) == 0:
            temp_list.remove(i)
            # print(i)
        text = " ".join(temp_list)
    input_text.insert(1.0, text)


window = Tk()
window.columnconfigure(0, weight=1)

window.rowconfigure(6, weight=1)

window.title("Text Changer")

# INPUT
input_text = Text(window)
input_text.grid(row=0, column=0, rowspan=8, padx=5, pady=5, sticky=(N, S, E, W))

# BUTTONS

# All text UPPERCASE
upper_text_value = BooleanVar(value=False)
upper_text = Checkbutton(window,
    text="Upper", variable=upper_text_value, command=upper)
upper_text.grid(row=0, column=1, sticky=(N,W), padx=2, pady=2,)

# All text lowercase
lower_text_value = BooleanVar(value=False)
lower_text = Checkbutton(window,
    text="Lower", variable=lower_text_value, command=lower)
lower_text.grid(row=0, column=2, sticky=(N,W), padx=2, pady=2)

# First string Capitalize
capitalize_text_value = BooleanVar(value=False)
capitalize_text = Checkbutton(window,
    text="Capitalize", variable=capitalize_text_value, command=capitalize)
capitalize_text.grid(row=0, column=3, sticky=(N,W), padx=2, pady=2)

# All strings Capitalize
capitalize_all_text_value = BooleanVar(value=False)
capitalize_all_text = Checkbutton(window,
    text="Capitalize All", variable=capitalize_all_text_value, command=capitalize_all)
capitalize_all_text.grid(row=1, column=1, sticky=(N,W), padx=2, pady=20)

# Format text
format_text_value = BooleanVar(value=False)
format_text_button = Checkbutton(window,
    text="Format text", variable=format_text_value, command=format_text)
format_text_button.grid(row=1, column=2, sticky=(N, W), padx=2, pady=20)

# REPLACE
find_label = Label(window, text="Replace All")
find_label.grid(row=2, column=1, columnspan=3, sticky=(S))
find_input = Entry(window, width=40)
find_input.grid(row=3, column=1, columnspan=3, sticky=(N))

replace_label = Label(window, text="with")
replace_label.grid(row=4, column=1, sticky=(S), columnspan=4)
replace_input = Entry(window, width=40)
replace_input.grid(row=5, column=1,columnspan=4, sticky=(N))

replace_button = Button(window, text="Replace", command=replace, width=20)
replace_button.grid(row=6, column=1, sticky=(N), columnspan=4, pady=20)

# All text copied to clipboard
show_text = Button(window,text="Copy text to clipboard", command=copy_to_clipboard, width=20)
show_text.grid(row=7, column=1, columnspan=4, sticky=(N), pady=5)

window.mainloop()
