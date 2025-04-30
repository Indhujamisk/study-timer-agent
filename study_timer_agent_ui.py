<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox
import time
import threading

class StudyTimerAgent:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Study Timer Agent")
        self.root.geometry("350x200")
        self.root.resizable(False, False)

        # Agent label
        self.label = tk.Label(root, text="👋 Welcome to your Study Agent", font=("Arial", 14))
        self.label.pack(pady=10)

        # Timer display
        self.timer_display = tk.Label(root, text="1:00", font=("Arial", 36), fg="green")
        self.timer_display.pack()

        # Start and Stop buttons
        self.start_button = tk.Button(root, text="▶️ Start 1-min Timer", command=self.start_timer, bg="green", fg="white")
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="⏹️ Stop Timer", command=self.stop_timer, bg="red", fg="white")
        self.stop_button.pack(pady=5)

        # Timer thread
        self.running = False
        self.remaining_seconds = 1 * 60  # 25 minutes

    def start_timer(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.run_timer).start()

    def stop_timer(self):
        self.running = False
        self.timer_display.config(text="1:00")
        self.remaining_seconds = 1 * 60

    def run_timer(self):
        while self.remaining_seconds > 0 and self.running:
            mins, secs = divmod(self.remaining_seconds, 60)
            self.timer_display.config(text=f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            self.remaining_seconds -= 1

        if self.remaining_seconds == 0:
            self.running = False
            self.timer_display.config(text="00:00")
            messagebox.showinfo("Time's up!", "⏰ Great job! Take a break.")
            self.remaining_seconds = 1 * 60  # Reset for next round

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTimerAgent(root)
    root.mainloop()
=======
import tkinter as tk
from tkinter import messagebox
import time
import threading

class StudyTimerAgent:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Study Timer Agent")
        self.root.geometry("350x200")
        self.root.resizable(False, False)

        # Agent label
        self.label = tk.Label(root, text="👋 Welcome to your Study Agent", font=("Arial", 14))
        self.label.pack(pady=10)

        # Timer display
        self.timer_display = tk.Label(root, text="1:00", font=("Arial", 36), fg="green")
        self.timer_display.pack()

        # Start and Stop buttons
        self.start_button = tk.Button(root, text="▶️ Start 1-min Timer", command=self.start_timer, bg="green", fg="white")
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="⏹️ Stop Timer", command=self.stop_timer, bg="red", fg="white")
        self.stop_button.pack(pady=5)

        # Timer thread
        self.running = False
        self.remaining_seconds = 1 * 60  # 25 minutes

    def start_timer(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.run_timer).start()

    def stop_timer(self):
        self.running = False
        self.timer_display.config(text="1:00")
        self.remaining_seconds = 1 * 60

    def run_timer(self):
        while self.remaining_seconds > 0 and self.running:
            mins, secs = divmod(self.remaining_seconds, 60)
            self.timer_display.config(text=f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            self.remaining_seconds -= 1

        if self.remaining_seconds == 0:
            self.running = False
            self.timer_display.config(text="00:00")
            messagebox.showinfo("Time's up!", "⏰ Great job! Take a break.")
            self.remaining_seconds = 1 * 60  # Reset for next round

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTimerAgent(root)
    root.mainloop()
>>>>>>> deae955 (Initial commit)
