from modules.messagebox.info.math import MRES

class CUA:#check url address
    def __init__(self,url:str):
        self.Url = url
    
    def check(self):
        if self.Url.startswith("https://") or self.Url.startswith("http://") or self.Url.startswith("www."):
            return self.Url
        else:
            MRES("I Think Your Url Is Not Valid But I Run And Show This Url.Please Wait For See The Result")
            # important : you should not change thissssss.but you can't read Doc.txt file.if see problem in 
            # Doc.txt, write under this line(start your note with #!)
            