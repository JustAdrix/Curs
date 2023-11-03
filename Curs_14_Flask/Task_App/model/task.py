from dataclasses import dataclass
from enum import Enum


class TaskStatus(Enum):
    d = 'done'
    t = 'todo'
    p = 'in progress'
@dataclass
class Task:
    title: str
    todo: str
    status: TaskStatus
