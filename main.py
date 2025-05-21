import tkinter as tk
from app.logic import TaskManager

# Create window
win = tk.Tk()
win.title("Task Manager")
win.geometry("500x450+500+200")
win.resizable(width=0, height=0)

# Logic manager instance
manager = TaskManager()

# 🔁 Refresh listbox with current tasks
def refresh_listbox():
    listbox.delete(0, tk.END)
    for task in manager.get_tasks():
        listbox.insert(tk.END, task)

# ➕ Add task to manager
def add_task():
    task = entry.get().strip()
    if task:
        manager.add_task(task)
        entry.delete(0, tk.END)
        refresh_listbox()

# ➖ Remove selected task
def remove_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        manager.remove_task(index)
        refresh_listbox()

# 🗑 Clear all tasks
def clear_tasks():
    manager.clear_all()
    refresh_listbox()

# ⛔ Save and close
def on_close():
    manager.save()
    win.destroy()

# 🧱 GUI Layout
main_frame = tk.Frame(win, background="gray")
main_frame.pack(fill="both", padx=20, pady=20)

entry = tk.Entry(master=main_frame)
entry.pack(fill="both", padx=10, pady=10)

btn_frame = tk.Frame(master=main_frame, background="white")
btn_frame.pack()

add = tk.Button(btn_frame, text="ADD", width=10, command=add_task)
remove = tk.Button(btn_frame, text="REMOVE", width=10, command=remove_task)
clear = tk.Button(btn_frame, text="CLEAR", width=10, command=clear_tasks)

add.grid(row=0, column=0, padx=10, pady=10)
remove.grid(row=0, column=1, padx=10, pady=10)
clear.grid(row=0, column=2, padx=10, pady=10)

# Optional: center frame itself
btn_frame.pack(anchor="center")


listbox = tk.Listbox(master=main_frame)
listbox.pack(fill="both", expand=True, padx=10, pady=10)

# 🔄 Load tasks on startup
refresh_listbox()

# 💾 Auto-save on close
win.protocol("WM_DELETE_WINDOW", on_close)

# 🚀 Start GUI loop
win.mainloop()
