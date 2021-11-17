import tkinter as tk
import tkinter.messagebox as MessageBox
import webbrowser as wb
import os
import time as tm
import speech_recognition as sr
import random
import winsound as ws
import requests
from bs4 import BeautifulSoup
from instagramy import InstagramUser
import eyed3
import sqlite3 as sq
import pdf2image
import math
from modules.cryptography.core import crypt
from modules.open import open_url,project
from modules.messagebox.error.open_project import OPRO
from modules.search.bing import Main as bing_serach
from modules.search.google import Main as google_serach
from modules.search.wikipedia import Main as wikipedia_serach
from modules.math.math import base as base_math
from modules.math.math import advand as advand_math
from modules.messagebox.info.math import MRES
from modules.renames import RFAF
from modules.pap.core import PAP
from modules.attention.alarm import Alarm
def Main(c):
    cd = c.split(' ')
    cdd = c.split('-')
    cda = c.split('@')
    cdl = c.split('|')
    if cd[0]=="open":
        if cd[1]=="url":open_url.open(cd[2])
        elif cd[1]=="project":
            if cd[2]=="py":
                if cd[3]=="with":
                    if cd[4]=="idle":project.py(cd[5],True)
                project.py(cd[3])
            elif cd[2]=="b4a":project.b4a(cd[3])
            elif cd[2]=="c#":project.cs(cd[3])
            elif cd[2]=="js":project.js(cd[3])
            elif cd[2]=="vb":project.vb(cd[3])
            elif cd[2]=="web":project.web(cd[3])
            else:OPRO().show()
    elif cd[0]=="hello":MessageBox.showinfo("","hello                           ")
    elif cdd[0]=="what's your name?":MessageBox.showinfo("Your Name!","I don't now your name.                           ")
    elif cdd[0]=="please say about you":MessageBox.showinfo("Me","I'm Phoenix Smart Assistant.I Want to help My Creator ,My Creator is Phoenix                            ")             
    elif cdd[0]=="What Do You Can":MessageBox.showinfo("I can","I Can {this for PSA}                           ")
    elif cd[0]=="search":
        if cd[1]=="google":google_serach(cd[2]).search()
        elif cd[1]=="bing":bing_serach(cd[2]).search()
        elif cd[1]=="wiki":
            if cd[2]=="fa":wikipedia_serach(cd[3]).fa()
            elif cd[2]=="en":wikipedia_serach(cd[3]).en()
            else:wikipedia_serach(cd[3]).RTL()
    elif cd[0]=="math":
        if cd[1]=="sum":
            result = base_math.sum(cd[2],cd[3])
            MRES(msg=result).show()
        elif cd[1]=="mul":
            result = base_math.mul(cd[2],cd[3])
            MRES(msg=result).show()
        elif cd[1]=="min":
            result = base_math.min(cd[2].cd[3])
            MRES(msg=result).show()
        elif cd[1]=="div":
            result = base_math.div(cd[2],cd[3])
            MRES(msg=result).show()
        elif cd[1]=="sqr":
            result = base_math.sqr(cd[2])
            MRES(msg=result).show()
        elif cd[1]=="ceil":
            MRES(msg=str(base_math.ceil(cd[2]))).show()
        elif cd[1]=="floor":
            MRES(msg=str(base_math.floor(cd[2]))).show()
        elif cd[1]=="abs":
            MRES(msg=str(base_math.absv(cd[2]))).show()
        elif cd[1]=="fac":
            MRES(msg=str(base_math.fac(cd[2]))).show()
        elif cd[1]=="ln":
            MRES(msg=str(base_math.ln(cd[2]))).show()
        elif cd[1]=="log":
            MRES(msg=str(base_math.log(cd[2],cd[3]))).show()
        elif cd[1]=="log10":
            MRES(msg=str(base_math.log_10(cd[2]))).show()
        elif cd[1]=="log2":
            MRES(msg=str(base_math.log_2(cd[2]))).show()
        elif cd[1]=="cos":
            if cd[2]=="deg":MRES(msg=str(advand_math.cos(cd[3],True))).show()
            else:MRES(msg=str(advand_math.cos(cd[2]))).show()
        elif cd[1]=="sin":
            if cd[2]=="deg":MRES(msg=str(advand_math.sin(cd[3],True))).show()
            else:MRES(msg=str(advand_math.sin(cd[2]))).show()
        elif cd[1]=="tan":
            if cd[2]=="deg":MRES(msg=str(advand_math.tan(cd[3],True))).show()
            else:MRES(msg=str(advand_math.tan(cd[2]))).show()
        elif cd[1]=="acos":
            if cd[2]=="deg":MRES(msg=str(advand_math.acos(cd[3],True))).show()
            else:MRES(msg=str(advand_math.acos(cd[2]))).show()
        elif cd[1]=="asin":
            if cd[2]=="deg":MRES(msg=str(advand_math.asin(cd[3],True))).show()
            else:MRES(msg=str(advand_math.asin(cd[2]))).show()
        elif cd[1]=="atan":
            if cd[2]=="deg":MRES(msg=str(math.atan(cd[3],True))).show()
            else:MRES(msg=str(advand_math.atan(cd[2]))).show()
        elif cd[1]=="cosh":
            if cd[2]=="deg":MRES(msg=str(advand_math.cosh(cd[3],True))).show()
            else:MRES(msg=str(advand_math.cosh(cd[2]))).show()
        elif cd[1]=="sinh":
            if cd[2]=="deg":MRES(msg=str(math.degrees(math.sinh(cd[3])))).show()
            else:MRES(msg=str(advand_math.sinh(cd[2]))).show()
        elif cd[1]=="tanh":
            if cd[2]=="deg":MRES(msg=str(math.tanh(cd[3],True))).show()
            else:MRES(msg=str(advand_math.tanh(cd[2]))).show()
        elif cd[1]=="acosh":
            if cd[2]=="deg":MRES(msg=str(math.acosh(cd[3],True))).show()
            else:MRES(msg=str(advand_math.acosh(cd[2]))).show()
        elif cd[1]=="asinh":
            if cd[2]=="deg":MRES(msg=str(advand_math.asinh(cd[3],True))).show()
            else:MRES(msg=str(advand_math.asinh(cd[2]))).show()
        elif cd[1]=="atanh":
            if cd[2]=="deg":MRES(msg=str(advand_math.atanh(cd[3],True))).show()
            else:MRES(msg=str(advand_math.atanh(cd[2]))).show()
        elif cd[1]=="number":
            if cd[2]=="pi":MRES(msg=str(advand_math.number_p))
            elif cd[2]=="e":MRES(msg=str(advand_math.number_e))
    elif cda[0]=="renames":
        if cda[2]=="to":RFAF(cd[1],cd[3]).start()
    elif cda[0]=="pea":
        if cda[1]=="with data":
            print("start rsi")
            f = open(str(cda[2]),'r',encoding='utf-8')
            fr = f.read()
            l1 = fr.split("\n")
            mnf = []
            msb = []
            clpc = []
            rlpc = []
            mmnf = 0
            mmsb = 0
            rs = 0
            rs_1 = 0
            rs_1_100 = 0
            rsi = 0
            for ln in l1:
                l2 = ln.split(",")
                l2.remove(l2[0])
                date = l2[0]
                high = l2[2]
                low = l2[3]
                value = l2[5]
                volume = l2[6]
                count = l2[7]
                openp = l2[8]
                close = l2[4]
                result = float(close) - float(openp)
                if result == 0.0:rlpc.append(result)
                elif result != 0.0:
                    rlpc.append(float(float(100 /  float(float(openp) / float(result)))))
                    print(str(str(float(float(100 /  float(float(openp) / float(result))))) + " close : " + close + " open : " + openp))
                clpc.append(close)
            num14 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
            for n in num14:
                if str(rlpc[int(int(cda[4]) - n)]).startswith("-")==True:mnf.append(clpc[int(int(cda[4]) - n)])
                elif str(rlpc[int(int(cda[4]) - n)]).startswith("-")==False:msb.append(clpc[int(int(cda[4]) - n)])
                else:print("hello")
            def sumarray(ls:list):
                r = 0
                for l in ls:r = r + float(l)
                return r
            mmnf = mmnf + float(float(sumarray(mnf)) / 14)
            mmsb = mmsb + float(float(sumarray(msb)) / 14)
            rs = rs + float(mmsb / mmnf)
            rs_1 = rs + float(1)
            rs_1_100 = rs_1_100 + float(100 / float(rs_1))
            rsi = rsi + float(100 - float(rs_1_100))
            if str(str(rsi).split('.'))[0] >= "70":print(str("rsi is false"))
            elif str(str(rsi).split('.'))[0] <= "30":print(str("rsi is true"))
            else:print(str("rsi is meddum"))
            print("this RSI is : " + str(rsi))
            print("start ma")
            closen = []
            for price in range(0,int(cda[5])):closen.append(float(clpc[int(int(cda[4]) - int(price))]))
            ma = int(sumarray(closen)) / int(cda[5])
            if str(ma) >= str(clpc[int(int(cda[4]) - 0)]):print(str("ma is false"))
            elif str(str(ma).split('.'))[0] <= str(clpc[int(int(cda[4]) - 0)]):print(str("ma is true"))
            else:print(str("rsi is meddum"))
            print("this ma is : " + str(ma))
            print("start ema")
            ToDay =  clpc[int(int(cda[4]) - 0)]
            try:NumberOfDays = int(cda[6])
            except IndexError:NumberOfDays = 7.0
            k = 2.0 / float(1.0 + float(NumberOfDays))
            print("k : " + str(k))
            em = float(float(float(ToDay) - float(cda[7]))) * float(k)
            print(str(ToDay))
            print("em : " + str(em))
            ema = float(em) + float(cda[7])
            print("this ema is : " + str(ema))
    elif cd[0]=="attention":
        if cd[2]=="alarm":
            if cd[3]=="range":Alarm(cd[1],cd[4],cd[6]).range()
            else:Alarm(cd[1],cd[3]).defult()
    elif cd[0]=="find":
        if cd[1]=="instagram" or "insta":
            username = str(cd[2]).split(':')[1]
            data_file = open(f"{username}.json",'w+',encoding="utf-8")
            user = InstagramUser(str(username))
            data_file.write(str(user.get_json()))
            data_file.close()
    elif cda[0]=="paa":
        file_fname = cd[1].removeprefix(cd[1].split('/')[len(cd[1].split('/')) - 1])
        file_type = file_fname.split('.')[len(file_fname.split(".")) - 1]
        if file_type == "mp3":
            audiofile = eyed3.load(str(cd[1]))
            file_fname = cd[1].removeprefix(cd[1].split('/')[len(cd[1].split('/')) - 1])
            artist = audiofile.tag.artist
            album = audiofile.tag.album
            album_artist = audiofile.tag.album_artist
            title = audiofile.tag.title
            track_num = audiofile.tag.track_num
            MessageBox.showinfo(f"{file_fname} information",f"""
            Artist : {artist}
            Album : {album}
            Album Artist : {album_artist}
            Title : {title}
            Track Number : {track_num}
            """)
        elif file_type != "mp3":
            file_fname = cd[1].removeprefix(cd[1].split('/')[len(cd[1].split('/')) - 1])
            file_address = cd[1].removesuffix(file_fname)
            file_name = file_fname.split('.')[0]
            new_file = str(file_address + file_name)
            os.system(f'ffmpeg -i {cd[2]} {new_file}')
    elif cda[0] == "PPP":
        if cda[1] == "jpg":
            images =  pdf2image.convert_from_path(cda[2].replace("\\","/"))
            for image in images:images[image].save('page_'+ str(image) +'.jpg', 'JPEG')
            MessageBox.showinfo("finish","finish this work")