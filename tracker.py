class Creature:
  def __init__(self, name, ac, hp, init_bonus, to_hit, attacks, is_caster):
    self.name = name
    self.ac = ac
    self.hp = hp
    self.init_bonus = init_bonus
    self.to_hit = to_hit
    self.attacks = attacks
    self.is_caster = is_caster
  

import tkinter as tk

window = tk.Tk(className = "5e Encounter Tracker")
window.configure(bg = "#474747")
#opens window and sets the background color

frame_head = tk.Frame(master = window, bg = "#474747", relief = tk.RAISED, borderwidth = 2)

header = tk.Label(master = frame_head, text = "Welcome to the 5e Encounter Tracker")

header.pack()
#creates the header label

buttons_frame = tk.Frame(master = window, bg = "#474747")

button1 = tk.Button(master = buttons_frame, text= "Add a Creature")
button2 = tk.Button(master = buttons_frame, text = "Add a Player")
button3 = tk.Button(master = buttons_frame, text = "Save Encounter")
button4 = tk.Button(master = buttons_frame, text = "Load Encounter")
#creates separate frame for buttons, then populates with buttons

button1.grid(row = 1, column = 0)
button2.grid(row = 1, column = 1)
button3.grid(row = 1, column = 2)
button4.grid(row = 1, column = 3)

buttons_frame.grid(row = 1, column = 0, rowspan = 1, columnspan = 5, sticky = "n")
#grids the button frame and buttons

frame_head.grid(row = 0, column = 0, rowspan = 1, columnspan = 5, sticky = "n")

window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)
window.columnconfigure(3, weight = 1)
#grids the header frame and configures column attributes

window.mainloop()
