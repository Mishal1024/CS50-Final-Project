from tabulate import tabulate
import json


class Task():
    def __init__(self,task,priority):
        self.task = task
        self.priority = priority
        self.done = "Incomplete"
    
    def to_list(self):
        return [self.task,self.priority,self.done]
    

try:
    with open("data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {
        "task":[],
        "habit":[],
        "note":[],
        "log":[]
    }


def main():
    while True:
        print("Menu\n1. Tasks\n2. Habits\n3. Notes\n4. Focus Sessions\n5. Stats\n6. Exit")
        main_menu_choice = input("Choice: ")
        print()
        match main_menu_choice:
            case "1":
                tasks = data["task"]
                while True:
                    print(tabulate(tasks,headers =["Task","Priority","Completion"],tablefmt="grid"))
                    print()
                    print("Tasks Menu\n1. Add Task\n2. Mark Complete\n3. Mark Incomplete\n4. Remove Completed\n5. Exit")
                    task_menu_choice = input("Choice: ")
                    match task_menu_choice:
                        case "1":
                            add_task(tasks)
                        case "2":
                            mark_task(int(input("Task Number: ")),tasks)
                        case "3":
                            unmark_task(int(input("Task Number: ")),tasks)
                        case "4":
                            tasks = remove_marked(tasks)
                        case "5":
                            print()
                            break
                        case _:
                            print("Invalid Input")
                    print()
                    data["task"] = tasks
            case "2":
                print("Habits")
            case "3":
                print("Notes")
            case "4":
                print("Focus")
            case "5":
                print("stats")
            case "6":
                break
            case _:
                print("Invalid Input")
                pass
    with open("data.json", "w") as file:
        json.dump(data,file,indent=4)
        file.close()


def add_task(tasks):
    tasks.append(Task(input("Task: "),input("Priority: ")).to_list())

def mark_task(i,tasks):
    tasks[i-1][2] = "Complete"

def unmark_task(i,tasks):
    tasks[i-1][2] = "Incomplete"

def remove_marked(tasks):
    return [task for task in tasks if task[2] != "Complete"]



if __name__ == "__main__":
    main()