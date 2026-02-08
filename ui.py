import tkinter as tk

class Window:
    def __init__(self):
        self.root = tk.Tk()
    def set_geometry(self, window=None, width=1080, height=600):
        target = window if window is not None else self.root
        target.geometry(f"{width}x{height}")
    def resize(self, width = None, height = None, window = None):
        target = window if window is not None else self.root
        target.resizable(width, height)

window = Window()
window.set_geometry(window.root)
window.resize( True,False, window.root)
window.root.mainloop()
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Вторичное окно")
    new_window.geometry("200x100")