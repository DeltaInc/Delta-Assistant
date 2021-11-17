import webbrowser as wb
from processors.rtl import Core 

class Main:
    def __init__(self,qoury:str):
        self.qoury = qoury

    def en(self):
        wb.open_new_tab( "https://www.en.wikipedia.com/wiki/" + self.qoury )

    def fa(self):
        wb.open_new_tab( "https://www.fa.wikipedia.com/wiki/" + self.qoury )

    def RTL(self):
        wb.open_new_tab( f"https://www.{Core(self.qoury).check()}.wikipedia.com/wiki/" + self.qoury )