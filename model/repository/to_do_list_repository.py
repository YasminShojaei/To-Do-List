import sqlite3
import os

class ToDoListRepository:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        db_path = os.path.join(os.path.dirname(__file__), "to_do_list_db.sqlite")
        print("DB absolute path:", db_path)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def disconnect(self, commit = False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save_task(self, new_task):
        self.connection()
        self.cursor.execute(
            """ INSERT INTO TASKS
                    (title, start_time, description, priority)
                VALUES (?,?,?,?) """,
            (new_task.title, new_task.start_time, new_task.description, new_task.priority)
        )
        self.disconnect(commit = True)

    def edit_task(self, new_task):
        self.connect()
        self.cursor.execute("update TASKS set title=?, start_time=?, description=?, priority=? where id_=?",
                            [new_task.title, new_task.start_time, new_task.description, new_task.priority, new_task.id])
        self.disconnect(commit = True)

    def delete_task(self, id_):
        self.connect()
        self.cursor.execute("delete from TASKS where id_=?", [id_])
        self.disconnect(commit = True)

    def find_all_tasks(self):
        self.connect()
        self.cursor.execute("select * from TASKS")
        tasks_list = self.cursor.fetchall()
        self.disconnect()
        return tasks_list

    def find_tasks_by_id(self, id_):
        self.connect()
        self.cursor.execute("select * from TASKS where id_=?", [id_])
        tasks_list = self.cursor.fetchall()
        self.disconnect()
        return tasks_list

    def find_tasks_by_title(self, title):
        self.connect()
        self.cursor.execute("select * from TASKS where title=?", [title])
        tasks_list = self.cursor.fetchall()
        self.disconnect()
        return tasks_list

    def find_tasks_by_date(self, start_time):
        self.connect()
        self.cursor.execute("select * from TASKS where start_time=?", [start_time])
        tasks_list = self.cursor.fetchall()
        self.disconnect()
        return tasks_list

