from model.tools.validation import *

class ToDoList:
    def __init__(self, id_, title, start_time, description, priority):
        self._id_ = id_
        self._title = title
        self._start_time = start_time
        self._description = description
        self._priority = priority

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return (self.id_, self.title, self.start_time, self.description, self.priority)


    @property
    def id_(self):
        return self._id_

    @id_.setter
    def id_(self, value):
        id_validator(value)
        self._id_ = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        title_validator(value)
        self._title = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        start_time_validator(value)
        self._start_time = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        description_validator(value)
        self._description = value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        priority_validator(value)
        self._priority = value