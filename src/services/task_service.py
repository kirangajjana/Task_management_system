from src.models import Queue, Stack, Task, Graph  # Make sure imports are correct

class Task_service:
    def __init__(self):
        self.tasks = []
        self.task_queue = Queue()
        self.task_history = Stack()

    def create_task(self, id, title, description):
        task = Task(id, title, description)
        self.tasks.append(task)
        self.task_queue.Enqueue(task)  # Use enqueue() to add to the queue
        return task

    def complete_task(self):
        if not self.task_queue.is_empty():
            task = self.task_queue.Dequeue()
            self.task_history.push(task)
            return task
        return None

    def get_task_history(self):
        return self.task_history.item  # Corrected: Access the stack items