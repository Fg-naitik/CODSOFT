import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Refresh listbox
def refresh_list():
    task_listbox.delete(0, tk.END)

    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        task_listbox.insert(tk.END, f"{task['task']} {status}")

# Add task
def add_task():
    task = task_entry.get()

    if task:
        tasks.append({
            "task": task,
            "completed": False
        })

        save_tasks()
        refresh_list()
        task_entry.delete(0, tk.END)

    else:
        messagebox.showwarning("Warning", "Enter a task!")

# Delete task
def delete_task():
    try:
        selected = task_listbox.curselection()[0]

        tasks.pop(selected)

        save_tasks()
        refresh_list()

    except:
        messagebox.showwarning("Warning", "Select a task!")

# Mark complete
def complete_task():
    try:
        selected = task_listbox.curselection()[0]

        tasks[selected]["completed"] = True

        save_tasks()
        refresh_list()

    except:
        messagebox.showwarning("Warning", "Select a task!")

# Update task
def update_task():
    try:
        selected = task_listbox.curselection()[0]

        new_task = task_entry.get()

        if new_task:
            tasks[selected]["task"] = new_task

            save_tasks()
            refresh_list()

            task_entry.delete(0, tk.END)

        else:
            messagebox.showwarning("Warning", "Enter new task!")

    except:
        messagebox.showwarning("Warning", "Select a task!")

# Main Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x500")

tasks = load_tasks()

title = tk.Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

task_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 14)
)
task_entry.pack(pady=10)

add_btn = tk.Button(
    root,
    text="Add Task",
    width=20,
    command=add_task
)
add_btn.pack(pady=5)

task_listbox = tk.Listbox(
    root,
    width=50,
    height=12,
    font=("Arial", 12)
)
task_listbox.pack(pady=10)

update_btn = tk.Button(
    root,
    text="Update Task",
    width=20,
    command=update_task
)
update_btn.pack(pady=5)

complete_btn = tk.Button(
    root,
    text="Mark Complete",
    width=20,
    command=complete_task
)
complete_btn.pack(pady=5)

delete_btn = tk.Button(
    root,
    text="Delete Task",
    width=20,
    command=delete_task
)
delete_btn.pack(pady=5)

refresh_list()

root.mainloop()