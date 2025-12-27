import json
from Task import Task

class TaskManager:
    def __init__(self):
        self.task_list = []
        self.next_id = 1
        self.load_from_file()
    
    def add_task(self, title, priority, due_date):
        task = Task(self.next_id, title, priority, due_date)
        self.task_list.append(task)
        self.next_id += 1
        self.save_to_file()
        return task
    
    def view_tasks(self):
        return self.task_list
    
    def update_task(self, task_id, title=None, priority=None, due_date=None):
        task = self._find_task(task_id)
        if task:
            if title: task.title = title
            if priority: task.priority = priority
            if due_date: task.due_date = due_date
            self.save_to_file()
            return True
        return False
    
    def mark_complete(self, task_id):
        task = self._find_task(task_id)
        if task:
            task.status = "Completed"
            self.save_to_file()
            return True
        return False
    
    def delete_task(self, task_id):
        task = self._find_task(task_id)
        if task:
            self.task_list.remove(task)
            self.save_to_file()
            return True
        return False
    
    def filter_tasks(self, by="status", value=None):
        if by == "status":
            return [t for t in self.task_list if t.status == value]
        elif by == "due_date":
            return [t for t in self.task_list if t.due_date == value]
        return self.task_list
    
    def save_to_file(self):
        try:
            with open("tasks.json", "w") as f:
                json.dump([t.to_dict() for t in self.task_list], f, indent=2)
        except Exception as e:
            print(f"Error saving: {e}")
    
    def load_from_file(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                self.task_list = [Task.from_dict(t) for t in data]
                self.next_id = max([t.id for t in self.task_list], default=0) + 1
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error loading: {e}")
    
    def _find_task(self, task_id):
        return next((t for t in self.task_list if t.id == task_id), None)
