class Manager():
    def __init__(self, task_name, task_description):
        # For my personal demons that keep annoying me about this.
        # This is when you initialize an instance. It tells the code that hey, the arguments in parenthesis are assigned to these parts of the instance.
        self.task_name = task_name
        self.task_description = task_description

    def write_task(self):
        f = open("./todos.txt", 'a+')
        print(f.readlines())

        # file = eval(f)
        #     # new_dict= {"Task Name" : task_name, "Task Description": task_description}

        # We need to pull any current dicts from this.
        #  try:
        #     file = eval(f)
        #     # new_dict= {"Task Name" : task_name, "Task Description": task_description}
        #     print(len(file))
        # # print("Check the file.")
        # except:
        #     print("Can't do anything yet.")
