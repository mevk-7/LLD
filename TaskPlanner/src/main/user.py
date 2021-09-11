from typing import List, Any
from TaskPlanner.src.main.task import Task, TaskStatus, task_factory, TaskType
from TaskPlanner.src.main.sprint import Sprint


class User:
    __slots__ = ["_name", "_all_task", "_all_sprint"]
    _name: str
    _all_task: List[Task]
    _all_sprint: List[Sprint]

    def __init__(self, name: str) -> None:
        self._name = name
        self._all_task = []
        self._all_sprint = []

    @property
    def name(self) -> str:
        return self._name

    def print_pending_task(self) -> None:
        print("*" * 10, "pending task", "*" * 10)
        for task in self._all_task:
            if task.status != TaskStatus.DONE:
                print(task)

    def print_all_task(self):
        print("*"*10, "all task", "*"*10)
        for task in self._all_task:
            print(task)

    def create_task(self, task_name: str,  task_type: TaskType) -> Task:
        new_task = task_factory(task_name, task_type, self)
        self._all_task.append(new_task)
        return new_task

    def change_task_status(self, task: Task, status: TaskStatus) -> None:

        task.set_status(status, self)

    def create_sprint(self, sprint_name: str, start: int, end: int) -> Sprint:
        sprint = Sprint(sprint_name, start, end, self)
        self._all_sprint.append(sprint)
        return sprint

    def add_task_to_sprint(self, sprint: Sprint, task: Task) -> None:
        sprint.add_task(task, self)

    def remove_task_to_sprint(self, sprint: Sprint, task: Task) -> None:
        sprint.remove_task(task, self)

    # TODO add sub task to story
    def add_task_to_story(self, story:Task):
        pass

    def __str__(self):
        return self._name
