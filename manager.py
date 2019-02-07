import datetime
class Manager():
    def __init__(self, task_name, task_description, task_timestamp, task_isfinished):
        # For my personal demons that keep annoying me about this.
        # This is when you initialize an instance. It tells the code that hey, the arguments in parenthesis are assigned to these parts of the instance.
        self.task_name = task_name
        self.task_description = task_description
        self.task_timestamp = task_timestamp
        self.task_isfinished = task_isfinished

    def write_task(self):
        # new_task= [self.task_name, self.task_description, self.task_timestamp, self.task_isfinished]
        f = open("./todos.txt", "a+")
        f.write(f"{self.task_name}, {self.task_description}, {self.task_timestamp}, {self.task_isfinished}\n")
        f.close()
        print("Task Written. Type \"list\" to view all tasks.")
