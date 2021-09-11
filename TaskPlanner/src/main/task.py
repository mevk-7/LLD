from enum import Enum, auto
from abc import abstractmethod, ABC
from typing import Any


class InvalidTaskType(ValueError):
    pass


class TaskStatus:
    __slots__ = []

    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    BLOCKED = "BLOCKED"


class TaskType:
    __slots__ = []
    BUG = auto()
    FEATURE = auto()
    STORY = auto()


class Task:
    __slots__ = ["_name", "_type", "_status", "_user"]
    _name: str
    _type: TaskType.BUG

    def __init__(self, name, user):
        self._name = name
        self._user = user
        self._status = TaskStatus.TODO
        self._type = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def status(self):
        return self._status

    def set_status(self, status_, user):
        if status_ not in [TaskStatus.TODO, TaskStatus.BLOCKED,
                           TaskStatus.DONE, TaskStatus.IN_PROGRESS]:
            print(f"passed status: {status_} is not supported")
            return
        if self._user != user:
            print(f"user: {user} is not authorized to status of task : {self}")
            return
        self._status = status_
        print(f"Set the status of task : {self.name} to : {status_}")

    def __str__(self):
        return f"Task : {self._name}, status : {self._status}"


class BugTask(Task):
    __slots__ = []

    def __init__(self, name, user) -> None:
        super().__init__(name, user)
        self._type = TaskType.BUG


class FeatureTask(Task):
    __slots__ = []

    def __init__(self, name, user) -> None:
        super().__init__(name, user)
        self._type = TaskType.FEATURE


class StoryTask(Task):
    __slots__ = ["_subtask"]

    def __init__(self, name, user) -> None:
        super().__init__(name, user)
        self._type = TaskType.STORY

    def add_subtask(self, task: Task):
        self._subtask.append(task)

    @property
    def get_all_subtask(self):
        return self._subtask


def task_factory( name: str, task_type: TaskType, user) -> Task:

    if task_type == TaskType.BUG:
        return BugTask(name, user)
    elif task_type == TaskType.FEATURE:
        return FeatureTask(name, user)
    elif task_type == TaskType.STORY:
        return StoryTask(name, user)
    raise InvalidTaskType("Invalid task type has been passed")
