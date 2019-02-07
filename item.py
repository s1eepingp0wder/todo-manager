import manager
class Item():
    def __init__(self, task_name, task_description, task_timestamp, task_isfinished):
        # For my personal demons that keep annoying me about this.
        # This is when you initialize an instance. It tells the code that hey, the arguments in parenthesis are assigned to these parts of the instance.
        manager.__init__(self, task_name, task_description, task_timestamp, task_isfinished)

    def read_task(self):
        task_file = open("./todos.txt", 'r')
        print("Task List:")
        i = 0
        for line in task_file:
            i += 1
            line_array = line.split(",")
            print(f"{i}. {line_array[0]}")
