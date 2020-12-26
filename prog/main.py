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


#commands
def play():
    startbutton.place(x=130, y=10, height=40, width=40)
    name.place(x=420, y=50)
    roundedbutton.place(x=70, y=10)
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
    yourslovo.pack_forget()
def setting():
    roundedbutton.pack(pady=1,padx=1)
    startbutton.pack(pady=1,padx=1)
    roundedbutton.pack_forget()
    startbutton.pack_forget()
    playbut.place(x=70,y=10)
    inp.place(x = 60,y=120,height=40)
    text.place(x=60,y=90)
    getbutton.place(x=700,y=120,height=41)
    name.pack()
    name.pack_forget()
    sname.place(x=300,y=1)
    stopbutton.pack_forget()
def setdictionary():
    inputget=str(inpu.get())
    config.dictionarypath = inputget
def close():
    global word
    root.destroy()
    word = "exitq"
    time.sleep(0.5)
    keyboard.release("space")
    print(1)
def start():
    tyour.pack()
    tyour.place(x=10,y=83)
    tpod.pack()
    tpod.place(x=10,y=265)
    slovo1.place(x=10,y=300,width=380,height=70)
    slovo2.place(x=390, y=300,width=380,height=70)
    slovo3.place(x=10, y=370,width=380,height=70)
    slovo4.place(x=390, y=370,width=380,height=70)
    slovo5.place(x=190, y=440,width=380,height=70)
    yourslovo.pack()
    yourslovo.place(x=10, y=120,width=480,height=90)
    roundedbutton.pack(pady=1, padx=1)
    startbutton.pack(pady=1, padx=1)
    roundedbutton.pack_forget()
    startbutton.pack_forget()
    stopbutton.pack()
    stopbutton.place(x=70,y=10,height=40,width=40)
    playbut.pack(pady=1,padx=1)
    playbut.pack_forget()
    inp.pack(pady=1, padx=1)
    inp.pack_forget()
    text.pack(pady=1, padx=1)
    text.pack_forget()
    getbutton.pack(pady=1, padx=1)
    getbutton.pack_forget()
    name.place(x=420, y=5)
    root.wm_attributes('-topmost', 1)


#hud
loadimage = PhotoImage(file=config.imgpath)
loadimage = loadimage.subsample(16)
roundedbutton = tk.Button(root, image=loadimage,bg=config.butbg,command=setting,highlightbackground=config.butbg)
roundedbutton.place(x=70,y=10)
startbutton = tk.Button(root,bg=config.butbg,command=start,text="▶",fg=config.bg,font = config.font)
startbutton.place(x=130,y=10,height=40,width=40)
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
text = tk.Label(root,height=1,font=config.text,fg=config.bg,bg=config.butbg,text="Задать путь к словарю")
text["border"] = "0"
text.pack()
text.pack_forget()
getbutton = tk.Button(root,bg=config.butbg,command=setdictionary,text="установить",fg=config.bg,font = config.text)
getbutton.pack()
getbutton.pack_forget()
slovo1 = tk.Text(root, height=2, font=config.text, fg=config.butbg, bg=config.bg,highlightbackground=config.butbg,highlightthickness=4)
slovo1["border"] = "0"
slovo1.pack_forget()
slovo2 = tk.Text(root, height=2, font=config.text, fg=config.butbg, bg=config.bg,highlightbackground=config.butbg,highlightthickness=4)
slovo2["border"] = "0"
slovo2.pack_forget()
slovo3 = tk.Text(root, height=2, font=config.text, fg=config.butbg, bg=config.bg,highlightbackground=config.butbg,highlightthickness=4)
slovo3["border"] = "0"
slovo3.pack_forget()
slovo4 = tk.Text(root, height=2, font=config.text, fg=config.butbg, bg=config.bg,highlightbackground=config.butbg,highlightthickness=4)
slovo4["border"] = "0"
slovo4.pack_forget()
slovo5 = tk.Text(root, height=2, font=config.text, fg=config.butbg, bg=config.bg,highlightbackground=config.butbg,highlightthickness=4)
slovo5.insert(END,"")
slovo5["border"] = "0"
slovo5.pack_forget()
yourslovo = tk.Text(root, height=2, font=config.text, fg=config.butbg, bg=config.bg,highlightbackground=config.butbg,highlightthickness=4)
yourslovo.insert(END,"")
yourslovo["border"] = "0"
yourslovo.pack_forget()
name = tk.Label(root,height=1,font=config.name,fg=config.butbg,bg=config.bg,text="T9 ")
name.place(x=420,y=50)
sname = tk.Label(root, height=1, font=config.name, fg=config.butbg, bg=config.bg, text="настройки")
sname.pack_forget()
tyour = tk.Label(root, height=1, font=config.text, fg=config.bg, bg=config.butbg, text="Ваше слово")
tyour.pack_forget()
tpod = tk.Label(root, height=1, font=config.text, fg=config.bg, bg=config.butbg, text="Подсказки")
tpod.pack_forget()
qt = tk.Button(root,bg="red",command=close,text="✖",fg=config.bg,font = config.text)
qt.place(x=10,y=10,height = 39,width=39)
#t9
def my_mainloop():
    global w1
    global w2
    global w3
    global w4
    global w5
    global word
    if 1>100:
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
        slovo1.delete('1.0', END)
        slovo1.insert(END, "" + str(w1))
        slovo2.delete('1.0', END)
        slovo2.insert(END, "" + str(w2))
        slovo3.delete('1.0', END)
        slovo3.insert(END, "" + str(w3))
        slovo4.delete('1.0', END)
        slovo4.insert(END, "" + str(w4))
        slovo5.delete('1.0', END)
        slovo5.insert(END, "" + str(w5))
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
        slovo1.delete('1.0', END)
        slovo1.insert(END, "" + str(w1))
        slovo2.delete('1.0', END)
        slovo2.insert(END, "" + str(w2))
        slovo3.delete('1.0', END)
        slovo3.insert(END, "" + str(w3))
        slovo4.delete('1.0', END)
        slovo4.insert(END, "" + str(w4))
        slovo5.delete('1.0', END)
        slovo5.insert(END, "" + str(w5))
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
        slovo1.delete('1.0', END)
        slovo1.insert(END, "" + str(w1))
        slovo2.delete('1.0', END)
        slovo2.insert(END, "" + str(w2))
        slovo3.delete('1.0', END)
        slovo3.insert(END, "" + str(w3))
        slovo4.delete('1.0', END)
        slovo4.insert(END, "" + str(w4))
        slovo5.delete('1.0', END)
        slovo5.insert(END, "" + str(w5))
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
        slovo1.delete('1.0', END)
        slovo1.insert(END, "" + str(w1))
        slovo2.delete('1.0', END)
        slovo2.insert(END, "" + str(w2))

        slovo3.delete('1.0', END)
        slovo3.insert(END, "" + str(w3))

        slovo4.delete('1.0', END)
        slovo4.insert(END, "" + str(w4))

        slovo5.delete('1.0', END)
        slovo5.insert(END, "" + str(w5))
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
        slovo1.delete('1.0', END)
        slovo1.insert(END, "" + str(w1))
        slovo2.delete('1.0', END)
        slovo2.insert(END, "" + str(w2))

        slovo3.delete('1.0', END)
        slovo3.insert(END, "" + str(w3))

        slovo4.delete('1.0', END)
        slovo4.insert(END, "" + str(w4))

        slovo5.delete('1.0', END)
        slovo5.insert(END, "" + str(w5))
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
