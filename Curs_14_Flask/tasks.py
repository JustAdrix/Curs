import csv
from model.task import Task


def _read_tasks():
    with open("data/tasks.csv", "r") as f:
        reader = csv.DictReader(f)
        return list(reader)  # transformam iteratorul reader
    # in lista de dictionare


def get_tasks():
    tasks = _read_tasks()
    # return [Task(*task.values()) for task in tasks] # List comprehension
    new_tasks = []
    for task in tasks:
        new_tasks.append(Task(task["title"], task["todo"], task["status"]))
        # new_tasks.append(Task(*task.values())) # despachetare cu *
    return new_tasks
