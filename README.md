## TraceView

A lightweight, resizable, always-on-top transparent image overlay for artists, designers, and creatives. Load images (PNG/JPEG) and trace or sketch directly on your screen with adjustable transparency and click-through modes.

---

# Features

- Resizable overlay window that stays on top of all programs
- Load images via a simple file browser (right-click to open)
- Adjust transparency of the entire window (image + background) using keyboard controls
- Toggle click-through mode to interact with programs underneath while keeping the image visible
- Supports PNG and JPEG image formats
- Cross-monitor DPI awareness for crisp display
- Simple and intuitive controls designed for tracing and drawing

---

# Installation

# Prerequisites

- Windows OS (Windows-only due to system-level transparency and click-through functionality)
- Python 3.6+
- Pillow (Python Imaging Library fork)

# Install dependencies

`pip install pillow`

Running the application

Clone or download this repository, then run:

`python main.py`

---

# Usage

- Right-click anywhere inside the window to open the file browser and select an image (PNG/JPEG)
- Use Up/Down arrow keys to increase or decrease the transparency of the entire overlay
- Press Ctrl + T to toggle click-through mode (allows clicking through the overlay to underlying windows)
- Move or resize the window using the standard window controls
- Press Esc to exit the program

---

# Controls Summary


Open image              : Right-click

Increase transparency   : Up Arrow

Decrease transparency   : Down Arrow

Toggle click-through    : Ctrl + T

Exit program            : Esc


# Troubleshooting

- No window appears?
  Ensure you’re running on Windows. The program uses Windows-specific APIs for transparency and click-through features.

- Transparency not working properly?
  Make sure your Windows version supports layered windows and window transparency (Windows 7 and above).

- Image does not load?
  Confirm the file is a supported PNG or JPEG image and not corrupted.

- Click-through mode stuck?
  Press Ctrl + T again to toggle it off.

---

# Contributing

Feel free to fork the repo and submit pull requests for improvements or new features.

---

