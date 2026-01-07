class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority  

    def __str__(self):
        return f"[Priority {self.priority}] {self.name}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority):
        task = Task(name, priority)
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: x.priority)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False

def print_menu():
    print("\nTask Tracker")
    print("1. Add task")
    print("2. List tasks")
    print("3. Remove task")
    print("4. Exit")

def main():
    manager = TaskManager()
    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter task name: ").strip()
            if not name:
                print("Task name cannot be empty.")
                continue
            priority = input("Enter priority (1-5): ").strip()
            if not priority:
                print("Priority cannot be empty.")
                continue
            manager.add_task(name, priority)
            print("Task added.")

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            manager.list_tasks()
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if manager.remove_task(index):
                    print("Task removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()