class GFNFP():
    def __init__(self,Path:str):
        self._Path = Path
        self.Result = ""

    def __Get_Name(self):
        self.Result = self._Path.split("/")[len(self._Path.split("/"))-1].replace
        