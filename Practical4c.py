class Task:
    def __init__(self, task):
        self.task = task
        self.next = None


class ToDoList:
    def __init__(self):
        self.head = None

    # Add a task at the end
    def add_task(self, task):
        new_task = Task(task)

        if self.head is None:
            self.head = new_task
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_task

    # Display all tasks
    def show_tasks(self):
        if self.head is None:
            print("To-Do List is empty")
            return

        current = self.head
        while current is not None:
            print("-", current.task)
            current = current.next

    # Complete and remove a task
    def complete_task(self, task):
        current = self.head
        previous = None

        while current is not None:
            if current.task.lower() == task.lower():
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                print("Completed:", current.task)
                return

            previous = current
            current = current.next

        print("Task not found")


# Main program
todo = ToDoList()

todo.add_task("Study Python")
todo.add_task("Complete assignment")
todo.add_task("Go for a walk")

print("To-Do List:")
todo.show_tasks()

print("\nCompleting a task:")
todo.complete_task("Complete assignment")

print("\nUpdated To-Do List:")
todo.show_tasks()