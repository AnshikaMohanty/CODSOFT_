import tkinter as tk
from tkinter import messagebox, simpledialog

# Create the main window
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x500")
root.configure(bg="#F7F7F7")

tasks = []

# Functions
def update_listbox():
    listbox.delete(0, tk.END)
    for index, task in enumerate(tasks):
        status = "✓" if task["done"] else "⏳"
        listbox.insert(tk.END, f"{status} {task['title']}")

def add_task():
    task_title = entry.get().strip()
    if task_title:
        tasks.append({"title": task_title, "done": False})
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True
        update_listbox()
    else:
        messagebox.showinfo("Select Task", "Please select a task to mark as done.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        deleted_task = tasks.pop(index)
        update_listbox()
    else:
        messagebox.showinfo("Select Task", "Please select a task to delete.")

# UI Components
title = tk.Label(root, text="My To-Do List", font=("Helvetica", 20, "bold"), bg="#F7F7F7", fg="#333")
title.pack(pady=10)

entry_frame = tk.Frame(root, bg="#F7F7F7")
entry_frame.pack(pady=5)

entry = tk.Entry(entry_frame, width=25, font=("Helvetica", 14))
entry.pack(side=tk.LEFT, padx=(10, 5), pady=10)

add_btn = tk.Button(entry_frame, text="Add", width=8, bg="#4CAF50", fg="white", font=("Helvetica", 12), command=add_task)
add_btn.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=40, height=15, font=("Helvetica", 12), selectbackground="#ADD8E6")
listbox.pack(pady=10)

btn_frame = tk.Frame(root, bg="#F7F7F7")
btn_frame.pack(pady=5)

done_btn = tk.Button(btn_frame, text="Mark as Done", width=15, bg="#2196F3", fg="white", font=("Helvetica", 12), command=mark_done)
done_btn.pack(side=tk.LEFT, padx=10)

delete_btn = tk.Button(btn_frame, text="Delete Task", width=15, bg="#F44336", fg="white", font=("Helvetica", 12), command=delete_task)
delete_btn.pack(side=tk.LEFT)

# Run the main loop
root.mainloop()
