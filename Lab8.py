import tkinter as tk
import sqlite3

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Приложение для задач")

        self.setup_database()

        self.create_widgets()
        self.refresh_tasks()

    def setup_database(self):
        self.conn = sqlite3.connect('tasks.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, completed INTEGER)''')

    def create_widgets(self):
        self.task_list = tk.Listbox(self.root, height=15, width=50, font=("Helvetica", 12))
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH)

        self.task_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.task_entry.pack(side=tk.BOTTOM, fill=tk.BOTH)

        buttons = [("Добавить задачу", self.add_task), ("Удалить задачу", self.delete_task), ("Завершить задачу", self.complete_task)]
        for text, command in buttons:
            button = tk.Button(self.root, text=text, command=command)
            button.pack(side=tk.BOTTOM)

    def refresh_tasks(self):
        self.task_list.delete(0, tk.END)
        for row in self.c.execute('SELECT * FROM tasks'):
            task_text = '✓ ' + row[1] if row[2] == 1 else row[1]
            self.task_list.insert(tk.END, task_text)

    def add_task(self):
        task = self.task_entry.get()
        self.c.execute('INSERT INTO tasks (task, completed) VALUES (?, ?)', (task, 0))
        self.conn.commit()
        self.task_entry.delete(0, tk.END)
        self.refresh_tasks()

    def delete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task_text = self.task_list.get(selected_task)
            self.c.execute('DELETE FROM tasks WHERE task=?', (task_text,))
            self.conn.commit()
            self.refresh_tasks()

    def complete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task_text = self.task_list.get(selected_task)
            if '✓' not in task_text:
                updated_task = '✓ ' + task_text
                self.c.execute('UPDATE tasks SET task=? WHERE task=?', (updated_task, task_text))
                self.conn.commit()
                self.refresh_tasks()


root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
