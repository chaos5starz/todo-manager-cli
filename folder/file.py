x = {}

while True:
    command = input("> ").strip()
    part = command.split()

    if not part:
        continue

    action = part[0]

    if action == "add":
        if len(part) < 2:
            print("please provide a task name\n")
            continue
        task = part[1]
        if task in x:   # 🔥 duplicate protection
            print(f"task {task} already exists")
        else:
            x[task] = "pending"
            print(f"task {task} added.")

    elif action == "done":
        if len(part) < 2:
            print("please provide a task name to mark as done")
            continue
        task = part[1]
        if task in x:
            x[task] = "done"
            print(f"task {task} marked as done")
        else:
            print(f"task {task} not found")

    elif action == "remove":
        if len(part) < 2:
            print("please provide a task name to remove")
            continue
        task = part[1]
        if task in x:
            del x[task]
            print(f"task {task} removed")
        else:
            print(f"task {task} not found")

    elif action == "show":
        if not x:
            print("no tasks yet")
        else:
            for task, status in x.items():
                print(f"{task}: {status}")

    elif action == "quit":
        break

    else:
        print("unknown command")
