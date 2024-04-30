import tkinter as tk

class TimeManagementMatrixApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Time Management Matrix")
    
        self.quadrant_frames = []
        for i in range(4):
            frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=2)
            frame.grid(row=i//2, column=i%2, padx=5, pady=5, sticky="nsew")
            self.quadrant_frames.append(frame)
            
        labels = ["Important/Urgent", "Important/Not Urgent", "Not Important/Urgent", "Not Important/Not Urgent"]
        self.todo_lists = []
        self.new_task_entries = []
        self.add_task_buttons = []
        self.delete_task_buttons = []
        for i, label_text in enumerate(labels):
            label = tk.Label(self.quadrant_frames[i], text=label_text, font=("Arial", 12, "bold"))
            label.pack(pady=5)
            todo_list = tk.Listbox(self.quadrant_frames[i], height=8, width=30, selectmode=tk.SINGLE)
            todo_list.pack(padx=5, pady=5)
            todo_list.bind("<Double-Button-1>", lambda event, idx=i: self.toggle_task_completion(event, idx))
            self.todo_lists.append(todo_list)

            new_task_entry = tk.Entry(self.quadrant_frames[i], width=20)
            new_task_entry.pack(padx=5, pady=5)
            self.new_task_entries.append(new_task_entry)
            add_task_button = tk.Button(self.quadrant_frames[i], text="Add Task",
                                        command=lambda idx=i: self.add_task(idx))
            add_task_button.pack(pady=5)
            self.add_task_buttons.append(add_task_button)

            delete_task_button = tk.Button(self.quadrant_frames[i], text="Delete Task",
                                           command=lambda idx=i: self.delete_task(idx))
            delete_task_button.pack(pady=5)
            self.delete_task_buttons.append(delete_task_button)

    def add_task(self, quadrant_idx):
        new_task = self.new_task_entries[quadrant_idx].get()
        if new_task:
            self.todo_lists[quadrant_idx].insert(tk.END, new_task)
            self.new_task_entries[quadrant_idx].delete(0, tk.END)

    def toggle_task_completion(self, event, quadrant_idx):
        task_index = self.todo_lists[quadrant_idx].nearest(event.y)
        if task_index != -1:
            current_state = self.todo_lists[quadrant_idx].itemcget(task_index, "foreground")
            new_state = "gray" if current_state == "black" else "black"
            self.todo_lists[quadrant_idx].itemconfig(task_index, foreground=new_state)

    def delete_task(self, quadrant_idx):
        selected_index = self.todo_lists[quadrant_idx].curselection()
        if selected_index:
            self.todo_lists[quadrant_idx].delete(selected_index)

if __name__ == "__main__":
    app = TimeManagementMatrixApp()
    app.mainloop()
