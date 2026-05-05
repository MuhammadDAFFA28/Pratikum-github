tasks = []

def show_task():
    if not tasks:
        print("Belum ada task")
    else:
        for i, task in enumerate(tasks):
            print(i+1, task)
