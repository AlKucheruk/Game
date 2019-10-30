import tkinter as tk

class Block:
    """ Строим класс который набрасывает три элемента на окно
    """
    def __init__(self, master):
        self.entry_v = tk.Entry(master, width=20, bg = 'green')
        self.button_v = tk.Button(master, text = 'Chang')
        self.label_v = tk.Label(master, bg='green', fg='red', width=20)
        self.entry_v.pack()
        self.button_v.pack()
        self.label_v.pack()

    def setSelf(self, func):
        """ преображает через  eval функцию """

        self.button_v['command'] = eval('self.' + func)

    def strSort(self):
        """ Сортирует слова """

        s = self.entry_v.get()
        s = s.split()
        s.sort()
        self.label_v['text'] = ' '.join(s)

    def strReverse(self):
        """ переворачивает набор слов """
        
        s = self.entry_v.get()
        s = s.split()
        s.reverse()
        self.label_v['text'] = ' '.join(s)

root = tk.Tk()

first_block = Block(root)
first_block.setSelf('strSort')

second_block = Block(root)
second_block.setSelf('strReverse')

root.mainloop()