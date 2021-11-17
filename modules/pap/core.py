import speech_recognition as sr
from modules.messagebox.info.math import MRES

class PAP:#@Phoenix Audio Processors
    def __init__(self,File_Path,EndFile_Path,Lang):#@adr_file@to@adr_endfile@lang
        self.File_Path = File_Path
        self.EndFile_Path = EndFile_Path
        self.Lang = Lang
        self.Result:object

    def Start(self):
        __class__.__Start_Process()
        __class__.__WRIF()
        __class__.__Finish_Process()

    def __Start_Process(self):
        print("start!")
        self.Recognizer = sr.Recognizer()
        self.Audio_file = sr.AudioFile(str(self.File_Path))
        with self.Audio_file as Source:
            self.Recognizer.adjust_for_ambient_noise(Source)
            self.audio = self.Recognizer.record(Source)
            self.Result = self.Recognizer.recognize_google(self.audio,language=str(self.Lang))

    def __WRIF(self):#@Write Result In File
        self.File =  open(str(self.EndFile_Path),'w+', encoding="utf-8")
        self.File.write("#############################\n\nPhoenix Smart Assistent\n\n#############################")
        self.File.write("\n")
        self.File.write("Text:")
        self.File.write("\n")
        self.File.write(str(self.Result))
        self.File.close()
    
    def __Finish_Process(self):
        print("ready!")
        MRES("Result: ","Finish!.Your Audio File Is Converted.")
        print("finish!")


