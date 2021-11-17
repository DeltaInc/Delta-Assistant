import tkinter as tk
import datetime
from modules.main import Main

date = datetime.datetime.now()
time = date.strftime("%H")

if time <= "09" and time >= "1":
    root = tk.Tk()
    root.title("PSA")
    lbl = tk.Label(root,text=f"Now Is {time} and I Can't Help you.I'm Sleeping. you should go and sleep",foreground="red").pack()
    root.mainloop()
else:
    app = tk.Tk()
    app.title("PSA")
    app.geometry('600x250')
    cmd = tk.Text(app,foreground="orange",font=("Consolas",14),background="black")
    cmd.pack(fill='both',side='top',expand=True)
    def run():
        code = str(cmd.get(1.0, tk.END)).split("\n")#@ this is for get the code from cmd
        for c in code:
            Main(c)
        print("Viva Phoenix")
    cmd.bind('<F5>',run)
    app.mainloop()

