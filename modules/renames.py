import os
from processors.RFAF import Core as RFAF_Core

class RFAF:
    def __init__(self,oldname,newname):
        self.old = RFAF_Core(oldname,newname).check()[0]
        self.new = RFAF_Core(oldname,newname).check()[1]

    def start(self):
        num = range(0,len(self.old))
        for n in num:
            os.renames(str(self.old[n]),str(self.new[n]))
