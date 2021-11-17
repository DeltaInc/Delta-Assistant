import webbrowser as wb

class Main:
    def __init__(self,qoury:str):
        self.qoury = qoury

    def search(self):
        wb.open_new_tab( "https://www.google.com/search?q=" + self.qoury )

