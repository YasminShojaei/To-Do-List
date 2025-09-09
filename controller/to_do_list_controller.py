from streamlit import title

from model.entity.to_do_list import ToDoList
from model.repository.to_do_list_repository import ToDoListRepository

class ToDoListController:

    def save_task(self, id_, title, start_time, description, priority):

        try:
            task = ToDoList(id_, title, start_time, description, priority)
            task_repo  = ToDoListRepository()
            task_repo.save_task(task)
            return True, f"Tasks saved {id_}, {title}"
        except Exception as e:
            return False, f"Error saving task {e}"

    def edit_task(self, id_, title, start_time, description, priority):

        try:
            new_task = ToDoList(id_, title, start_time, description, priority)
            task_repo = ToDoListRepository()
            task_repo.edit_task(new_task)
            return True, f"Task edited {new_task}"
        except Exception as e:
            return False, f"Error editing task {e}"

    def delete_task(self, id_):

        try:
            task_repo = ToDoListRepository()
            task_repo.delete_task(id_)
            return True, f"Task deleted {id_}, {title}"
        except Exception as e:
            return False, f"Error deletin task {e}"

    def find_all_tasks(self):
        try:
            task_repo = ToDoListRepository()
            return True, task_repo.find_all_tasks()

        except Exception as e:
            return False, f"Error findig all tasks {e}"

    def find_tasks_by_id(self, id_):
        try:
            task_repo = ToDoListRepository()
            return True, task_repo.find_tasks_by_id(id_)
        except Exception as e:
            return False, f"Error finding tasks {e}"

    def find_tasks_by_title(self, title):
        try:
            task_repo = ToDoListRepository()
            return True, task_repo.find_tasks_by_title(title)
        except Exception as e:
            return False, f"Error finding tasks {e}"

    def find_tasks_by_date(self, start_time):
        try:
            task_repo = ToDoListRepository()
            return True, task_repo.find_tasks_by_date(start_time)
        except Exception as e:
            return False, f"Error finding tasks {e}"

