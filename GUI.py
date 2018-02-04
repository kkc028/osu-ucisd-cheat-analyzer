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
        # canvas.create_text(1070, 50,"OSU UCISD")

        tk_img = ImageTk.PhotoImage(file=FILENAME)
        canvas.create_image(500, 340, image=tk_img)
        fileInputButton = tk.Button(root, text= "Enter file", fg = "black", background = 'white', width = 20, height = 5,
            command = self.load_file, activebackground="#33B5E5")
        fileWindow = canvas.create_window(1070, 200, anchor='nw', window=fileInputButton)
        quit_button = tk.Button(root, text="Quit", command=self.quit, anchor='w',
                                width=20, activebackground="#33B5E5")
        quit_button_window = canvas.create_window(1070, 370, anchor='nw', window=quit_button)

        root.mainloop()

        # self.fileInputButton.grid(row = 0, column = 1, pady = 200, ipadx = 50, ipady = 20)
        # self.grid(row = 1, column = 1, padx = 1100, pady = 100)
        # self.grid(row = 2, ipadx = 0, ipady = 100)
        # self.quitButton = tk.Button(self, text='Quit', fg = "red",
        #     command=self.quit)
        # self.quitButton.grid(row = 3, column = 1, ipadx = 55, ipady = 20)

    def load_file(self):
        filename = filedialog.askopenfilename(filetypes = (("Template files", "*.txt")
                                                         ,("HTML files", "*.html;*.htm")
                                                         ,("All files", "*.*") ))
        CheatChecks(filename)

app = Application()
app.master.title('Sample application')
app.mainloop()
