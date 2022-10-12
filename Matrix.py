from tkinter import *

rows = []

for i in range(10):

    cols = []

    for j in range(10):

        e = Entry(relief=GROOVE)

        e.grid(row=i, column=j, sticky=NSEW)

        e.insert(END, '%d.%d' % (i, j))

        cols.append(e)

    rows.append(cols)

mainloop()
