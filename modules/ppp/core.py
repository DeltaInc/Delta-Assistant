import pdf2image
from modules.messagebox.info.math import MRES

class PPP:
    def __init__(self,Pdf_File_Path):
        self.Pdf_File_Path = Pdf_File_Path

    def Start(self):
        self.Images =  pdf2image.convert_from_path(self.Pdf_File_Path.replace("\\","/"))
        for image in self.Images:
            self.Images[image].save('page_'+ str(image) +'.jpg', 'JPEG')
        MRES("finish","finish this work").show()
        