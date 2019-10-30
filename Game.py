import tkinter as tk

root = tk.Tk()

entry_v = tk.Entry(root, width=20, bg='grey')
button_v = tk.Button(root, text='Chang')
label_v = tk.Label(root, width=20, bg='blue', fg='white', font='Arial')

def str_sort(event):
    s = entry_v.get()
    s = s.split()
    s.sort()
    label_v['text'] = ' '.join(s)

button_v.bind('<Button-1>', str_sort)

entry_v.pack()
button_v.pack()
label_v.pack()

root.mainloop()