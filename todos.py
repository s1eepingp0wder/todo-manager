import item
import manager

def helpScreen():
    print("""Select an option.
          You can type \"Write\" to write.""")

manage_option=""
options = ['write', 'help']

while True:
    manage_option= input("Type an action or \"help\". ")

    if manage_option.lower() == "write":
        print ("Getting there.")
    elif manage_option.lower() == "help":
        helpScreen()
    elif manage_option.lower() == "quit":
        break
        exit(1)
    else:
        print("Unrecognized Command.")
