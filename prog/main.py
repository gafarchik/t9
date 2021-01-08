#imports
import keyboard
import sys
import time
sys.path.insert(0,"proj/prog/tscript/")
import tkinter as tk
from tkinter import *
import threading
import config

#config
config.font = "Arial 24 bold"
color = 0
lang = 0
bgcolor = 6
rootcolor=6
bclose = ""
bopen = ""
w1 = ""
w2 = ""
w3 = ""
w4 = ""
w5 = ""
word = ""
#window settings
root = tk.Tk()
root.geometry("%dx%d" % (config.width, config.height))
root.overrideredirect(0)
root.config(bg=config.bg)
root.title(config.title)
root.resizable(height=0,width=0)

btn_text1 = tk.StringVar()
btn_text2 = tk.StringVar()
btn_text3 = tk.StringVar()
btn_text4 = tk.StringVar()
btn_text5 = tk.StringVar()
maxwidth = root.winfo_screenwidth()
maxheight = root.winfo_screenheight()
#commands
def play():
    startbutton.place(x=config.width/100*13.6842105263, y=config.height/100*1.66666666667,height = config.height/100*6.5,width=config.width/100*4.10526315789)
    name.place(x=config.width/100*44.2105263158,y=config.height/100*8.33333333333)
    roundedbutton.place(x=config.width/100*7.36842105263, y=config.height/100*1.66666666667,height = config.height/100*6.5,width=config.width/100*4.10526315789)
    playbut.pack(pady=1,padx=1)
    playbut.pack_forget()
    inp.pack(pady=1, padx=1)
    inp.pack_forget()
    text.pack(pady=1, padx=1)
    text.pack_forget()
    getbutton.pack(pady=1, padx=1)
    getbutton.pack_forget()
    sname.pack()
    sname.pack_forget()
    stopbutton.pack()
    stopbutton.pack_forget()
    tpod.pack()
    tyour.pack()
    slovo1.pack()
    slovo2.pack()
    slovo3.pack()
    slovo4.pack()
    slovo5.pack()
    tpod.pack_forget()
    tyour.pack_forget()
    slovo1.pack_forget()
    slovo2.pack_forget()
    slovo3.pack_forget()
    slovo4.pack_forget()
    slovo5.pack_forget()
    yourslovo.pack()
    butgreen.pack()
    butyellow.pack()
    butblack.pack()
    butblue.pack()
    butred.pack()
    butwhite.pack()
    butdefault.pack()
    cconfirm.pack()
    ctext.pack()
    ctext.pack_forget()
    yourslovo.pack_forget()
    butgreen.pack_forget()
    butyellow.pack_forget()
    butblack.pack_forget()
    butblue.pack_forget()
    butred.pack_forget()
    butwhite.pack_forget()
    butdefault.pack_forget()
    cconfirm.pack_forget()
    butbgred.pack()
    butbgblue.pack()
    butbgyellow.pack()
    butbggreen.pack()
    butbgblack.pack()
    butbgwhite.pack()
    butbgdefault.pack()
    bgtext.pack()
    cbgconfirm.pack()
    cbgconfirm.pack_forget()
    butbgred.pack_forget()
    butbgblue.pack_forget()
    butbgyellow.pack_forget()
    butbggreen.pack_forget()
    butbgblack.pack_forget()
    butbgwhite.pack_forget()
    butbgdefault.pack_forget()
    bgtext.pack_forget()
    butrtred.pack()
    butrtblue.pack()
    butrtyellow.pack()
    butrtgreen.pack()
    butrtblack.pack()
    butrtwhite.pack()
    butrtdefault.pack()
    rttext.pack()
    crtconfirm.pack()
    crtconfirm.pack_forget()
    butrtred.pack_forget()
    butrtblue.pack_forget()
    butrtyellow.pack_forget()
    butrtgreen.pack_forget()
    butrtblack.pack_forget()
    butrtwhite.pack_forget()
    butrtdefault.pack_forget()
    rttext.pack_forget()
    inpwidth.pack()
    inphight.pack()
    inpwidth.pack_forget()
    inphight.pack_forget()
    sizetext.pack()
    sizetext.pack_forget()
    xtext.pack()
    xtext.pack_forget()
    sizeconfirm.pack()
    sizeconfirm.pack_forget()
    butru.pack()
    buten.pack()
    butru.pack_forget()
    buten.pack_forget()
    ltext.pack()
    ltext.pack_forget()
    activ.pack()
    activ.pack_forget()
    dactiv.pack()
    dactiv.pack_forget()
    minitext.pack()
    minitext.pack_forget()
    miniconfirm.pack()
    miniconfirm.pack_forget()
    inpclose.pack()
    inpopen.pack()
    inpclose.pack_forget()
    inpopen.pack_forget()
    miniclose.pack()
    miniopen.pack()
    miniclose.pack_forget()
    miniopen.pack_forget()
