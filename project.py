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
                    print("Tasks Menu\n1. Add Task\n2. Mark Complete\n3. Remove Completed\n4. Exit")
                    task_menu_choice = input("Choice: ")
                    match task_menu_choice:
                        case "1":
                            tasks = add_task(input("Task: "),input("Priority: "),tasks)
                        case "2":
                            tasks[int(input("Task Number: "))-1][2] = "Complete"
                        case "3":
                            tasks = [task for task in tasks if task[2] != "Complete"]
                        case "4":
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
            

def add_task(task,priority,tasks):
    tasks.append(Task(task,priority).to_list())
    return tasks


def complete_task(tasks):
    return tasks



if __name__ == "__main__":
    main()