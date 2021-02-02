import tkinter as tk

window = tk.Tk(className = "5e Encounter Tracker")
window.configure(bg = "#474747")

frame_head = tk.Frame(master = window, bg = "#474747", relief = tk.RAISED, borderwidth = 2)

header = tk.Label(master = frame_head, text = "Welcome to the 5e Encounter Tracker")

header.pack()

button1 = tk.Button(text= "Add a Creature")
button2 = tk.Button(text = "Add a Player")
button3 = tk.Button(text = "Save Encounter")
button4 = tk.Button(text = "Load Encounter")

button1.grid(row = 1, column = 0)
button2.grid(row = 1, column = 1)
button3.grid(row = 1, column = 2)
button4.grid(row = 1, column = 3)

frame_head.grid(row = 0, column = 0, rowspan = 1, columnspan = 5)

window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)
window.columnconfigure(3, weight = 1)

window.mainloop()
