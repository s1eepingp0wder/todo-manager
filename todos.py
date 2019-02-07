import item
import manager
import ast
import datetime

#print(datetime.datetime.now())

def help_screen():
    print("""\nSelect an option.
          Type \"write\" to create a task.
          Type \"help\" to view this help screen.
          Type \"quit\" to exit.
          Type \"destroy\" to kill all tasks.
          Type \"mark\" to mark a task complete.\n""")

print("""
*******************
*   GITTER DONE   *
*                 *
* repl based to-  *
* do list.        *
*******************
""")
help_screen()
manage_option=""
options = ['write', 'help']

while True:
    manage_option= input("Type an action or \"help\". >")

    if manage_option.lower() == "write":
        # Put this in the Manager Module!
        manager.create_task()
    elif manage_option.lower() == "help":
        help_screen()
    elif manage_option.lower() == "list":
        manager.list_all()
    elif manage_option.lower() == "destroy":
        manager.destroy_tasks()
    elif manage_option.lower() == "mark":
        manager.mark_task()
    elif manage_option.lower() == "quit":
        print("""
        *******************
        *   GITTER DONE   *
        *                 *
        *    good bye!    *
        *******************
        """)
        break
        exit(1)
    else:
        print("Unrecognized Command.")
