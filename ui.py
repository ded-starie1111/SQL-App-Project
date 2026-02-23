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
    def add_label(self,text):
        label = tk.Label(self.root,text=text, font=("Arial", 16), fg="blue")
        label.pack(pady=20)
        if not hasattr(self, "labels"):
            self.labels = []
        self.labels.append(label)
        return label
    def open_new_window(self, title="Secondary window", width=200, height=100):
        new_window = tk.Toplevel(self.root)
        new_window.title(title)
        new_window.geometry(f"{width}x{height}")
        return new_window
    def add_button(self, text, command=None,window = None,fg=None,bg=None):
        target = window if window is not None else self.root
        button = tk.Button(target, text=text, command=command, fg=fg, bg=bg)
        button.pack(pady=20)
        return button
window = Window()
window.set_geometry(width=400, height=300)
window.resize( True,False, window.root)
window.add_label("Hello World" )
new_window = window.open_new_window(title="Secondary window", width=400, height=300)
window.add_button("Click me!", fg="red", bg="green")
window.root.mainloop()