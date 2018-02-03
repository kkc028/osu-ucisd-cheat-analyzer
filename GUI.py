import tkinter as tk

root = tk.Tk();
root.attributes('-fullscreen', True)

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
button.place(y = 4)

root.mainloop()