from TaskPlanner.src.main.user import User
from TaskPlanner.src.main.task import TaskType, TaskStatus

if __name__ == '__main__':
    user1 = User("vikrant")
    sprint1 = user1.create_sprint("Sprint 1", 1, 5)
    task1 = user1.create_task("Task 1", TaskType.BUG)
    task2 = user1.create_task("Task 2", TaskType.FEATURE)
    user1.add_task_to_sprint(sprint1, task1)
    user1.add_task_to_sprint(sprint1, task2)
    user1.change_task_status(task1, TaskStatus.DONE)
    user1.print_all_task()
    user1.print_pending_task()
    print(sprint1)
    user1.remove_task_to_sprint(sprint1, task1)
    print(sprint1)
    user2 = User("Some other guy")
    user2.remove_task_to_sprint(sprint1, task2)
    print(sprint1)
