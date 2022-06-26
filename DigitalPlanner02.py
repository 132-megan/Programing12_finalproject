import tkinter as tk
from tkinter import ttk
from tkinter import Menu


root = tk.Tk()
root.geometry("700x500")
root.title("MyProductivity")

root.columnconfigure(1, minsize=700)

header = tk.Frame(root)
header.grid(column=1,row=0)
header.columnconfigure(1, minsize=20)

##creates the labels at the top of the screen
sunday = tk.Label(header, text="Sunday").grid(column=2, row=0)
monday = tk.Label(header, text="Monday").grid(column=3, row=0)
tuesday = tk.Label(header, text= "Tuesday").grid(column=4, row=0)
wednesday = tk.Label(header, text="Wednesday").grid(column=5, row=0)
thursday = tk.Label(header, text="Thursday").grid(column=6, row=0)
friday = tk.Label(header, text="Friday").grid(column=7, row=0)
saturday = tk.Label(header, text="Saturday").grid(column=8, row=0)

calendar = tk.Frame (root)
calendar.grid(column=1, columnspan=10, row=1)

canvas1=tk.Canvas(calendar)

scrollbar = ttk.Scrollbar (calendar, orient="vertical", command=canvas1.yview)
scrollable_frame=tk.Frame(canvas1)

##this defines the scrollable regions so you can't scroll off into nothingness
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas1.configure(
        scrollregion=canvas1.bbox("all")
        )
    )

canvas1.create_window((0,0), window=scrollable_frame, anchor="nw")
canvas1.configure(yscrollcommand=scrollbar.set)
##oriending the canvas and the scroll bar within the calendar frame
canvas1.grid(column=1, row=1)
scrollbar.grid(column=2, row=1, sticky=tk.NS)

##creates the dashes and the times along the side
ttk.Label(scrollable_frame, text="-----").grid(column=0)
for i in range (6, 12):
    ttk.Label(scrollable_frame, text="{:2} AM".format(i)).grid(column=0)
    ttk.Label(scrollable_frame, text="-----").grid(column=0)   
ttk.Label(scrollable_frame, text="12 PM").grid(column=0)
ttk.Label(scrollable_frame, text="-----").grid(column=0)
for i in range (1, 10):
    ttk.Label(scrollable_frame, text="{:2} PM".format(i)).grid(column=0)
    ttk.Label(scrollable_frame, text="-----").grid(column=0)

##creates all the editable text boxes
for x in range (1,8):
    for y in range (1, 17):
        tk.Text(scrollable_frame, height=1, width=5).grid(column=x, row=(y*2)-1)


root.mainloop()
