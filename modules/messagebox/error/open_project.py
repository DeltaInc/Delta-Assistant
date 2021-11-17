import tkinter.messagebox as MessageBox

class OPRO:
    def __init__(self,title:str=None,msg:str=None):
        self.title = title
        self.msg = msg
    
    def show(self):#open.project
        self.title = "Not Found!"
        self.msg = "I don't Now You have project folder with this language.If Not This You Can Try Again"
        MessageBox.showerror(self.title,message=self.msg)#@ this send a not found project type error