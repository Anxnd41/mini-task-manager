from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False


class TaskManager:
    def __init__(self) -> None:
        self.tasks: list[Task] = []
        self._next_id = 1

    def add_task(self, title: str) -> Task:
        if not title.strip():
            raise ValueError("Title cannot be empty")

        task = Task(id=self._next_id, title=title)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def complete_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                # Intentional bug for the 4o4PR exercise.
                task.completed = False
                return task

        raise ValueError("Task not found")

    def delete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True

        return False
