from typing import List, Any, Dict
from TaskPlanner.src.main.task import TaskStatus, Task
from collections import defaultdict


class Sprint:
    __slots__ = ["_all_task", "_name", "_start", "_end", "_user"]

    _name: str
    _start: int
    _end: int
    _all_task: List[Task]

    def __init__(self, name: str, start: int, end: int, user):
        self._name = name
        self._start = start
        self._end = end
        self._all_task = []
        self._user = user

    @property
    def name(self):
        return self._name

    def add_task(self, task: Task, user):
        if user != self._user:
            print(f"{user} is not authorized to do any changes to sprint: {self._name} ")
            return
        self._all_task.append(task)

    def remove_task(self, task: Task, user):
        if user != self._user:
            print(f" {user} is not authorized to do any changes sprint: {self._name}")
            return
        try:
            self._all_task.remove(task)
        except ValueError:
            print(f"task {task.name} not present in sprint")

    @staticmethod
    def build_status_string(task_dict: Dict[TaskStatus, List[Task]],  status: TaskStatus):
        str_ = ""
        for task in task_dict[status]:
            str_ += f"{task} "
        str_ += "\n"
        return str_

    def __str__(self):
        print("*"*20)
        str_ = f"Sprint : {self._name}\n"

        task_dict = defaultdict(list)
        for task in self._all_task:
            status = task.status
            task_dict[status].append(task)

        str_ += "TODO : " + self.build_status_string(task_dict, TaskStatus.TODO)
        str_ += "In progress : " + self.build_status_string(task_dict, TaskStatus.IN_PROGRESS)
        str_ += "Done : " + self.build_status_string(task_dict, TaskStatus.DONE)
        str_ += "Blocked : " + self.build_status_string(task_dict, TaskStatus.BLOCKED)
        str_ += "\n"
        return str_
