tasks = []

def show_task():
    if not tasks:
        print("Belum ada task")
    else:
        for i, task in enumerate(tasks):
            print(i+1, task)

def add_task():
    title = input("Masukkan task: ")
    tasks.append({"title": title, "status": "belum"})
    print("Task berhasil ditambahkan!")
