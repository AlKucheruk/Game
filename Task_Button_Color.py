#import tkinter as tk
from tkinter import *

colors_s = ['#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#007dff', '#0000ff', '#7d00ff']
colors_d={'#ff0000':"red", '#ff7d00':"orange", '#ffff00':"yellow", '#00ff00':"green", '#007dff':"cyan", '#0000ff':"blue", '#7d00ff':"purple"}

class Color_Button:
    """ в этом классе делаю обработчик который принимает цвет и согласно этого цвета отрисовывается """

    def __init__(self, master, color):
        self.color = color
        self.button_v = Button(master, width=5, height=1, bg=color, command=self.push_button)
        self.button_v.pack(side=LEFT)
    def push_button(self):
        entry_v.delete(0, END)
        entry_v.insert(0, self.color)
        label_v['text'] = colors_d[self.color]
        return self.color

root = Tk()
fr_top = LabelFrame(root, text='Top')
fr_bottom = LabelFrame(root, text='Bottom')

fr_top.pack()
fr_bottom.pack()

label_v = Label(fr_top, width=20, height=1, text='')
label_v.pack(side=TOP, padx=10, pady=10)

entry_v = Entry(fr_top, width=25, justify='center')
entry_v.pack(side=TOP, padx=10, pady=10)

for color in colors_s:
    Color_Button(fr_bottom, color)
    
root.mainloop()