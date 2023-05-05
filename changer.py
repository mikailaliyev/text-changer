from tkinter import *
import re
import pyperclip


def copy_to_clipboard():
    text = input_text.get(1.0, "end-1c")
    pyperclip.copy(text)


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
    print(temp_list)
    new_list = []
    for i in temp_list:
        if "\n" in i:
            start = i.find("\n")
            end = i.rfind("\n")
            new_list.append(i[0: start].capitalize() +
                            i[start: end+1] + i[end + 1:].capitalize())
        else:
            new_list.append(i.capitalize())
    print(new_list)
    text = " ".join(new_list)
    input_text.insert(1.0, text)
    deselect(capitalize_all_text_value)

# deselecting other buttons


def deselect(current):
    button_values_list = [upper_text_value, lower_text_value,
                          capitalize_text_value, capitalize_all_text_value]
    # removing current button value from the list to allow it to stay active
    button_values_list.remove(current)
    for i in button_values_list:
        i.set(False)


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

# All text copied
show_text = Button(text="Copy text", command=copy_to_clipboard)
show_text.place(x=810, y=690)
window.mainloop()
