import tkinter as tk
from tkinter import ttk

def test_function(event):
    print(f"curselection: {event.widget.curselection()}")

root = tk.Tk()
root.title("GUI TEST")

main_frame = ttk.Frame(root)
main_frame.pack(side="top", fill="both", expand=True, padx=10, pady=(5, 5))

listbox = tk.Listbox(main_frame)
listbox.pack(fill="both", side="left", expand=True)
listbox.bind("<<ListboxSelect>>", lambda e: test_function(e))

buttons_frame = ttk.Frame(main_frame)
buttons_frame.pack(side="right", padx=5)

option1 = ttk.Button(buttons_frame, text="Option 1", command= lambda lb=listbox: lb.delete(tk.ANCHOR))
option1.pack(side="top", fill="none")

option2 = ttk.Button(buttons_frame, text="Option 2", command=lambda lb=listbox: test_function(lb))
option2.pack(side="top", fill="none")

option3 = ttk.Button(buttons_frame, text="Option 3")
option3.pack(side="top", fill="none")

scrollbar = ttk.Scrollbar(main_frame, orient="vertical")
scrollbar.config(command=listbox.yview)
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)

#add items

for i in range(1, 15):
    listbox.insert(tk.END, f"Item number {i}")

root.mainloop()