from tkinter import *
from PIL import Image, ImageTk


class ToDoListView:
    def __init__(self):

        window = Tk()
        window.title("To-Do List")
        window.geometry("1920x1920")
        window.config(cursor = "hand2", background = "light yellow")

        img = Image.open("to_do_list.png")
        photo = ImageTk.PhotoImage(img)
        my_label = Label(window, image = photo)
        my_label.image = photo
        my_label.pack(side = LEFT)
        my_label.place(x = 0, y = 0)

        Label(window, text = "ID:",background = "light yellow", font=("Arial", 12)).place(x = 20, y = 350)
        self.id_ = IntVar()
        Entry(window, textvariable = self.id_, background= "light yellow", font=("Arial", 12)).place(x = 135, y = 350)

        Label(window, text = "Titel:",background = "light yellow", font=("Arial", 12)).place(x = 20, y = 400)
        self.title = StringVar()
        Entry(window, textvariable = self.title, background= "light yellow", font=("Arial", 12)).place(x = 135, y = 400)

        Label(window, text = "Starting at:",background = "light yellow", font=("Arial", 12)).place(x = 20, y = 450)
        self.start_time = StringVar()
        Entry(window, textvariable = self.start_time, background= "light yellow", font=("Arial", 12)).place(x = 135, y = 450)

        Label(window, text = "description:",background = "light yellow", font=("Arial", 12)).place(x = 20, y = 500)
        self.description = StringVar()
        Entry(window, textvariable = self.description, background= "light yellow", font=("Arial", 12)).place(x = 135, y = 500)

        Label(window, text = "priority:",background = "light yellow", font=("Arial", 12)).place(x = 20, y = 550)
        self.priority = StringVar()
        Entry(window, textvariable = self.priority, background= "light yellow", font=("Arial", 12)).place(x = 135, y = 550)






        window.mainloop()