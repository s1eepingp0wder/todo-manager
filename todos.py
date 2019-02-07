import item
import manager
import ast
import datetime

#print(datetime.datetime.now())

def help_screen():
    print("""\nSelect an option.
          Type \"write\" to create a task.
          Type \"help\" to view this help screen.
          Type \"quit\" to exit.\n
          Type \"destroy\" to kill all tasks.""")

def list_all():
    pass

help_screen()
manage_option=""
options = ['write', 'help']

while True:
    manage_option= input("Type an action or \"help\". >")

    if manage_option.lower() == "write":
        # Let's not learn to run before we learn to walk. We can always clear the file.
        # eval is a thing...?
        now_now= datetime.datetime.now()
        time_stamp= f"{now_now.month}/{now_now.day}/{now_now.year}"
        print("\n==Write New Task==\n")
        print(time_stamp)
        current_task_name = input("Task Name: ")
        current_task_desc = input("Task Description: ")
        current_task = manager.Manager(current_task_name, current_task_desc, time_stamp, False)
        current_task.write_task()
    elif manage_option.lower() == "help":
        help_screen()
    elif manage_option.lower() == "list":
        pass
    elif manage_option.lower() == "destroy":
        pass
    elif manage_option.lower() == "quit":
        break
        exit(1)
    else:
        print("Unrecognized Command.")
