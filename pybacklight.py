import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.w = tk.Scale(self.master, from_=0, to=200, orient=tk.HORIZONTAL)
        self.w.pack(side="top")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