def setting():
    miniclose.place(x=320,y=510)
    miniopen.place(x=320,y=420)
    inpopen.place(x=config.width/100*38.9473684211,y=config.height/100*76.6666666667,width=100)
    inpclose.place(x=config.width/100*38.9473684211,y=config.height/100*91.6666666667,width=100)
    miniconfirm.place(x=config.width/100*80,y=config.height/100*86.6666666667)
    minitext.place(x=config.width/100*36.8421052632,y=config.height/100*58.3333333333)
    activ.place(x=config.width/100*35.7894736842,y=config.height/100*63.6666666667)
    dactiv.place(x=config.width/100*44.2105263158,y=config.height/100*63.6666666667)
    butrtgreen.place(x=config.width/100*49.4736842105, y=config.height/100*41.6666666667, height=config.height/100*3.33333333333, width=config.width/100*2.10526315789)
    butrtblue.place(x=config.width/100*51.5789473684, y=config.height/100*41.6666666667, height=config.height/100*3.33333333333, width=config.width/100*2.10526315789)
    butrtred.place(x=config.width/100*53.6842105263, y=config.height/100*41.6666666667, height=config.height/100*3.33333333333, width=config.width/100*2.10526315789)
    butrtdefault.place(x=config.width/100*55.7894736842, y=config.height/100*41.6666666667, height=config.height/100*3.33333333333, width=config.width/100*2.10526315789)
    butrtyellow.place(x=config.width/100*57.8947368421, y=config.height/100*41.6666666667, height=config.height/100*3.33333333333, width=config.width/100*2.10526315789)
    butrtblack.place(x=config.width/100*60, y=config.height/100*41.6666666667, height=config.height/100*3.33333333333, width=config.width/100*2.10526315789)
    butrtwhite.place(x=config.width/100*62.1052631579, y=config.height/100*41.6666666667, height=config.height/100*3.33333333333, width=config.width/100*2.10526315789)
    crtconfirm.place(x=config.width/100*48.4210526316, y=config.height/100*46.6666666667)
    rttext.place(x=config.width/100*48.4210526316, y=config.height/100*33.3333333333)
    butbggreen.place(x=config.width/100*28.4210526316,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    butbgblue.place(x=config.width/100*30.5263157895,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    butbgred.place(x=config.width/100*32.6315789474,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    butbgdefault.place(x=config.width/100*34.7368421053,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    butbgyellow.place(x=config.width/100*36.8421052632,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    butbgblack.place(x=config.width/100*38.9473684211,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    butbgwhite.place(x=config.width/100*41.0526315789,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    cbgconfirm.place(x=config.width/100*26.3157894737,y=config.height/100*46.6666666667)
    bgtext.place(x=config.width/100*26.3157894737,y=config.height/100*33.3333333333)
    roundedbutton.pack(pady=1,padx=1)
    startbutton.pack(pady=1,padx=1)
    roundedbutton.pack_forget()
    startbutton.pack_forget()
    playbut.place(x=config.width/100*7.36842105263,y=config.height/100*1.66666666667,height = config.height/100*6.5,width=config.width/100*4.10526315789)
    inp.place(x = config.width/100*6.31578947368,y=config.height/100*20,height=40)
    text.place(x=config.width/100*6.31578947368,y=config.height/100*14)
    getbutton.place(x=config.width/100*73.6842105263,y=config.height/100*20,height=41)
    ltext.place(y=config.height/100*33.3333333333,x=config.width/100*82.2105263158)
    butru.place(y=config.height/100*41.6666666667,x=config.width/100*78.9473684211,width=65,height=47)
    buten.place(y=config.height/100*41.6666666667, x=config.width/100*86.3157894737, width=65, height=47)
    name.pack()
    name.pack_forget()
    sname.place(x=config.width/100*31.5789473684,y=config.height/100*0.16666666666)
    stopbutton.pack_forget()
    butgreen.place(x=config.width/100*8.42105263158,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    butyellow.place(x=config.width/100*10.5263157895,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    butblack.place(x=config.width/100*12.6315789474,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    butblue.place(x=config.width/100*14.7368421053,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    butred.place(x=config.width/100*16.8421052632,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    butwhite.place(x=config.width/100*18.9473684211,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    butdefault.place(x=config.width/100*21.0526315789,y=config.height/100*41.6666666667,height=config.height/100*3.33333333333,width=config.width/100*2.10526315789)
    cconfirm.place(x=config.width/100*6.31578947368,y=config.height/100*46.6666666667)
    ctext.place(x=config.width/100*6.31578947368,y=config.height/100*33.3333333333)
    inpwidth.place(x=config.width/100*6.31578947368,y=config.height/100*66.6666666667)
    inphight.place(x=config.width/100*21.0526315789,y=config.height/100*66.6666666667)
    sizetext.place(x=config.width/100*6.31578947368,y=config.height/100*58.3333333333)
    xtext.place(x=config.width/100*17.8947368421,y=config.height/100*66.6666666667)
    sizeconfirm.place(x=config.width/100*6.31578947368,y=config.height/100*78.3333333333)
def setdictionary():
    inputget=str(inpu.get())
    config.dictionarypath = inputget
def close():
    global word
    root.destroy()
    word = "exitq"
    time.sleep(0.5)
    keyboard.release("space")
    print("Press Any Key To Exit...")
def start():
    miniclose.pack()
    miniopen.pack()
    miniclose.pack_forget()
    miniopen.pack_forget()
    inpclose.pack()
    inpopen.pack()
    inpclose.pack_forget()
    inpopen.pack_forget()
    miniconfirm.pack()
    miniconfirm.pack_forget()
    minitext.pack()
    minitext.pack_forget()
    dactiv.pack()
    dactiv.pack_forget()
    ltext.pack()
    ltext.pack_forget()
    butru.pack()
    buten.pack()
    butru.pack_forget()
    buten.pack_forget()
    sizeconfirm.pack()
    sizeconfirm.pack_forget()
    xtext.pack()
    xtext.pack_forget()
    sizetext.pack()
    sizetext.pack_forget()
    inphight.pack()
    inpwidth.pack()
    inphight.pack_forget()
    inpwidth.pack_forget()
    butrtred.pack()
    butrtblue.pack()
    butrtyellow.pack()
    butrtgreen.pack()
    butrtblack.pack()
    butrtwhite.pack()
    butrtdefault.pack()
    rttext.pack()
    crtconfirm.pack()
    crtconfirm.pack_forget()
    butrtred.pack_forget()
    butrtblue.pack_forget()
    butrtyellow.pack_forget()
    butrtgreen.pack_forget()
    butrtblack.pack_forget()
    butrtwhite.pack_forget()
    butrtdefault.pack_forget()
    rttext.pack_forget()
    butbgred.pack()
    butbgblue.pack()
    butbgyellow.pack()
    butbggreen.pack()
    butbgblack.pack()
    butbgwhite.pack()
    butbgdefault.pack()
    bgtext.pack()
    cbgconfirm.pack()
    cbgconfirm.pack_forget()
    butbgred.pack_forget()
    butbgblue.pack_forget()
    butbgyellow.pack_forget()
    butbggreen.pack_forget()
    butbgblack.pack_forget()
    butbgwhite.pack_forget()
    butbgdefault.pack_forget()
    bgtext.pack_forget()
    butgreen.pack()
    butyellow.pack()
    butblack.pack()
    butblue.pack()
    butred.pack()
    butwhite.pack()
    butdefault.pack()
    cconfirm.pack()
    activ.pack()
    activ.pack_forget()
    ctext.pack()
    ctext.pack_forget()
    butgreen.pack_forget()
    butyellow.pack_forget()
    butblack.pack_forget()
    butblue.pack_forget()
    butred.pack_forget()
    butwhite.pack_forget()
    butdefault.pack_forget()
    cconfirm.pack_forget()
    tyour.pack()
    tyour.place(x=config.width/100*1.05263157895,y=config.height/100*13.8333333333)
    tpod.pack()
    tpod.place(x=config.width/100*1.05263157895,y=config.height/100*44.1666666667)
    slovo1.place(x=config.width/100*1.05263157895,y=config.height/100*50,width=config.width/100*40,height=config.height/100*11.6666666667)
    slovo2.place(x=config.width/100*41.0526315789, y=config.height/100*50,width=config.width/100*40,height=config.height/100*11.6666666667)
    slovo3.place(x=config.width/100*1.05263157895, y=config.height/100*61.6666666667,width=config.width/100*40,height=config.height/100*11.6666666667)
    slovo4.place(x=config.width/100*41.0526315789, y=config.height/100*61.6666666667,width=config.width/100*40,height=config.height/100*11.6666666667)
    slovo5.place(x=config.width/100*20, y=config.height/100*73.3333333333,width=config.width/100*40,height=config.height/100*11.6666666667)
    yourslovo.pack()
    yourslovo.place(x=config.width/100*1.05263157895, y=config.height/100*20,width=config.width/100*50.5263157895,height=config.height/100*20)
    roundedbutton.pack(pady=1, padx=1)
    startbutton.pack(pady=1, padx=1)
    roundedbutton.pack_forget()
    startbutton.pack_forget()
    stopbutton.pack()
    stopbutton.place(x=config.width/100*7.36842105263,y=config.height/100*1.66666666667,height=config.height/100*6.66666666667,width=config.width/100*4.21052631579)
    playbut.pack(pady=1,padx=1)
    playbut.pack_forget()
    inp.pack(pady=1, padx=1)
    inp.pack_forget()
    text.pack(pady=1, padx=1)
    text.pack_forget()
    getbutton.pack(pady=1, padx=1)
    getbutton.pack_forget()
    name.place(x=config.width/100*44.2105263158, y=config.height/100*0.83333333333)
    #root.wm_attributes('-topmost', 1)
def tw1():
    global word
    global w1
    word = w1
def tw2():
    global word
    global w2
    word = w2
def tw3():
    global word
    global w3
    word = w3
def tw4():
    global word
    global w4
    word = w4
def tw5():
    global word
    global w5
    global butbg
    word = w5
def cgreen():
    global color
    color = 0
    color +=1
def cyellow():
    global color
    color = 0
    color +=2
def cblue():
    global color
    color = 0
    color +=3
def cred():
    global color
    color = 0
    color +=4
def cdefault():
    global color
    color = 0
    color +=5
def cwhite():
    global color
    color = 0
    color +=6
def cblack():
    global color
    color = 0
    color +=7
def bggreen():
    global bgcolor
    bgcolor= 0
    bgcolor +=1
def bgyellow():
    global bgcolor
    bgcolor = 0
    bgcolor += 2
def bgblue():
    global bgcolor
    bgcolor = 0
    bgcolor += 3
def bgred():
    global bgcolor
    bgcolor = 0
    bgcolor += 4
def bgdefault():
    global bgcolor
    bgcolor = 0
    bgcolor += 5
def bgwhite():
    global bgcolor
    bgcolor = 0
    bgcolor += 6
def bgblack():
    global bgcolor
    bgcolor = 0
    bgcolor += 7
def rootgreen():
    global rootcolor
    rootcolor=0
    rootcolor+=1
def rootyellow():
    global rootcolor
    rootcolor=0
    rootcolor+=2
def rootblue():
    global rootcolor
    rootcolor=0
    rootcolor+=3
def rootred():
    global rootcolor
    rootcolor=0
    rootcolor+=4
def rootdefault():
    global rootcolor
    rootcolor=0
    rootcolor+=5
def rootwhite():
    global rootcolor
    rootcolor=0
    rootcolor+=6
def rootblack():
    global rootcolor
    rootcolor=0
    rootcolor+=7
def chcolor():
    global bgcolor
    global color
    global rootcolor
    if color == 1:#green
        inpclose.config(fg=config.green)
        inpopen.config(fg=config.green)
        xtext.config(fg=config.green)
        sizetext.config(fg=config.green)
        name.config(fg=config.green)
        yourslovo.config(fg=config.green)
        qt.config(fg=config.green)
        playbut.config(fg=config.green)
        sname.config(fg=config.green)
        slovo5.config(fg=config.green)
        slovo4.config(fg=config.green)
        slovo3.config(fg=config.green)
        slovo2.config(fg=config.green)
        slovo1.config(fg=config.green)
        startbutton.config(fg=config.green)
        stopbutton.config(fg=config.green)
        inp.config(fg=config.green)
        text.config(fg=config.green)
        tyour.config(fg=config.green)
        tpod.config(fg=config.green)
        ctext.config(fg=config.green)
        getbutton.config(fg=config.green)
        cconfirm.config(fg=config.green)
        cbgconfirm.config(fg=config.green)
        bgtext.config(fg=config.green)
        crtconfirm.config(fg=config.green)
        rttext.config(fg=config.green)
        inpwidth.config(fg=config.green)
        inphight.config(fg=config.green)
        sizeconfirm.config(fg=config.green)
        ltext.config(fg=config.green)
        activ.config(fg=config.green)
        dactiv.config(fg=config.green)
        minitext.config(fg=config.green)
        miniconfirm.config(fg=config.green)
        miniclose.config(fg=config.green)
        miniopen.config(fg=config.green)
    if color == 2:#yellow
        inpclose.config(fg=config.yellow)
        inpopen.config(fg=config.yellow)
        xtext.config(fg=config.yellow)
        sizetext.config(fg=config.yellow)
        name.config(fg=config.yellow)
        yourslovo.config(fg=config.yellow)
        qt.config(fg=config.yellow)
        playbut.config(fg=config.yellow)
        sname.config(fg=config.yellow)
        slovo5.config(fg=config.yellow)
        slovo4.config(fg=config.yellow)
        slovo3.config(fg=config.yellow)
        slovo2.config(fg=config.yellow)
        slovo1.config(fg=config.yellow)
        startbutton.config(fg=config.yellow)
        stopbutton.config(fg=config.yellow)
        inp.config(fg=config.yellow)
        text.config(fg=config.yellow)
        tyour.config(fg=config.yellow)
        tpod.config(fg=config.yellow)
        ctext.config(fg=config.yellow)
        getbutton.config(fg=config.yellow)
        cconfirm.config(fg=config.yellow)
        cbgconfirm.config(fg=config.yellow)
        bgtext.config(fg=config.yellow)
        crtconfirm.config(fg=config.yellow)
        rttext.config(fg=config.yellow)
        inpwidth.config(fg=config.yellow)
        inphight.config(fg=config.yellow)
        sizeconfirm.config(fg=config.yellow)
        ltext.config(fg=config.yellow)
        activ.config(fg=config.yellow)
        dactiv.config(fg=config.yellow)
        minitext.config(fg=config.yellow)
        miniconfirm.config(fg=config.yellow)
        miniclose.config(fg=config.yellow)
        miniopen.config(fg=config.yellow)
    if color == 3:#blue
        inpclose.config(fg=config.blue)
        inpopen.config(fg=config.blue)
        xtext.config(fg=config.blue)
        sizetext.config(fg=config.blue)
        name.config(fg=config.blue)
        yourslovo.config(fg=config.blue)
        qt.config(fg=config.blue)
        playbut.config(fg=config.blue)
        sname.config(fg=config.blue)
        slovo5.config(fg=config.blue)
        slovo4.config(fg=config.blue)
        slovo3.config(fg=config.blue)
        slovo2.config(fg=config.blue)
        slovo1.config(fg=config.blue)
        startbutton.config(fg=config.blue)
        stopbutton.config(fg=config.blue)
        inp.config(fg=config.blue)
        text.config(fg=config.blue)
        tyour.config(fg=config.blue)
        tpod.config(fg=config.blue)
        ctext.config(fg=config.blue)
        getbutton.config(fg=config.blue)
        cconfirm.config(fg=config.blue)
        cbgconfirm.config(fg=config.blue)
        bgtext.config(fg=config.blue)
        crtconfirm.config(fg=config.blue)
        rttext.config(fg=config.blue)
        inpwidth.config(fg=config.blue)
        inphight.config(fg=config.blue)
        sizeconfirm.config(fg=config.blue)
        ltext.config(fg=config.blue)
        activ.config(fg=config.blue)
        dactiv.config(fg=config.blue)
        minitext.config(fg=config.blue)
        miniconfirm.config(fg=config.blue)
        miniclose.config(fg=config.blue)
        miniopen.config(fg=config.blue)
    if color == 4:
        inpclose.config(fg=config.red)
        inpopen.config(fg=config.red)
        xtext.config(fg=config.red)
        sizetext.config(fg=config.red)
        name.config(fg=config.red)
        yourslovo.config(fg=config.red)
        qt.config(fg=config.red)
        playbut.config(fg=config.red)
        sname.config(fg=config.red)
        slovo5.config(fg=config.red)
        slovo4.config(fg=config.red)
        slovo3.config(fg=config.red)
        slovo2.config(fg=config.red)
        slovo1.config(fg=config.red)
        startbutton.config(fg=config.red)
        stopbutton.config(fg=config.red)
        inp.config(fg=config.red)
        text.config(fg=config.red)
        tyour.config(fg=config.red)
        tpod.config(fg=config.red)
        ctext.config(fg=config.red)
        getbutton.config(fg=config.red)
        cconfirm.config(fg=config.red)
        cbgconfirm.config(fg=config.red)
        bgtext.config(fg=config.red)
        crtconfirm.config(fg=config.red)
        rttext.config(fg=config.red)
        inpwidth.config(fg=config.red)
        inphight.config(fg=config.red)
        sizeconfirm.config(fg=config.red)
        ltext.config(fg=config.red)
        activ.config(fg=config.red)
        dactiv.config(fg=config.red)
        minitext.config(fg=config.red)
        miniconfirm.config(fg=config.red)
        miniclose.config(fg=config.red)
        miniopen.config(fg=config.red)
    if color == 5:
        inpclose.config(fg=config.default)
        inpopen.config(fg=config.default)
        xtext.config(fg=config.default)
        sizetext.config(fg=config.default)
        name.config(fg=config.default)
        yourslovo.config(fg=config.default)
        qt.config(fg=config.default)
        playbut.config(fg=config.default)
        sname.config(fg=config.default)
        slovo5.config(fg=config.default)
        slovo4.config(fg=config.default)
        slovo3.config(fg=config.default)
        slovo2.config(fg=config.default)
        slovo1.config(fg=config.default)
        startbutton.config(fg=config.default)
        stopbutton.config(fg=config.default)
        inp.config(fg=config.default)
        text.config(fg=config.default)
        tyour.config(fg=config.default)
        tpod.config(fg=config.default)
        ctext.config(fg=config.default)
        getbutton.config(fg=config.default)
        cconfirm.config(fg=config.default)
        cbgconfirm.config(fg=config.default)
        bgtext.config(fg=config.default)
        crtconfirm.config(fg=config.default)
        rttext.config(fg=config.default)
        inpwidth.config(fg=config.default)
        inphight.config(fg=config.default)
        sizeconfirm.config(fg=config.default)
        ltext.config(fg=config.default)
        activ.config(fg=config.default)
        dactiv.config(fg=config.default)
        minitext.config(fg=config.default)
        miniconfirm.config(fg=config.default)
        miniclose.config(fg=config.default)
        miniopen.config(fg=config.default)
    if color == 6:
        inpclose.config(fg=config.white)
        inpopen.config(fg=config.white)
        sizetext.config(fg=config.white)
        qt.config(fg=config.white)
        playbut.config(fg=config.white)
        startbutton.config(fg=config.white)
        stopbutton.config(fg=config.white)
        text.config(fg=config.white)
        tyour.config(fg=config.white)
        tpod.config(fg=config.white)
        ctext.config(fg=config.white)
        getbutton.config(fg=config.white)
        cconfirm.config(fg=config.white)
        cbgconfirm.config(fg=config.white)
        bgtext.config(fg=config.white)
        crtconfirm.config(fg=config.white)
        rttext.config(fg=config.white)
        crtconfirm.config(fg=config.white)
        rttext.config(fg=config.white)
        inpwidth.config(fg=config.white)
        inphight.config(fg=config.white)
        sizeconfirm.config(fg=config.white)
        ltext.config(fg=config.white)
        activ.config(fg=config.white)
        dactiv.config(fg=config.white)
        minitext.config(fg=config.white)
        miniconfirm.config(fg=config.white)
        miniclose.config(fg=config.white)
        miniopen.config(fg=config.white)
        if bgcolor==6:
            xtext.config(fg=config.white)
            yourslovo.config(fg=config.blue)
            inp.config(fg=config.black)
            slovo5.config(fg=config.blue)
            slovo4.config(fg=config.blue)
            slovo3.config(fg=config.blue)
            slovo2.config(fg=config.blue)
            slovo1.config(fg=config.blue)
        if bgcolor!=6:
            yourslovo.config(fg=config.white)
            inp.config(fg=config.white)
            slovo5.config(fg=config.white)
            slovo4.config(fg=config.white)
            slovo3.config(fg=config.white)
            slovo2.config(fg=config.white)
            slovo1.config(fg=config.white)
        if rootcolor!=6:
            xtext.config(fg=config.white)
            name.config(fg=config.white)
            sname.config(fg=config.white)
        if rootcolor==6:
            xtext.config(fg=config.blue)
            name.config(fg=config.blue)
            sname.config(fg=config.blue)
    if color == 7:
        inpclose.config(fg=config.black)
        inpopen.config(fg=config.black)
        xtext.config(fg=config.black)
        sizetext.config(fg=config.black)
        name.config(fg=config.black)
        yourslovo.config(fg=config.black)
        qt.config(fg=config.black)
        playbut.config(fg=config.black)
        sname.config(fg=config.black)
        slovo5.config(fg=config.black)
        slovo4.config(fg=config.black)
        slovo3.config(fg=config.black)
        slovo2.config(fg=config.black)
        slovo1.config(fg=config.black)
        startbutton.config(fg=config.black)
        stopbutton.config(fg=config.black)
        inp.config(fg=config.black)
        text.config(fg=config.black)
        tyour.config(fg=config.black)
        tpod.config(fg=config.black)
        ctext.config(fg=config.black)
        getbutton.config(fg=config.black)
        cconfirm.config(fg=config.black)
        cbgconfirm.config(fg=config.black)
        bgtext.config(fg=config.black)
        crtconfirm.config(fg=config.black)
        rttext.config(fg=config.black)
        inpwidth.config(fg=config.black)
        inphight.config(fg=config.black)
        sizeconfirm.config(fg=config.black)
        ltext.config(fg=config.black)
        activ.config(fg=config.black)
        dactiv.config(fg=config.black)
        minitext.config(fg=config.black)
        miniconfirm.config(fg=config.black)
        miniclose.config(fg=config.black)
        miniopen.config(fg=config.black)
def backcolor():
    global bgcolor
    if bgcolor == 1:#green
        inpclose.config(bg=config.green)
        inpopen.config(bg=config.green)
        yourslovo.config(bg=config.green)
        playbut.config(bg=config.green)
        slovo5.config(bg=config.green)
        slovo4.config(bg=config.green)
        slovo3.config(bg=config.green)
        slovo2.config(bg=config.green)
        slovo1.config(bg=config.green)
        startbutton.config(bg=config.green)
        stopbutton.config(bg=config.green)
        inp.config(bg=config.green)
        getbutton.config(bg=config.green)
        cconfirm.config(bg=config.green)
        cbgconfirm.config(bg=config.green)
        crtconfirm.config(bg=config.green)
        inpwidth.config(bg=config.green)
        inphight.config(bg=config.green)
        sizeconfirm.config(bg=config.green)
        roundedbutton.config(bg=config.green)
        miniconfirm.config(bg=config.green)
    if bgcolor == 2:#yellow
        inpclose.config(bg=config.yellow)
        inpopen.config(bg=config.yellow)
        yourslovo.config(bg=config.yellow)
        playbut.config(bg=config.yellow)
        slovo5.config(bg=config.yellow)
        slovo4.config(bg=config.yellow)
        slovo3.config(bg=config.yellow)
        slovo2.config(bg=config.yellow)
        slovo1.config(bg=config.yellow)
        startbutton.config(bg=config.yellow)
        stopbutton.config(bg=config.yellow)
        inp.config(bg=config.yellow)
        getbutton.config(bg=config.yellow)
        cconfirm.config(bg=config.yellow)
        cbgconfirm.config(bg=config.yellow)
        crtconfirm.config(bg=config.yellow)
        inpwidth.config(bg=config.yellow)
        inphight.config(bg=config.yellow)
        sizeconfirm.config(bg=config.yellow)
        roundedbutton.config(bg=config.yellow)
        miniconfirm.config(bg=config.yellow)
    if bgcolor == 3:#blue
        inpclose.config(bg=config.blue)
        inpopen.config(bg=config.blue)
        yourslovo.config(bg=config.blue)
        playbut.config(bg=config.blue)
        slovo5.config(bg=config.blue)
        slovo4.config(bg=config.blue)
        slovo3.config(bg=config.blue)
        slovo2.config(bg=config.blue)
        slovo1.config(bg=config.blue)
        startbutton.config(bg=config.blue)
        stopbutton.config(bg=config.blue)
        inp.config(bg=config.blue)
        getbutton.config(bg=config.blue)
        cconfirm.config(bg=config.blue)
        cbgconfirm.config(bg=config.blue)
        crtconfirm.config(bg=config.blue)
        inpwidth.config(bg=config.blue)
        inphight.config(bg=config.blue)
        sizeconfirm.config(bg=config.blue)
        roundedbutton.config(bg=config.blue)
        miniconfirm.config(bg=config.blue)
    if bgcolor == 4:
        inpclose.config(bg=config.red)
        inpopen.config(bg=config.red)
        yourslovo.config(bg=config.red)
        playbut.config(bg=config.red)
        slovo5.config(bg=config.red)
        slovo4.config(bg=config.red)
        slovo3.config(bg=config.red)
        slovo2.config(bg=config.red)
        slovo1.config(bg=config.red)
        startbutton.config(bg=config.red)
        stopbutton.config(bg=config.red)
        inp.config(bg=config.red)
        getbutton.config(bg=config.red)
        cconfirm.config(bg=config.red)
        cbgconfirm.config(bg=config.red)
        crtconfirm.config(bg=config.red)
        inpwidth.config(bg=config.red)
        inphight.config(bg=config.red)
        sizeconfirm.config(bg=config.red)
        roundedbutton.config(bg=config.red)
        miniconfirm.config(bg=config.red)
    if bgcolor == 5:
        inpclose.config(bg=config.default)
        inpopen.config(bg=config.default)
        yourslovo.config(bg=config.default)
        playbut.config(bg=config.default)
        slovo5.config(bg=config.default)
        slovo4.config(bg=config.default)
        slovo3.config(bg=config.default)
        slovo2.config(bg=config.default)
        slovo1.config(bg=config.default)
        startbutton.config(bg=config.default)
        stopbutton.config(bg=config.default)
        inp.config(bg=config.default)
        getbutton.config(bg=config.default)
        cconfirm.config(bg=config.default)
        cbgconfirm.config(bg=config.default)
        crtconfirm.config(bg=config.default)
        inpwidth.config(bg=config.default)
        inphight.config(bg=config.default)
        sizeconfirm.config(bg=config.default)
        roundedbutton.config(bg=config.default)
        miniconfirm.config(bg=config.default)
    if bgcolor == 6:
        inpclose.config(bg=config.white)
        inpopen.config(bg=config.white)
        yourslovo.config(bg=config.white)
        playbut.config(bg=config.white)
        slovo5.config(bg=config.white)
        slovo4.config(bg=config.white)
        slovo3.config(bg=config.white)
        slovo2.config(bg=config.white)
        slovo1.config(bg=config.white)
        startbutton.config(bg=config.white)
        stopbutton.config(bg=config.white)
        inp.config(bg=config.white)
        getbutton.config(bg=config.white)
        cconfirm.config(bg=config.white)
        cbgconfirm.config(bg=config.white)
        crtconfirm.config(bg=config.white)
        inpwidth.config(bg=config.white)
        inphight.config(bg=config.white)
        sizeconfirm.config(bg=config.white)
        roundedbutton.config(bg=config.white)
        miniconfirm.config(bg=config.white)
    if bgcolor == 7:
        inpclose.config(bg=config.black)
        inpopen.config(bg=config.black)
        yourslovo.config(bg=config.black)
        playbut.config(bg=config.black)
        slovo5.config(bg=config.black)
        slovo4.config(bg=config.black)
        slovo3.config(bg=config.black)
        slovo2.config(bg=config.black)
        slovo1.config(bg=config.black)
        startbutton.config(bg=config.black)
        stopbutton.config(bg=config.black)
        inp.config(bg=config.black)
        getbutton.config(bg=config.black)
        cconfirm.config(bg=config.black)
        cbgconfirm.config(bg=config.black)
        crtconfirm.config(bg=config.black)
        inpwidth.config(bg=config.black)
        inphight.config(bg=config.black)
        sizeconfirm.config(bg=config.black)
        roundedbutton.config(bg=config.black)
        miniconfirm.config(bg=config.black)
def rootcolors():
    global rootcolor
    if rootcolor == 1:
        xtext.config(bg=config.green)
        name.config(bg=config.green)
        sname.config(bg=config.green)
        root.config(bg=config.green)
        sizetext.config(bg=config.green)
        text.config(bg=config.green)
        tyour.config(bg=config.green)
        tpod.config(bg=config.green)
        ctext.config(bg=config.green)
        bgtext.config(bg=config.green)
        rttext.config(bg=config.green)
        ltext.config(bg=config.green)
        activ.config(bg=config.green)
        dactiv.config(bg=config.green)
        minitext.config(bg=config.green)
        miniclose.config(bg=config.green)
        miniopen.config(bg=config.green)
    if rootcolor == 2:
        xtext.config(bg=config.yellow)
        name.config(bg=config.yellow)
        sname.config(bg=config.yellow)
        root.config(bg=config.yellow)
        sizetext.config(bg=config.yellow)
        text.config(bg=config.yellow)
        tyour.config(bg=config.yellow)
        tpod.config(bg=config.yellow)
        ctext.config(bg=config.yellow)
        bgtext.config(bg=config.yellow)
        rttext.config(bg=config.yellow)
        ltext.config(bg=config.yellow)
        activ.config(bg=config.yellow)
        dactiv.config(bg=config.yellow)
        minitext.config(bg=config.yellow)
        miniclose.config(bg=config.yellow)
        miniopen.config(bg=config.yellow)
    if rootcolor == 3:
        xtext.config(bg=config.blue)
        name.config(bg=config.blue)
        sname.config(bg=config.blue)
        root.config(bg=config.blue)
        sizetext.config(bg=config.blue)
        text.config(bg=config.blue)
        tyour.config(bg=config.blue)
        tpod.config(bg=config.blue)
        ctext.config(bg=config.blue)
        bgtext.config(bg=config.blue)
        rttext.config(bg=config.blue)
        ltext.config(bg=config.blue)
        activ.config(bg=config.blue)
        dactiv.config(bg=config.blue)
        minitext.config(bg=config.blue)
        miniclose.config(bg=config.blue)
        miniopen.config(bg=config.blue)
    if rootcolor == 4:
        xtext.config(bg=config.red)
        name.config(bg=config.red)
        sname.config(bg=config.red)
        root.config(bg=config.red)
        sizetext.config(bg=config.red)
        text.config(bg=config.red)
        tyour.config(bg=config.red)
        tpod.config(bg=config.red)
        ctext.config(bg=config.red)
        bgtext.config(bg=config.red)
        rttext.config(bg=config.red)
        ltext.config(bg=config.red)
        activ.config(bg=config.red)
        dactiv.config(bg=config.red)
        minitext.config(bg=config.red)
        miniclose.config(bg=config.red)
        miniopen.config(bg=config.red)
    if rootcolor == 5:
        xtext.config(bg=config.default)
        name.config(bg=config.default)
        sname.config(bg=config.default)
        root.config(bg=config.default)
        sizetext.config(bg=config.default)
        text.config(bg=config.default)
        tyour.config(bg=config.default)
        tpod.config(bg=config.default)
        ctext.config(bg=config.default)
        bgtext.config(bg=config.default)
        rttext.config(bg=config.default)
        ltext.config(bg=config.default)
        activ.config(bg=config.default)
        dactiv.config(bg=config.default)
        minitext.config(bg=config.default)
        miniclose.config(bg=config.default)
        miniopen.config(bg=config.default)
    if rootcolor == 6:
        xtext.config(bg=config.white)
        name.config(bg=config.white)
        sname.config(bg=config.white)
        root.config(bg=config.white)
        text.config(bg=config.white)
        tyour.config(bg=config.white)
        tpod.config(bg=config.white)
        ctext.config(bg=config.white)
        sizetext.config(bg=config.white)
        rttext.config(bg=config.white)
        bgtext.config(bg=config.white)
        ltext.config(bg=config.white)
        activ.config(bg=config.white)
        dactiv.config(bg=config.white)
        minitext.config(bg=config.white)
        miniclose.config(bg=config.white)
        miniopen.config(bg=config.white)
    if rootcolor == 7:
        bgtext.config(bg=config.gray)
        rttext.config(bg=config.gray)
        sizetext.config(bg=config.gray)
        text.config(bg=config.gray)
        tyour.config(bg=config.gray)
        tpod.config(bg=config.gray)
        ctext.config(bg=config.gray)
        xtext.config(bg=config.gray)
        name.config(bg=config.gray)
        sname.config(bg=config.gray)
        root.config(bg=config.gray)
        ltext.config(bg=config.gray)
        activ.config(bg=config.gray)
        dactiv.config(bg=config.gray)
        minitext.config(bg=config.gray)
        miniclose.config(bg=config.gray)
        miniopen.config(bg=config.gray)
def sizeconfirm():
    global maxwidth
    global maxheight
    global ihight
    global iwidth
    newwidth = int(iwidth.get())
    newheight = int(ihight.get())
    if newheight <= maxheight:
        if newwidth <= maxwidth:
            root.geometry("{}x{}".format(newwidth,newheight))
    if newwidth <= maxwidth:
        if newheight <= maxheight:
            root.geometry("{}x{}".format(newwidth,newheight))
def ru():
    global lang
    lang = 0
    language()
def en():
    global lang
    lang = 1
    language()
def language():
    global lang
    if lang == 0:
        sname.config(text="Настройки")
        sizetext.config(text="Размер окна")
        text.config(text="Задать путь к словарю")
        tyour.config(text="Ваше слово")
        tpod.config(text="Подсказки")
        ctext.config(text="Цвет текста")
        bgtext.config(text="Цвет фона")
        rttext.config(text="Цвет окна")
        ltext.config(text="Язык")
        cconfirm.config(text="Установить")
        cbgconfirm.config(text="Установить")
        crtconfirm.config(text="Установить")
        sizeconfirm.config(text="Установить")
        getbutton.config(text="Установить")
        miniconfirm.config(text="Установить")
        minitext.config(text="Мини окно")
        miniopen.config(text="Кнопка открытия")
        miniclose.config(text="Кнопка закрытия")
    if lang == 1:
        bgtext.place(x=config.width/100*23.3157894737,y=config.height/100*33.3333333333)
        rttext.place(x=config.width/100*49.4210526316, y=config.height/100*33.3333333333)
        miniconfirm.config(text="Set")
        sname.config(text="Settings")
        sizetext.config(text="Window size")
        text.config(text="Set path to dictionary")
        tyour.config(text="Your word")
        tpod.config(text="Hints")
        ctext.config(text="Text color")
        bgtext.config(text="Background color")
        rttext.config(text="Window color")
        ltext.config(text="Language")
        cconfirm.config(text="Set")
        cbgconfirm.config(text="Set")
        crtconfirm.config(text="Set")
        sizeconfirm.config(text="Set")
        getbutton.config(text="Set")
        minitext.config(text="Mini Window")
        miniclose.config(text="Close Button")
        miniopen.config(text="Open Button")
def new():
    global activ_var
    global key
    global bindclose
    global bindopen
    var=activ_var.get()
    if var == 0:
        pass
    if var == 1:
        window = tk.Toplevel(root)
def openbind(event):
    global bopen
    key2 = keyboard.read_key()
    badkeys = ["q","w","e","r","t","y","u","i","o","p",
               "a","s","d","f","g","h","j","k","l"
               ,"z","x","c","v","b","n","m",
               "enter","backspace","space"]
    if key2:
        if key2 not in badkeys:
            bopen = key2
            inpopen.delete(0,END)
            inpopen.insert(END,bopen)
def closebind(event):
    global bclose
    key2 = keyboard.read_key()
    badkeys = ["q","w","e","r","t","y","u","i","o","p",
               "a","s","d","f","g","h","j","k","l"
               ,"z","x","c","v","b","n","m",
               "enter","backspace","space"]
    if key2:
        if key2 not in badkeys:
            bclose = key2
            inpclose.delete(0,END)
            inpclose.insert(END,bclose)
#hud
loadimage = PhotoImage(file=config.imgpath)
loadimage = loadimage.subsample(16)
roundedbutton = tk.Button(root, image=loadimage,bg=config.butbg,command=setting,highlightbackground=config.butbg)
roundedbutton.place(x=config.width/100*7.36842105263,y=config.height/100*1.66666666667,height = config.height/100*6.5,width=config.width/100*4.10526315789)
startbutton = tk.Button(root,bg=config.butbg,command=start,text="▶",fg=config.bg,font = config.font)
startbutton.place(x=config.width/100*13.6842105263,y=config.height/100*1.66666666667,height = config.height/100*6.5,width=config.width/100*4.10526315789)
stopbutton = tk.Button(root,bg=config.butbg,command=play,text="⏸",fg=config.bg,font = config.font)
stopbutton.pack_forget()
image = PhotoImage(file=config.butpath)
image = image.subsample(16)
playbut = tk.Button(root, image=image, bg=config.butbg, command=play,highlightbackground=config.butbg)
playbut.pack(pady=1,padx=1)
playbut.pack_forget()
inpu = StringVar()
inp = Entry(width=34,font=config.font,textvariable=inpu,highlightbackground=config.butbg,highlightthickness=4)
inp.pack(pady=1,padx=1)
inp.pack_forget()
inp.insert(END,"proj/prog/tscript/slov.txt")
text = tk.Label(root,height=1,font=config.text,fg=config.butbg,bg=config.white,text="Задать путь к словарю")
text["border"] = "0"
text.pack()
text.pack_forget()
getbutton = tk.Button(root,bg=config.butbg,command=setdictionary,text="установить",fg=config.bg,font = config.text)
getbutton.pack()
getbutton.pack_forget()
slovo1 = tk.Button(root, textvariable = btn_text1,command=tw1, font=config.text, fg=config.butbg, bg=config.bg,highlightbackground=config.butbg,highlightthickness=4)
slovo1.pack_forget()
slovo2 = tk.Button(root,  font=config.text, textvariable = btn_text2,command=tw2, fg=config.butbg, bg=config.bg,highlightbackground=config.butbg,highlightthickness=4)
slovo2.pack_forget()
slovo3 = tk.Button(root,  font=config.text, textvariable = btn_text3,command=tw3, fg=config.butbg, bg=config.bg,highlightbackground=config.butbg,highlightthickness=4)
slovo3.pack_forget()
slovo4 = tk.Button(root,  font=config.text, fg=config.butbg, textvariable = btn_text4,command=tw4, bg=config.bg ,highlightbackground=config.butbg,highlightthickness=4)
slovo4.pack_forget()
slovo5 = tk.Button(root, font=config.text, fg=config.butbg, textvariable = btn_text5,command=tw5,bg=config.bg,highlightbackground=config.butbg,highlightthickness=4)
slovo5.pack_forget()
yourslovo = tk.Text(root,height=2, font=config.text, fg=config.butbg, bg=config.bg,highlightbackground=config.butbg,highlightthickness=4)
yourslovo.insert(END,"")
yourslovo["border"] = "0"
yourslovo.pack_forget()
name = tk.Label(root,height=1,font=config.name,fg=config.butbg,bg=config.bg,text="T9 ")
name.place(x=config.width/100*44.2105263158,y=config.height/100*8.33333333333)
sname = tk.Label(root, height=1, font=config.name, fg=config.butbg, bg=config.bg, text="настройки")
sname.pack_forget()
tyour = tk.Label(root, height=1, font=config.text, fg=config.butbg, bg=config.white, text="Ваше слово")
tyour.pack_forget()
tpod = tk.Label(root, height=1, font=config.text, fg=config.butbg, bg=config.white, text="Подсказки")
tpod.pack_forget()
qt = tk.Button(root,bg="red",command=close,text="✖",fg=config.bg,font = config.text)
qt.place(x=config.width/100*1.05263157895,y=config.height/100*1.66666666667,height = config.height/100*6.5,width=config.width/100*4.10526315789)
butgreen = tk.Button(root,font=config.text,fg=config.bg,bg=config.green,command=cgreen)
butgreen.pack_forget()
butyellow = tk.Button(root,font=config.text,fg=config.bg,bg=config.yellow,command=cyellow)
butyellow.pack_forget()
butblue = tk.Button(root,font=config.text,fg=config.bg,bg=config.blue,command=cblue)
butblue.pack_forget()
butred = tk.Button(root,font=config.text,fg=config.bg,bg=config.red,command=cred)
butred.pack_forget()
butdefault = tk.Button(root,font=config.text,fg=config.bg,bg=config.default,command=cdefault)
butdefault.pack_forget()
butwhite = tk.Button(root,font=config.text,fg=config.bg,bg=config.white,command=cwhite)
butwhite.pack_forget()
butblack = tk.Button(root,font=config.text,fg=config.bg,bg=config.black,command=cblack)
butblack.pack_forget()
cconfirm = tk.Button(root,font=config.text,fg=config.bg,bg=config.butbg,command=chcolor,text="Установить")
cconfirm.pack_forget()
ctext = tk.Label(root, height=1, font=config.text, fg=config.butbg, bg=config.white, text="Цвет текста")
ctext.pack_forget()
butbggreen = tk.Button(root,font=config.text,fg=config.bg,bg=config.green,command=bggreen)
butbggreen.pack_forget()
butbgyellow = tk.Button(root,font=config.text,fg=config.bg,bg=config.yellow,command=bgyellow)
butbgyellow.pack_forget()
butbgblue = tk.Button(root,font=config.text,fg=config.bg,bg=config.blue,command=bgblue)
butbgblue.pack_forget()
butbgred = tk.Button(root,font=config.text,fg=config.bg,bg=config.red,command=bgred)
butbgred.pack_forget()
butbgdefault = tk.Button(root,font=config.text,fg=config.bg,bg=config.default,command=bgdefault)
butbgdefault.pack_forget()
butbgwhite = tk.Button(root,font=config.text,fg=config.bg,bg=config.white,command=bgwhite)
butbgwhite.pack_forget()
butbgblack = tk.Button(root,font=config.text,fg=config.bg,bg=config.black,command=bgblack)
butbgblack.pack_forget()
cbgconfirm = tk.Button(root,font=config.text,fg=config.bg,bg=config.butbg,command=backcolor,text="Установить")
cbgconfirm.pack_forget()
bgtext = tk.Label(root, height=1, font=config.text, fg=config.butbg, bg=config.white, text="Задний фон")
bgtext.pack_forget()
butrtgreen = tk.Button(root,font=config.text,fg=config.bg,bg=config.green,command=rootgreen)
butrtgreen.pack_forget()
butrtyellow = tk.Button(root,font=config.text,fg=config.bg,bg=config.yellow,command=rootyellow)
butrtyellow.pack_forget()
butrtblue = tk.Button(root,font=config.text,fg=config.bg,bg=config.blue,command=rootblue)
butrtblue.pack_forget()
butrtred = tk.Button(root,font=config.text,fg=config.bg,bg=config.red,command=rootred)
butrtred.pack_forget()
butrtdefault = tk.Button(root,font=config.text,fg=config.bg,bg=config.default,command=rootdefault)
butrtdefault.pack_forget()
butrtwhite = tk.Button(root,font=config.text,fg=config.bg,bg=config.white,command=rootwhite)
butrtwhite.pack_forget()
butrtblack = tk.Button(root,font=config.text,fg=config.bg,bg=config.gray,command=rootblack)
butrtblack.pack_forget()
crtconfirm = tk.Button(root,font=config.text,fg=config.bg,bg=config.butbg,command=rootcolors,text="Установить")
crtconfirm.pack_forget()
rttext = tk.Label(root, height=1, font=config.text, fg=config.butbg, bg=config.white, text="Задний фон окна")
rttext.pack_forget()
iwidth = StringVar()
inpwidth = Entry(width=5,font=config.font,textvariable=iwidth,highlightbackground=config.butbg,highlightthickness=4)
inpwidth.pack_forget()
ihight = StringVar()
inphight = Entry(width=5,font=config.font,textvariable=ihight,highlightbackground=config.butbg,highlightthickness=4)
inphight.pack_forget()
sizetext = tk.Label(root, height=1, font=config.text, fg=config.butbg, bg=config.white, text="Размеры окна")
sizetext.pack_forget()
xtext = tk.Label(root, height=1, font=config.text, fg=config.butbg, bg=config.bg, text="x")
xtext.pack_forget()
sizeconfirm = tk.Button(root,font=config.text,fg=config.bg,bg=config.butbg,command=sizeconfirm,text="Установить")
sizeconfirm.pack_forget()
ruimg = PhotoImage(file=config.rupath)
ruimg = ruimg.subsample(16)
enimg = PhotoImage(file=config.enpath)
enimg = enimg.subsample(16)
butru = tk.Button(root, image=ruimg,bg=config.butbg,command=ru,highlightbackground=config.butbg)
butru.pack_forget()
buten = tk.Button(root, image=enimg,bg=config.butbg,command=en,highlightbackground=config.butbg)
buten.pack_forget()
ltext = tk.Label(root, height=1, font=config.text, fg=config.butbg, bg=config.white, text="Язык")
ltext.pack_forget()
activ_var = IntVar()
activ_var.set(0)
activ = tk.Radiobutton(bg=config.white,text="On",variable=activ_var, value=1,fg=config.blue,font=config.text)
activ.pack_forget()
dactiv = tk.Radiobutton(bg=config.white,text="Off",variable=activ_var, value=0,fg=config.blue,font=config.text)
dactiv.pack_forget()
minitext = tk.Label(root, height=1, font=config.text, fg=config.butbg, bg=config.white, text="Мини окно")
minitext.pack_forget()
miniconfirm = tk.Button(root,font=config.text,fg=config.bg,bg=config.butbg,command=new,text="Установить")
miniconfirm.pack_forget()
bindclose = StringVar()
inpclose = Entry(width=14,font=config.font,textvariable=bindclose,highlightbackground=config.butbg,highlightthickness=4)
inpclose.pack_forget()
bindopen = StringVar()
inpopen = Entry(width=14,font=config.font,textvariable=bindopen,highlightbackground=config.butbg,highlightthickness=4)
inpopen.pack_forget()
miniopen = tk.Label(root, height=1, font=config.text, fg=config.butbg, bg=config.white, text="Кнопка Открытия")
miniopen.pack_forget()
miniclose = tk.Label(root, height=1, font=config.text, fg=config.butbg, bg=config.white, text="Кнопка Закрытия",)
miniclose.pack_forget()
inpopen.bind('<Button-1>',openbind)
inpclose.bind('<Button-1>',closebind)
#t9
def my_mainloop():
    global w1
    global w2
    global w3
    global w4
    global w5
    global word
    global btn_text1
    global btn_text2
    global btn_text3
    global btn_text4
    global btn_text5
    global bindclose
    global bindopen
    if 1==100:
        print(2)
    elif len(alist)==4:
        w1 = ""
        w2 = ""
        w3 = ""
        w4 = ""
        w5 = ""
        w1 = alist[0]
        w2 = alist[1]
        w3 = alist[2]
        w4 = alist[3]
        w5 = ""
        root.update()
        btn_text1.set(w1)
        btn_text2.set(w2)
        btn_text3.set(w3)
        btn_text4.set(w4)
        btn_text5.set(w5)
        yourslovo.delete('1.0',END)
        yourslovo.insert(END,""+str(word))
    elif len(alist)==3:
        w1 = ""
        w2 = ""
        w3 = ""
        w4 = ""
        w5 = ""
        w1 = alist[0]
        w2 = alist[1]
        w3 = alist[2]
        w4 = ""
        w5 = ""
        btn_text1.set(w1)
        btn_text2.set(w2)
        btn_text3.set(w3)
        btn_text4.set(w4)
        btn_text5.set(w5)
        yourslovo.delete('1.0', END)
        yourslovo.insert(END, "" + str(word))
    elif len(alist)==2:
        w1 = ""
        w2 = ""
        w3 = ""
        w4 = ""
        w5 = ""
        w1 = alist[0]
        w2 = alist[1]
        w3 = ""
        w4 = ""
        w5 = ""
        btn_text1.set(w1)
        btn_text2.set(w2)
        btn_text3.set(w3)
        btn_text4.set(w4)
        btn_text5.set(w5)
        yourslovo.delete('1.0', END)
        yourslovo.insert(END, "" + str(word))
    elif len(alist)==1:
        w1 = ""
        w2 = ""
        w3 = ""
        w4 = ""
        w5 = ""
        w1 = alist[0]
        w2 = ""
        w3 = ""
        w4 = ""
        w5 = ""
        btn_text1.set(w1)
        btn_text2.set(w2)
        btn_text3.set(w3)
        btn_text4.set(w4)
        btn_text5.set(w5)
        yourslovo.delete('1.0', END)
        yourslovo.insert(END, "" + str(word))
    elif len(alist)>5:
        w1 = ""
        w2 = ""
        w3 = ""
        w4 = ""
        w5 = ""
        w1 = alist[0]
        w2 = alist[1]
        w3 = alist[2]
        w4 = alist[3]
        w5 = alist[4]
        btn_text1.set(w1)
        btn_text2.set(w2)
        btn_text3.set(w3)
        btn_text4.set(w4)
        btn_text5.set(w5)
        yourslovo.delete('1.0', END)
        yourslovo.insert(END, "" + str(word))
    yourslovo.delete('1.0', END)
    yourslovo.insert(END, "" + str(word))
    root.after(1, my_mainloop)
root.after(1, my_mainloop)
tlist = []
alist = []
check = len(alist)
def t9():
    global word
    class Trie(object):
        def __init__(self):
            self.childNode = {}
            self.word_finished = False

        def add_Child(self, word):
            if len(word) == 0:
                self.word_finished = True
                return
            key = word[0]
            word = word[1:]
            if key in self.childNode:
                self.childNode[key].add_Child(word)
            else:
                node = Trie()
                self.childNode[key] = node
                node.add_Child(word)

        def search_word(self, word, word_keys=""):
            if len(word) > 0:
                key = word[0]
                prefix = word[1:]
                if key in self.childNode:
                    word_keys = word_keys + key
                    self.childNode[key].search_word(prefix, word_keys)
                else:
                    tlist.clear()
            else:
                if self.word_finished == True:
                    tlist.append(word_keys)
                    alist.append(word_keys)
                for key in self.childNode.keys():
                    self.childNode[key].DFS(word_keys + key)

        def DFS(self, word_keys=None):
            if self.childNode.keys() == []:
                tlist.append(word_keys)
                alist.append(word_keys)
                return
            if self.word_finished == True:
                tlist.append(word_keys)
                alist.append(word_keys)
            for key in self.childNode.keys():
                self.childNode[key].DFS(word_keys + key)

    hendler = ""
    bad = ["down", "alt", "shift", "ctrl", "up", "esc", "backspace", "locknum", "insert", "delete", "space", "enter",
           "left", "right", "tab", "caps lock", "home", "print screen", "page up", "page down", "left windows",
           "right alt", "right ctrl", "end", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12",
           "\\", "/", "|", ".", ",", "?", "!", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "`", ";", ":", "~",
           ">", "<", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "="]
    trie = Trie()
    with open(config.dictionarypath, 'r') as f:
        words = f.readline().strip('\r\n')
        while words != '':
            trie.add_Child(words)
            words = f.readline().strip('\r\n')
    while True:
        key = keyboard.read_key()
        if word == 'exitq':
            exit()
            break
        if key:
            if key not in bad:
                alist.clear()
                word += key
                trie.search_word(word)
                tlist.clear()
                time.sleep(0.1)
        if key == "space":
            word = ""
            tlist.clear()
        if key == "backspace":
            srez = len(word)
            srez = srez-1
            word = word[:srez]
            tlist.clear()
            time.sleep(0.1)

#start process
t1 = threading.Thread(target=t9, args=())
t1.start()
ui = root.mainloop()
t2 = threading.Thread(target=ui, args=())
t2.start()
