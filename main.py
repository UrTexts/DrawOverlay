import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import ctypes
import sys

class TransparentOverlay:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Tracer Overlay")
        self.root.attributes("-topmost", True)
        self.pass_through = False
        self.original_image = None
        self.tk_image = None
        self.root.geometry("800x650+100+100")

        self.canvas = tk.Canvas(root, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.prompt = tk.Label(self.canvas, text="Right-click to load an image\n(PNG or JPEG)",
                               font=("Segoe UI", 16), fg="gray", bg="white", justify="center")
        self.prompt.place(relx=0.5, rely=0.5, anchor="center")

        # Transparency from 0.1 (almost invisible) to 1.0 (opaque)
        self.transparency = 1.0
        self.root.attributes("-alpha", self.transparency)

        # Bindings
        root.bind("<Escape>", lambda e: root.destroy())
        root.bind("<Control-t>", self.toggle_pass_through)
        root.bind("<Up>", self.increase_transparency)
        root.bind("<Down>", self.decrease_transparency)
        self.canvas.bind("<Button-3>", self.open_image)
        root.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        if self.original_image:
            self.update_image()

    def open_image(self, event=None):
        print("Opening file dialog...")
        self.root.update()

        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        print(f"Selected path: {path}")

        if path:
            self.load_image(path)

    def load_image(self, path):
        try:
            self.original_image = Image.open(path).convert("RGBA")
            self.prompt.place_forget()
            self.update_image()
        except Exception as e:
            print("Failed to load image:", e)

    def update_image(self):
        if not self.original_image:
            return
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        if w < 1 or h < 1:
            return

        resized = self.original_image.resize((w, h), Image.LANCZOS)

        self.tk_image = ImageTk.PhotoImage(resized)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

        # Set whole window transparency here:
        self.root.attributes("-alpha", self.transparency)

    def toggle_pass_through(self, event=None):
        self.pass_through = not self.pass_through
        self.set_click_through(self.pass_through)
        print(f"Pass-through {'enabled' if self.pass_through else 'disabled'}")

    def set_click_through(self, enable):
        hwnd = ctypes.windll.user32.FindWindowW(None, "Image Tracer Overlay")
        if hwnd:
            GWL_EXSTYLE = -20
            WS_EX_LAYERED = 0x80000
            WS_EX_TRANSPARENT = 0x20

            style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)

            if enable:
                style |= WS_EX_LAYERED | WS_EX_TRANSPARENT
            else:
                style &= ~WS_EX_TRANSPARENT
                style |= WS_EX_LAYERED

            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)

    def increase_transparency(self, event=None):
        self.transparency = min(1.0, self.transparency + 0.05)
        print(f"Transparency increased to {self.transparency:.2f}")
        self.root.attributes("-alpha", self.transparency)

    def decrease_transparency(self, event=None):
        self.transparency = max(0.1, self.transparency - 0.05)
        print(f"Transparency decreased to {self.transparency:.2f}")
        self.root.attributes("-alpha", self.transparency)


if __name__ == "__main__":
    if sys.platform != "win32":
        print("This program only works on Windows.")
        sys.exit()

    ctypes.windll.shcore.SetProcessDpiAwareness(1)

    root = tk.Tk()
    app = TransparentOverlay(root)
    root.mainloop()

