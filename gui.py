import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("600x400")
window.resizable(0,0)
window.title("Mapping Space Trash in Real Time")
ico = tk.PhotoImage(file = 'sat.png')
window.iconphoto(False, ico)

satimg = Image.open("sat.png")
test = ImageTk.PhotoImage(satimg)
lab1 = tk.Label(image=test)
lab1.image = test
lab1.place(x=250, y= 45)

lab2 = tk.Label(window, text='Year').place(x=160, y=180)
lab3 = tk.Label(window, text='Month').place(x=285, y=180)
lab4 = tk.Label(window, text='Day').place(x=410, y=180)

e1 = tk.Entry(window).place(x=150, y=200, width=60, height=20)
e2 = tk.Entry(window).place(x=275, y=200, width=60, height=20)
e3 = tk.Entry(window).place(x=400, y=200, width=60, height=20)

satelites = [
    "COSMOS", 
    "FENGYUN", 
    "IRIDIUM33", 
    "MICROSAT"
    ]

satelite = tk.StringVar(window)
satelite.set(satelites[0])
sat_menu = tk.OptionMenu(window, satelite, *satelites)
sat_menu.place(x=255, y=250, width=100)

tk.Button(window, text = "Map", width=10, bg='#25387d', fg='white').place(x=265,y=300)

window.mainloop()