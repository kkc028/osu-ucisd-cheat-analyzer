import tkinter as tk

root = tk.Tk();
root.attributes('-fullscreen', True)

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', fg = "red",
            command=self.quit)
        self.quitButton.pack()
        self.quitButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()