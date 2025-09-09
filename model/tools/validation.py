from datetime import datetime


def id_validator(id_):
    if not ((type(id_) is int) and (1000 <= id_ <= 9999 )):
        raise TypeError("id_ must an integer and be between 1000 and 9999")

def title_validator(title):
    if not ((type(title) is str) and (3 <= len(title))):
        raise TypeError("title must contain at least 3 characters")

def start_time_validator(start_time):
    try:
        if type(start_time) == str:
            datetime.strptime(start_time, "%Y-%m-%d")
        elif type(start_time) == datetime:
            pass
        else:
            raise TypeError("start_time must be a string in 'YYYY-MM-DD' format or a datetime object")
    except ValueError:
        raise ValueError("start_time must be in 'YYYY-MM-DD' format")

def description_validator(description):
    if not ((type(description) is str) and (3 <= len(description))):
        raise TypeError("description must contain at least 3 characters")

def priority_validator(priority):
    if not ((type(priority) is str) and (3 <= len(priority))):
        raise TypeError("priority must contain at least 3 characters")


