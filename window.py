import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class MyGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x500")
        self.window.title("Cyberlike")
        self.window.resizable(False, False)

        #icon for window
        self.ico = Image.open('Cyberlike_Icon.jpg')
        self.photo = ImageTk.PhotoImage(self.ico)
        self.window.wm_iconphoto(False, self.photo)

        #create menu bar
        self.menubar = tk.Menu(self.window)

        #File menu
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Quit", command=self.on_closing)
        self.filemenu.add_command(label="Quit without warning", command=exit)
        #Action menu
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message (ctrl + Enter)", command=self.show_message)
        self.actionmenu.add_command(label="Clear", command=self.clear)
        #Add the menus to the top bar
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")
        
        self.window.config(menu=self.menubar)

        self.label = tk.Label(self.window, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.window, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)
        
        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.window, text="Show messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.window, text="Show message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.window, text="Clear", font=('Arial', 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        if event.state == 4 and event.keysym == "Return":
            self.show_message()
    
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?"):
            self.window.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)
        

MyGUI()
