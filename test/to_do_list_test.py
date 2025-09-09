from model.entity.to_do_list import ToDoList

##test passed
task1 = ToDoList(1001, "Deutsch", "1404-06-21", "lesson 1", "high")
print(task1.to_tuple())
print(task1.__repr__())