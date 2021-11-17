import webbrowser as wb

class Main:
    def __init__(self,qoury:str):
        self.qoury = qoury

    def search(self):
        wb.open_new_tab( "https://www.bing.com/search?q=" + self.qoury )

