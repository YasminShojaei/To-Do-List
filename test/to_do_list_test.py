from model.entity.to_do_list import ToDoList
from model.repository.to_do_list_repository import ToDoListRepository
from controller.to_do_list_controller import ToDoListController

##test passed
# task1 = ToDoList(1001, "Deutsch", "1404-06-21", "lesson 1", "high")
# print(task1.to_tuple())
# print(task1.__repr__())


##test passed
# task_repo = ToDoListRepository()
# new_task = ToDoList(1006, "english class", "1404-06-22", "class", "high")
# task_repo.save_task(new_task)


##test passed
# task_controller = ToDoListController()
# status, message = task_controller.save_task(1006, "english class", "1404-06-22", "class", "high")
# print(status, message)


##test passed
# task_repo = ToDoListRepository()
# new_task = ToDoList(1003, "python", "1404-06-23", "class", "high")
# task_repo.edit_task(new_task)


## test passes
# task_controller = ToDoListController()
# status, message = task_controller.edit_task(1003, "python class", "1404-06-23", "class", "high")
# print(status, message)

##test passed
# task_repo = ToDoListRepository()
# task_repo.delete_task(1004)

##test passed
# task_controller = ToDoListController()
# status, message = task_controller.delete_task(1005)
# print(status, message)

##test passed
# task_repo = ToDoListRepository()
# task_repo.find_all_tasks()

##test passed
# task_controller = ToDoListController()
# status, message = task_controller.find_all_tasks()
# print(status, message)

##test paased
# task_repo = ToDoListRepository()
# task_repo.find_tasks_by_id(1002)


##test passed
# task_controller = ToDoListController()
# status, message = task_controller.find_tasks_by_id(1002)
# print(status, message)


##test passed
# task_repo = ToDoListRepository()
# task_repo.find_tasks_by_title("deutsch")


##test passed
# task_repo = ToDoListRepository()
# task_repo.find_tasks_by_date("1404-06-21")

##test passed
# task_controller = ToDoListController()
# status, message = task_controller.find_tasks_by_title("deutsch")
# print(status, message)


##test passed
# task_controller = ToDoListController()
# status, message = task_controller.find_tasks_by_date("1404-06-20")
# print(status, message)
