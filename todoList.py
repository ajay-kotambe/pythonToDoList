import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_frame = tk.Frame(root)
        self.task_frame.pack()

        self.task_entry = tk.Entry(self.task_frame)
        self.task_entry.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.task_frame, text="Add", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.task_list = tk.Listbox(root)
        self.task_list.pack()

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.task_list.delete(index)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
