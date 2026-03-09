import tkinter as tk
import queue

class Overlay:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("AI Assistant")

        self.root.geometry("420x220+1100+100")

        self.root.attributes("-topmost", True)

        self.root.configure(bg="#121212")

        self.label = tk.Label(
            self.root,
            text="Waiting...",
            wraplength=380,
            justify="left",
            font=("Consolas", 12),
            bg="#121212",
            fg="#00FF9C"
        )

        self.label.pack(padx=15, pady=15)

        self.queue = queue.Queue()

        self.root.after(100, self.process_queue)

    def process_queue(self):

        while not self.queue.empty():

            text = self.queue.get()

            self.label.config(text=text)

        self.root.after(100, self.process_queue)

    def update(self, text):

        self.queue.put(text)

    def run(self):

        self.root.mainloop()