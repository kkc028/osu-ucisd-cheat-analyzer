import tkinter as tk
import math
from CheatChecks import CheatChecks
from tkinter import Image
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from PIL import ImageTk

root = tk.Tk();
root.attributes('-fullscreen', True)
background_image=tk.PhotoImage("727.gif")

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):

        FILENAME = '727.gif'
        canvas = tk.Canvas(root, width=1920, height=800)

        canvas.grid()
        canvas.create_text(1145, 50,text = "OSU UCISD", fill = "blue" , font="Times 35  bold")

        tk_img = ImageTk.PhotoImage(file=FILENAME)
        title_img = ImageTk.PhotoImage(file="title.png")
        osu_img = ImageTk.PhotoImage(file = "title2.png");

        canvas.create_image(500, 340, image=tk_img)
        canvas.create_image(480, 100, image = title_img)
        canvas.create_image(1150, 50, image = osu_img)

        fileInputButton = tk.Button(root, text= "Enter file", fg = "black", background = 'white', width = 20, height = 5,
            command = self.load_file, activebackground="#33B5E5", font="Times 10  bold")
        fileWindow = canvas.create_window(1070, 200, anchor='nw', window=fileInputButton)
        quit_button = tk.Button(root, text="Quit", fg = "black" , command=quit, background = 'white',
                                width=20, height = 3,  activebackground="#33B5E5",font="Times 10  bold")
        quit_button_window = canvas.create_window(1070, 370, anchor='nw', window=quit_button)

        root.mainloop()


    def load_file(self):
        filename = filedialog.askopenfilename(filetypes = (("Template files", "*.txt")
                                                         ,("HTML files", "*.html;*.htm")
                                                         ,("All files", "*.*") ))
        CheatChecks(filename)

app = Application()
app.master.title('Sample application')
app.mainloop()
