# These are only here so I have these snippets!
    task_file = open("./todos.txt", 'r')
    print("Task List:")
    i = 0
    for line in task_file:
        i += 1
        line_array = line.split(",")
        print(f"{i}. {line_array[0]}")
    selected_task = int(input("Select a task number: "))-1
    print (selected_task)
    # print(f"Selected task number {selected_task}.")
    # task_file = open('./todos.txt', 'r').readlines()
    # with open('./todos.txt', 'r') as output:
    #     for index,line in enumerate(task_file):
    #         if index != selected_task:
    #             output.write(line)
    task_read = str(open('./todos.txt', 'r').readlines(selected_task)).strip("[]'\\n")
    print(task_read)
    task_read= task_read.replace('False', 'True')
    task_write = open('./todos.txt', 'w')
    task_write.write(task_read)
    task_write.close()
