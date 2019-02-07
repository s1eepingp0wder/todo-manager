import item
import manager

def helpScreen():
    print("""\nSelect an option.
          You can type \"Write\" to write.\n""")

manage_option=""
options = ['write', 'help']

while True:
    manage_option= input("Type an action or \"help\". ")

    if manage_option.lower() == "write":
        # Let's not learn to run before we learn to walk. We can always clear the file.
        # eval is a thing...?
            print("Register a dream car\n")
            current_task_name = input("Task Name: ")
            current_task_desc = input("Task Description: ")
        current_task = manager.Manager(current_task_name, current_task_desc)
        current_task.write_task()
    elif manage_option.lower() == "help":
        helpScreen()
    elif manage_option.lower() == "write":
        
    elif manage_option.lower() == "quit":
        break
        exit(1)
    else:
        print("Unrecognized Command.")
