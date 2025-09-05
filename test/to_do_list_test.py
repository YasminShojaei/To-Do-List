from jedi.inference.utils import to_tuple

from model.entity.to_do_list import ToDoList

##test passed
task1 = ToDoList(1001, "deutsch", "1404-06-21", "lektion1", "high")
print(task1.to_tuple())
print(task1.__repr__())