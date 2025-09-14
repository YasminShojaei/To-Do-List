from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import Image, ImageTk

from controller.to_do_list_controller import ToDoListController


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

        Label(window, text = "ID:",background = "light yellow", font=("Arial", 12)).place(x = 20, y = 250)
        self.id_ = IntVar()
        Entry(window, textvariable = self.id_, background= "khaki1", font=("Arial", 12)).place(x = 135, y = 250)

        Label(window, text = "Title:",background = "light yellow", font=("Arial", 12)).place(x = 20, y = 300)
        self.title = StringVar()
        Entry(window, textvariable = self.title, background= "khaki1", font=("Arial", 12)).place(x = 135, y = 300)

        Label(window, text = "Starting at:",background = "light yellow", font=("Arial", 12)).place(x = 20, y = 350)
        self.start_time = StringVar()
        Entry(window, textvariable = self.start_time, background= "khaki1", font=("Arial", 12)).place(x = 135, y = 350)

        Label(window, text = "description:",background = "light yellow", font=("Arial", 12)).place(x = 20, y = 400)
        self.description = StringVar()
        Entry(window, textvariable = self.description, background= "khaki1", font=("Arial", 12)).place(x = 135, y = 400)

        Label(window, text = "priority:",background = "light yellow", font=("Arial", 12)).place(x = 20, y = 450)
        self.priority = StringVar()
        Entry(window, textvariable = self.priority, background= "khaki1", font=("Arial", 12)).place(x = 135, y = 450)


        self.to_do_list_table = ttk.Treeview(window, columns=[1,2,3,4,5], show="headings",height=20)

        self.to_do_list_table.heading(1, text="ID")
        self.to_do_list_table.heading(2, text="Title")
        self.to_do_list_table.heading(3, text="Start time")
        self.to_do_list_table.heading(4, text="description")
        self.to_do_list_table.heading(5, text="priority")

        self.to_do_list_table.column(1, width = 150, anchor = "center")
        self.to_do_list_table.column(2, width = 150, anchor = "center")
        self.to_do_list_table.column(3, width = 150, anchor = "center")
        self.to_do_list_table.column(4, width = 150, anchor = "center")
        self.to_do_list_table.column(5, width = 150, anchor = "center")

        self.to_do_list_table.place(x=400, y=15, height= 710)

        self.to_do_list_table.bind("<<TreeviewSelect>>", self.table_select_task)

        Button(window, text = "save", width=42, background="khaki1", command=self.save_task).place(x = 20, y = 500)
        Button(window, text = "edit", width=42, background="khaki1", command=self.edit_task).place(x = 20, y = 550)
        Button(window, text = "delete", width=42, background="khaki1", command=self.delete_task).place(x = 20, y = 600)
        Button(window, text = "search", width=42, background="khaki1", command=self.search_task).place(x = 20, y = 650)
        Button(window, text = "clear", width=42, background="khaki1", command=self.reset).place(x = 20, y = 700)


        window.mainloop()

    def save_task(self):
        id_ = self.id_.get()
        title = self.title.get()
        start_time = self.start_time.get()
        description = self.description.get()
        priority = self.priority.get()

        controller = ToDoListController()
        result, message = controller.save_task(id_, title, start_time, description, priority)

        if result:
            msg.showinfo("Task saved", message)
            self.load_student()
            self.reset()

        else:
            msg.showerror("Task saving failed", message)

    def edit_task(self):
        id_ = self.id_.get()
        title = self.title.get()
        start_time = self.start_time.get()
        description = self.description.get()
        priority = self.priority.get()

        controller = ToDoListController()
        result, message = controller.edit_task(id_, title, start_time, description, priority)

        if result:
            msg.showinfo("Task edited", message)
            self.load_student()
            self.reset()

        else:
            msg.showerror("Task editing failed", message)


    def delete_task(self):
        id_ = self.id_.get()

        if not id_:
            msg.showerror("Please enter a valid ID to delete")
            return

        controller = ToDoListController()
        result, message = controller.delete_task(id_)

        if result:
            msg.showinfo("Task deleted", message)
            self.load_student()
            self.reset()

        else:
            msg.showerror("Task deletion failed", message)


    def reset(self):
        self.id_.set(0)
        self.title.set("")
        self.start_time.set("")
        self.description.set("")
        self.priority.set("")

        self.to_do_list_table.selection_remove(self.to_do_list_table.selection())


    def search_task(self):
        id_ = self.id_.get()
        title = self.title.get().strip()
        start_time = self.start_time.get().strip()

        controller = ToDoListController()

        for row in self.to_do_list_table.get_children():
            self.to_do_list_table.delete(row)

        if id_:
            success, result = controller.find_tasks_by_id(id_)

            if success and result:

                task = result[0] if isinstance(result, list) else [result]
                self.to_do_list_table.insert("", "end", values=task)
                self.id_.set(task[0])
                self.title.set(task[1])
                self.start_time.set(task[2])
                self.description.set(task[3])
                self.priority.set(task[4])


            else:
                msg.showerror("Please enter a valid ID")

        elif title:
            success, result = controller.find_tasks_by_title(title)

            if success and result:
                for task in result:
                    self.to_do_list_table.insert("", "end", values=(task[0], task[1], task[2], task[3], task[4]))

            else:
                msg.showerror("Please enter a valid title")

        if start_time:
            success , result = controller.find_tasks_by_date(start_time)

            if success and result:
                for task in result:
                    self.to_do_list_table.insert("", "end", values=(task[0], task[1], task[2], task[3], task[4]))

            else:
                msg.showerror("Please enter a valid date")


    def load_student(self):
        controller = ToDoListController()
        success , result = controller.find_all_tasks()

        if success:
            for row in self.to_do_list_table.get_children():
                self.to_do_list_table.delete(row)

            for task in result:
                self.to_do_list_table.insert("", "end", values=task)
        else:
            msg.showerror("No tasks found", f"error loading task {result}")

    def table_select_task(self, event):
        selected_item = self.to_do_list_table.focus()

        if not selected_item:
            return

        values = self.to_do_list_table.item(selected_item)["values"]

        if values:
            self.id_.set(values[0])
            self.title.set(values[1])
            self.start_time.set(values[2])
            self.description.set(values[3])
            self.priority.set(values[4])