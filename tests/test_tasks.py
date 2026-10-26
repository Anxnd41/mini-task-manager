import pytest

from task_manager import TaskManager


def test_add_task_assigns_id_and_defaults_to_incomplete() -> None:
    manager = TaskManager()

    task = manager.add_task("Learn agentic AI")

    assert task.id == 1
    assert task.title == "Learn agentic AI"
    assert task.completed is False


def test_empty_title_is_rejected() -> None:
    manager = TaskManager()

    with pytest.raises(ValueError, match="Title cannot be empty"):
        manager.add_task("   ")


def test_complete_task_marks_task_as_completed() -> None:
    manager = TaskManager()
    task = manager.add_task("Write tests")

    completed_task = manager.complete_task(task.id)

    assert completed_task.completed is True


def test_unknown_task_cannot_be_completed() -> None:
    manager = TaskManager()

    with pytest.raises(ValueError, match="Task not found"):
        manager.complete_task(999)


def test_delete_task_removes_existing_task() -> None:
    manager = TaskManager()
    task = manager.add_task("Delete me")

    result = manager.delete_task(task.id)

    assert result is True
    assert manager.tasks == []
