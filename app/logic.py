import json
import os

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load()  # Load tasks from file on initialization
    
    def add_task(self, task):
        """Add a task to the list."""
        self.tasks.append(task)
        self.save()  # Save to file after adding
     
    def remove_task(self, index):
        """Remove a task based on the index."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save()  # Save after removing
    
    def clear_all(self):
        """Clear all tasks."""
        self.tasks = []
        self.save()  # Save after clearing
    
    def save(self):
        """Save the tasks to a JSON file."""
        with open(r"data/data.json", "w") as f:
            json.dump(self.tasks, f)
    
    def load(self):
        """Load tasks from a JSON file."""
        if os.path.exists(r"data/data.json"):
            with open(r"data/data.json", "r") as f:
                self.tasks = json.load(f)
    
    def get_tasks(self):
        """Return the current list of tasks."""
        return self.tasks
