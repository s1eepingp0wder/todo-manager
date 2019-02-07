import datetime
import item
class Manager(item.Item):
    def __init__(self, task_name, task_description, task_timestamp, task_isfinished):
        item.Item.__init__(self, task_name, task_description, task_timestamp, task_isfinished)

    def write_task(self):
        # new_task= [self.task_name, self.task_description, self.task_timestamp, self.task_isfinished]
        f = open("./todos.txt", "a+")
        f.write(f"{self.task_name},{self.task_description},{self.task_timestamp},{self.task_isfinished}\n")
        f.close()
        print("Task Written. Type \"list\" to view all tasks.")


def list_all():
    task_file = open("./todos.txt", 'r')
    print("Task List:")
    i = 0
    for line in task_file:
        i += 1
        line_array = line.split(",")
        print(f"{i}. {line_array[0]}:\n\t{line_array[1]}\n\tCreated On: {line_array[2]}\n\tComplete: {line_array[3]}")

def create_task():
    now_now= datetime.datetime.now()
    time_stamp= f"{now_now.month}/{now_now.day}/{now_now.year}"

    print("\n==Write New Task==\n")
    print(time_stamp)
    current_task_name = input("Task Name: ")
    current_task_desc = input("Task Description: ")
    current_task = Manager(current_task_name, current_task_desc, time_stamp, False)

    current_task.write_task()

def destroy_tasks():
    task_file = open("./todos.txt", 'w')
    task_file.write("")
    print("The file should now be empty. Check it.")
