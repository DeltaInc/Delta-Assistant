import requests
from bs4 import BeautifulSoup
import time as tm
import winsound as ws

class Alarm:
    def __init__(self,currency,min,maxium=None):
        self.__Currency = currency
        self.__Min = min
        self.__Max = maxium
        #TODO : I should be change this url and get this data from my sever.I should be write an api in a server for Δ assistant.
        self.__URL = "https://api.nobitex.ir/v2/orderbook/" + self.__Currency.upper() + "IRT"

    def range(self):
        #@SAMPLE : attention eth alarm down 813000000 and up 823000000
        while True:
            page = requests.get(self.__URL)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.get_text()
            result = results.removeprefix('{"status":"ok","bids":[["').split('"')[0]
            print(result)
            if result < self.__Min:
                #F:/projectpy/info-app/test.wav
                ws.PlaySound("warrning",ws.SND_FILENAME)
            elif result > self.__Max:
                ws.PlaySound("good",ws.SND_FILENAME)
            tm.sleep(2)
    
    def defult(self):
        #@SAMPLE : attention eth alarm down 813000000
        while True:
            page = requests.get(self.__URL)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.get_text()
            result = results.removeprefix('{"status":"ok","bids":[["').split('"')[0]
            print(result)
            if result < self.__Min:
                #F:/projectpy/info-app/test.wav
                ws.PlaySound("warrning",ws.SND_FILENAME)
            tm.sleep(2) 