import tkinter as tk

class Color_Button:
    """ в этом классе делаю обработчик который принимает цвет и согласно этого цвета отрисовывается """

    def __init__(self, master, color_v, color_n):
        self.button_v = tk.Button(master, width=20, height=2, bg=color_v, command=self.push_button)
        self.color = color_v
        self.color_n = color_n
        self.button_v.pack()

    def push_button(self):
        entry_v.delete(0, END)
        entry_v.insert(0, self.color)
        label_v['text'] = self.color_n
        return self.color


colors = ['#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#007dff', '#0000ff', '#7d00ff']
colors_name = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']

root = tk.Tk()

label_v = tk.Label(width=20, height=2)
label_v['text'] = 'Samfing'
label_v.pack()

entry_v = tk.Entry(width=20, justify='center')
entry_v.pack()

for color in colors:
    Color_Button(root, color, 'yellow')

root.mainloop()