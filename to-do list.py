import tkinter as tk
from tkinter import ttk

tasks = []

def add_task():
    description = description_entry.get()
    due_date = due_date_entry.get()
    priority = priority_var.get()
    task = {
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'completed': False
    }
    tasks.append(task)
    update_task_list()
    clear_entries()

def update_task_list():
    task_listbox.delete(0, tk.END)
    sorted_tasks = sorted(tasks, key=lambda x: x['priority'])
    for task in sorted_tasks:
        status = "Completed" if task['completed'] else "Incomplete"
        task_listbox.insert(tk.END, f"{task['description']} | Due Date: {task['due_date']} | Priority: {task['priority']} | Status: {status}")

def remove_task():
    if not task_listbox.curselection():
        return
    selected_task_index = task_listbox.curselection()[0]
    tasks.pop(selected_task_index)
    update_task_list()

def clear_entries():
    description_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    priority_var.set("Low")

# Create the main application window
app = tk.Tk()
app.title("To-Do List Application")

# Create and configure input fields
input_frame = ttk.Frame(app)
input_frame.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="w")

description_label = ttk.Label(input_frame, text="Description:")
description_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
description_entry = ttk.Entry(input_frame)
description_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

due_date_label = ttk.Label(input_frame, text="Due Date:")
due_date_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
due_date_entry = ttk.Entry(input_frame)
due_date_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

priority_label = ttk.Label(input_frame, text="Priority:")
priority_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
priority_var = tk.StringVar(value="Low")
priority_combobox = ttk.Combobox(input_frame, textvariable=priority_var, values=["Low", "Medium", "High"])
priority_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Create and configure buttons
button_frame = ttk.Frame(app)
button_frame.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

add_button = ttk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

remove_button = ttk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.grid(row=0, column=1, padx=5)

# Create and configure the task list
task_list_label = ttk.Label(app, text="To-Do List:")
task_list_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")
task_listbox = tk.Listbox(app, selectmode=tk.SINGLE, width=50)
task_listbox.grid(row=3, column=0, pady=10, padx=10, sticky="w")

# Create a scrollbar for the task list
scrollbar = tk.Scrollbar(app, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.grid(row=3, column=1, pady=10)
task_listbox.config(yscrollcommand=scrollbar.set)

update_task_list()

# Start the GUI application
app.mainloop()
