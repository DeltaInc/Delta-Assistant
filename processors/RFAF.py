class Core:
    def __init__(self,old,new):
        self.new = new
        self.old = old

    def check(self):
        if len(self.old.split('&')) < 2:
            self.old = self.old.split('&')

        else:
            self.old = self.old.split('&')

        if len(self.new.split('&')) < 2:
            self.new = self.new.split('&')

        else:
            self.new = self.new.split('&')

        return [self.old,self.new]
