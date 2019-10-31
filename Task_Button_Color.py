#import tkinter as tk
from tkinter import *


#colors_name = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
colors = ['#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#007dff', '#0000ff', '#7d00ff']
colors_2={'#ff0000':"красный", '#ff7d00':"оранжевый", '#ffff00':"желтый", '#00ff00':"зелёный", '#007dff':"голубой", '#0000ff':"синий", '#7d00ff':"фиолетовый"}

class Color_Button:
    """ в этом классе делаю обработчик который принимает цвет и согласно этого цвета отрисовывается """

    def __init__(self, master, color):
        self.color = color
        self.button_v = Button(master, width=20, height=2, bg=color, command=self.push_button)
        self.button_v.pack()
    def push_button(self):
        entry_v.delete(0, END)
        entry_v.insert(0, self.color)
        label_v['text'] = colors_2[self.color]
        return self.color

root = Tk()

label_v = Label(width=20, height=2, text='')
label_v.pack()

entry_v = Entry(width=25, justify='center')
entry_v.pack()

for color in colors:
    Color_Button(root, color)

root.mainloop()