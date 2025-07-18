import tkinter as tk
from tkinter import messagebox, ttk
import threading
import time
from datetime import datetime
import winsound

# Function to play notification sound
def play_sound():
    # Beep multiple times for better effect
    for _ in range(3):
        winsound.Beep(1200, 500)  # frequency, duration
        time.sleep(0.2)

# Background reminder checker
def reminder_checker(task, remind_time):
    while True:
        now = datetime.now().strftime("%I:%M %p")
        if now == remind_time:
            play_sound()
            messagebox.showinfo("🔔 Reminder", f"Time to: {task}")
            break
        time.sleep(30)

# Reminder function
def set_reminder():
    task = entry_task.get()
    hour = entry_hour.get()
    minute = entry_minute.get()
    am_pm = combo_am_pm.get()

    if not task or not hour or not minute or not am_pm:
        messagebox.showwarning("⚠️ Missing Info", "Please fill all fields.")
        return

    try:
        hour = int(hour)
        minute = int(minute)
        if not (1 <= hour <= 12 and 0 <= minute <= 59):
            raise ValueError
        remind_time = f"{hour:02d}:{minute:02d} {am_pm}"
        datetime.strptime(remind_time, "%I:%M %p")  # Validate format
    except ValueError:
        messagebox.showerror("⛔ Invalid Time", "Enter valid hour (1-12) and minute (00-59).")
        return

    threading.Thread(target=reminder_checker, args=(task, remind_time), daemon=True).start()
    messagebox.showinfo("✅ Reminder Set", f"Reminder set for '{task}' at {remind_time}!")

# GUI setup
root = tk.Tk()
root.title("🖥️ Desktop Reminder App")
root.geometry("400x300")
root.resizable(False, False)

# Task input
tk.Label(root, text="📝 Task/Reminder:", font=("Arial", 10)).pack(pady=5)
entry_task = tk.Entry(root, width=40, font=("Arial", 10))
entry_task.pack(pady=5)

# Time input 
frame_time = tk.Frame(root)
frame_time.pack(pady=10)

tk.Label(frame_time, text="Hour:", font=("Arial", 10)).grid(row=0, column=0, padx=10)
entry_hour = tk.Entry(frame_time, width=5, font=("Arial", 10))
entry_hour.grid(row=0, column=1)

tk.Label(frame_time, text="Minute:", font=("Arial", 10)).grid(row=0, column=2, padx=10)
entry_minute = tk.Entry(frame_time, width=5, font=("Arial", 10))
entry_minute.grid(row=0, column=3)

# AM/PM dropdown 
tk.Label(root, text="🕓 AM / PM:", font=("Arial", 10)).pack()
combo_am_pm = ttk.Combobox(root, values=["AM", "PM"], width=10, font=("Arial", 10))
combo_am_pm.set("AM")
combo_am_pm.pack(pady=5)

tk.Button(root, text="Set Reminder", command=set_reminder, bg="#4CAF50", fg="white", font=("Arial", 10)).pack(pady=20)

root.mainloop()
