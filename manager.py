class Manager():
    def __init__(self, task_name, task_description):
        # For my personal demons that keep annoying me about this.
        # This is when you initialize an instance. It tells the code that hey, the arguments in parenthesis are assigned to these parts of the instance.
        self.task_name = task_name
        self.task_description = task_description

    def write_task(self):
        f = open("todos.txt", "a")
        f.write()
        print("Check the file.")
