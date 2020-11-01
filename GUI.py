import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


class App(tk.Frame):
    # initialize object
    def __init__(self, master):
        self.master = master
        # load the first image
        load = Image.open("venv/images/start.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(master, image=render)
        img.image = render
        img.grid(row=0, column=0)
        # frame size
        self.master.geometry("806x" + str(master.winfo_screenheight() - 100))
        # make the backgound black
        self.master.configure(bg="black")

        # frame for the read only favour text and inventory
        text_frame = Frame(height=self.master.winfo_screenheight() - 100 - 486 - 30, width=806, bg="black")
        text_frame.grid(row=1, column=0)
        text_frame.columnconfigure(0, weight=10)
        text_frame.grid_propagate(False)

        # text box for the read only favour text
        text_box = Text(text_frame, bg="black", fg="lime")
        text_box.grid(columnspan=10,row=0, column=0, sticky="w")
        text_box.config(state=DISABLED)
        self.text_box = text_box

        # text box for the read only favour text
        inventory = tk.Text(text_frame, bg="black", fg="lime")
        inventory.grid(row=0, column=1, sticky="e")
        inventory.config(state=DISABLED)
        self.inventory = inventory

        # user input text box
        self.entry = tk.Entry(master, width=88, bg="black", fg="lime")
        self.entry.grid(row=3, column=0)

        # listen for the return key, if pressed, send whatever string is in the user input box to the handler,
        # and clear the text box
        master.bind("<Return>", self.user_input)

    # Function to add text to the read only text box
    def add_text(self, text):
        self.text_box.config(state=NORMAL)
        self.text_box.insert(tk.END, text + "\n")
        self.text_box.see("end")
        self.text_box.config(state=DISABLED)

    # Function to read and delete the user input
    def user_input(self, param):
        self.handle_input(self.entry.get())
        self.entry.delete(0, 'end')

    # Function to load a new image within the images directory. Need to be given the name of the image
    def load_image(self, img_name):
        load = Image.open("venv/images/" + img_name + ".jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self.master, image=render)
        img.image = render
        img.grid(row=0, column=0)

    # Funciton to handle the different user inputs
    def handle_input(self, text):
        if text == "ok":
            self.load_image("image1")
        else:
            self.add_text("wrong" + text)

def main():
    root = Tk()
    root.title('OpenDungeon')
    App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
