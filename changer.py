from tkinter import *
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
    if ".?!" not in text:
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
    temp_list = text.split(" ")
    new_list = []
    for i in temp_list:
        if "\n" in i:
            start = i.find("\n")
            end = i.rfind("\n")
            new_list.append(i[0: start].capitalize() +
                            i[start: end+1] + i[end + 1:].capitalize())
        else:
            new_list.append(i.capitalize())
    text = " ".join(new_list)
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


def format():
    deselect(format_text_value)
    text = input_text.get(1.0, "end-1c")
    input_text.delete('1.0', END)
    temp_list = text.split(" ")
    # making a slice of list to delete additional empty spaces
    for i in temp_list[:]:
        if len(i) == 0:
            temp_list.remove(i)            
    text = " ".join(temp_list)
    input_text.insert(1.0, text)


window = Tk()
window.title("Text Changer")
window.geometry("1200x720")

input_text = Text()
input_text.place(x=5, y=5, height=710, width=800)

# BUTTONS

# All text UPPERCASE
upper_text_value = BooleanVar(value=False)
upper_text = Checkbutton(
    text="Upper", variable=upper_text_value, command=upper)
upper_text.place(x=810, y=5)

# All text lowercase
lower_text_value = BooleanVar(value=False)
lower_text = Checkbutton(
    text="Lower", variable=lower_text_value, command=lower)
lower_text.place(x=900, y=5)

# First string Capitalize
capitalize_text_value = BooleanVar(value=False)
capitalize_text = Checkbutton(
    text="Capitalize", variable=capitalize_text_value, command=capitalize)
capitalize_text.place(x=1000, y=5)

# All strings Capitalize
capitalize_all_text_value = BooleanVar(value=False)
capitalize_all_text = Checkbutton(
    text="Capitalize All", variable=capitalize_all_text_value, command=capitalize_all)
capitalize_all_text.place(x=1100, y=5)

# All text copied to clipboard
show_text = Button(text="Copy text to clipboard", command=copy_to_clipboard)
show_text.place(x=810, y=690)

# REPLACE
find_label = Label(text="Replace All").place(x=807, y=35)
find_input = Entry()
find_input.place(x=810, y=60)

replace_label = Label(text="with").place(x=807, y=85)
replace_input = Entry()
replace_input.place(x=810, y=110)

replace_button = Button(text="Replace", command=replace).place(x=810, y=150)

format_text_value = BooleanVar(value=False)
format_text = Checkbutton(
    text="Format text", variable=format_text_value, command=format).place(x=1000, y=50)
window.mainloop()
