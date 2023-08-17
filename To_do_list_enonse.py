todo_list = []
kontinye = True

def add_task(task):
    todo_list.append(task)
    print()

def display_tasks():
    for index in range(len(todo_list)):
        print(f"{index+1}- {todo_list[index]}")
    print()

def mark_task_done(n):
    try:
        todo_list.pop(n-1)
    except IndexError:
        print("Pa gen tach ki gen nimewo sa")
    except:
        print("Sa ou ekri a pa bon")
    print()
    if todo_list == []:
        print("Lis tach ou a vid")
    print()

def save_tasks():
    s_tasks = open("tasks.txt", "w")
    s_tasks.close()
    for t in todo_list:
        s_tasks = open("tasks.txt", "a")
        s_tasks.write(t+"\n")
    s_tasks.close()

def load_tasks():
    task_to_load = None
    try:
        file = input("Antre non fichye a ak tout ekstansyon l 'fichye.txt' : ")
        task_to_load = open(file, "r")
        for line in task_to_load:
            todo_list.append(line)
    except:
        print("\nFichye sa pa egziste")
    print()

while kontinye:
    print("  ==========Meni===========")
    print("|| 1. Ajoute tach          ||") 
    print("|| 2. Afiche tach yo       ||")
    print("|| 3. Fini yon tach        ||") 
    print("|| 4. Anrejistre epi fèmen ||")
    print("  ========================= ")

    choice = input("Chwazi yon opsyon: ")
    while choice not in ['1', '2', '3', '4']:
        choice = input("Chwazi yon opsyon soti nan 1 pou rive nan 4: ")
    
    if choice == "1":
        entery_mode = input("Tape \"T\" pou w tape tach ou yo oubyen \"L\" pour televèse yon fichye tèks ki gen tach yo: ").upper()
        while not (entery_mode == "T" or entery_mode == "L"):
            entery_mode = input("Tape \"T\" pou w tape tach ou yo oubyen \"L\" pour televèse yon fichye tèks ki gen tach yo: ").upper()
        if entery_mode == "T":
            add = input("Ekri tach la: ")
            add_task(add)
        else:
            load_tasks()
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        nimewo_tach = input("Ki nimewo tach ou fini an: ")
        while not nimewo_tach.isdigit():
            nimewo_tach = input("Ki nimewo tach ou fini an: ")
        nimewo_tach = int(nimewo_tach)
        mark_task_done(nimewo_tach)
    else:
        save_tasks()
        print("  ===========  ")
        print("||  Babay\U0001f44b  ||")
        print("  ===========  ")
        break