from tkinter import *
from tkinter import ttk

# initializing the GUI

root = Tk()
root.title("Simple Base to Base Converter")

# making main frame

main_frame = ttk.Frame(root, width=1000, height=500, padding="12 12 12 12")
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

# combo boxes for base conversion options

base_start = StringVar()
base_end = StringVar()

start_bases = ttk.Combobox(main_frame, state="readonly", width="5", textvariable=base_start)
end_bases = ttk.Combobox(main_frame, state="readonly", width="5", textvariable=base_end)
start_bases.grid(column=2, row=1, sticky=(N, W))
end_bases.grid(column=2, row=2, sticky=(N, W))

start_bases["values"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
end_bases["values"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")

# entry for input
user_input = StringVar()

number_input = ttk.Entry(main_frame, width=50, textvariable=user_input)
number_input.grid(column=1, row=4, columnspan=3, pady=5, sticky=(W, E))

# labels

ttk.Label(main_frame, text="Starting Base: ").grid(column=1, row=1, sticky=S)
ttk.Label(main_frame, text="Ending Base: ").grid(column=1, row=2, sticky=S)
ttk.Label(main_frame, text="Input").grid(column=2, row=3, sticky=(N, W))
ttk.Label(main_frame, text="Result").grid(column=2, row=5, sticky=(N, W))
root.mainloop()
