import tkinter.messagebox as MessageBox

class MRES:
    def __init__(self,title:str=None,msg:str=None):
        self.title = title
        self.msg = msg
    
    def show(self):#open.project
        self.title = "Result: "
        MessageBox.showerror(self.title,message=self.msg)#@ this send a not found project type error