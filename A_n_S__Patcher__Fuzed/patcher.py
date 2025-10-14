import os
import tkinter as tk
from tkinter import PhotoImage, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Window, Frame, Label, Button, Menu

# Lokale Datei importieren
import patcher_methods as patcher_methods  # Achte darauf, dass patcher_methods.py die Funktion center_window definiert

def show_main_window():
    base_path = os.path.abspath(".")
    root = Window(themename="superhero")
    root.title("A.n.S Patcher")

    icon_path = os.path.join(base_path, "A_n_S__Patcher__Fuzed", "assets", "icon.png")
    try:
        icon = PhotoImage(file=icon_path)
        root.iconphoto(True, icon)
    except tk.TclError:
        print(f"Icon file not found or invalid: {icon_path}")
        icon = None

    root.geometry("600x400")
    root.minsize(600, 400)

    patcher_methods.center_window(root)

    # Top toolbar (Menu)
    menubar = Menu(root)
    root.config(menu=menubar)

    # Tools dropdown
    tools_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Tools", menu=tools_menu)
    tools_menu.add_command(label="Settings", command=lambda: messagebox.showinfo("Info", "Changing settings"))
    tools_menu.add_command(label="Stop", command=lambda: messagebox.showinfo("Info", "Stopping backup."))

    # Dependencies dropdown
    dependencies_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Dependencies", menu=dependencies_menu)
    # Add items to dependencies_menu here if needed

    # Help dropdown
    help_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Help", command=lambda: messagebox.showinfo("Info", "Help information"))


    # Main frame for logo and button
    main_frame = Frame(root)
    main_frame.pack(expand=True, fill='both', pady=20)

    # Logo
    if icon:
        logo_label = Label(main_frame, image=icon)
        logo_label.pack(pady=20)

    # Patch now button
    patch_button = Button(main_frame, text="Patch now", bootstyle="success")
    patch_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    show_main_window()
