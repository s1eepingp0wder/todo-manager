import datetime
import item
import random
class Manager(item.Item):
    def __init__(self, task_name, task_description, task_timestamp, task_isfinished):
        item.Item.__init__(self, task_name, task_description, task_timestamp, task_isfinished)

    def write_task(self):
        # new_task= [self.task_name, self.task_description, self.task_timestamp, self.task_isfinished]
        try:
            f = open("./todos.txt", "a+")
            f.write(f"{self.task_name}|{self.task_description}|{self.task_timestamp}|{self.task_isfinished}\n")
            f.close()
            print("Task Written. Type \"list\" to view all tasks.")
        except:
            print("Your to-do list might not be compatible with this version of Gitter Done. Type \"destroy\" to fix your file!")


def list_all():
    try:
        task_file = open("./todos.txt", 'r')
        print("\n==Task List==\n")
        i = 0
        for line in task_file:
            i += 1
            line_array = line.split("|")
            print(f"{i}. {line_array[0]}:\n\t{line_array[1]}\n\tCreated On: {line_array[2]}\n\tComplete: {line_array[3]}\n")
    except:
        print("Your to-do list might not be compatible with this version of Gitter Done. Type \"destroy\" to fix your file!")

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

def mark_task():
    list_all()
    task_list = open('todos.txt','r').readlines()
    try:
        selected_task = int(input("Select a task by number: "))
        with open('./todos.txt', 'w') as output:
            for tasksel, line in enumerate(task_list):
                # Let's rewrite every line otherwise.
                if tasksel != selected_task -1:
                    output.write(line)
                elif tasksel == selected_task-1:
                    line = line.replace("False", "True ✅")
                    output.write(line)
        encouragement = ['Proud of You!', 'Good Job!', 'Keep going!', 'You got this!']
        print(f"Task marked complete. {random.choice(encouragement)}")
    except:
        print("Something went wrong. Perhaps the input was not a number?")
