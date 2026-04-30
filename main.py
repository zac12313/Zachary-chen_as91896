import tkinter as tk
root= tk.Tk()
label=tk.Label(root, text="bomboclatt quiz", width=67,bg="red",font="arial",).grid(row=0, column=5)


tk.Label(root, text="First Name").grid(row=6, column=10)
tk.Label(root, text="Last Name").grid(row=7, column=10)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=6, column=10)
entry2.grid(row=7, column=10)

root.title("Gym quiz")

button = tk.Button(root,text="Exit", width=12,command=root.destroy).grid(row=0)






root.mainloop()