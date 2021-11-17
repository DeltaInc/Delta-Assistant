class Core:
    def __init__(self,qoury):
        self.qoury = qoury
        self.langs = ["ابپتثجچهخدذرزژسشصضطظعغفقکگلمنوهی","abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        self.langs_index = {"0":"fa","1":"en"}
        self.en = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    def check(self):
        self.lang:str
        for lang in self.langs:
            for alph in lang:
                self.al = list(alph)
                if self.al in self.qoury:
                    self.lang = self.langs_index.get(self.langs.index(alph))
                    break
                else:
                    self.lang = "None"
        return self.lang