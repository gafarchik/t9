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
#window settings
root = tk.Tk()
root.geometry("%dx%d" % (config.width, config.height))
root.overrideredirect(0)
root.config(bg=config.bg)
root.title(config.title)
root.resizable(height=0,width=0)
#commands
def play():
    name.place(x=420, y=50)
    roundedbutton.place(x=10, y=10)
    startbutton.place(x=400, y=250)
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
def setting():
    roundedbutton.pack(pady=1,padx=1)
    startbutton.pack(pady=1,padx=1)
    roundedbutton.pack_forget()
    startbutton.pack_forget()
    playbut.place(x=10,y=10)
    inp.place(x = 60,y=120,height=40)
    text.place(x=60,y=80)
    getbutton.place(x=700,y=120,height=41)
    name.pack()
    name.pack_forget()
    sname.place(x=300,y=1)
def setdictionary():
    inputget=str(inpu.get())
    config.dictionarypath = inputget
def start():
    qt.place(x=1,y=1,height=20,width=20)
    slovo1.place(x=10,y=100,width=480)
    slovo2.place(x=10, y=160,width=480)
    slovo3.place(x=10, y=220,width=480)
    slovo4.place(x=10, y=280,width=480)
    slovo5.place(x=10, y=340,width=480)
    roundedbutton.pack(pady=1, padx=1)
    startbutton.pack(pady=1, padx=1)
    roundedbutton.pack_forget()
    startbutton.pack_forget()
    playbut.pack(pady=1,padx=1)
    playbut.pack_forget()
    inp.pack(pady=1, padx=1)
    inp.pack_forget()
    text.pack(pady=1, padx=1)
    text.pack_forget()
    getbutton.pack(pady=1, padx=1)
    getbutton.pack_forget()
    name.pack(pady=1, padx=1)
    name.pack_forget()
    root.geometry("%dx%d" % (config.width, config.height))
    root.overrideredirect(0)
    root.geometry("500x500+100+100")
    root.wm_attributes('-topmost', 1)
#hud
loadimage = PhotoImage(file=config.imgpath)
loadimage = loadimage.subsample(16)
roundedbutton = tk.Button(root, image=loadimage,bg=config.bg,command=setting)
roundedbutton["border"] = "0"
roundedbutton.place(x=10,y=10)
startbutton = tk.Button(root,bg=config.butbg,command=start,text="START",fg=config.bg,font = config.font)
startbutton.place(x=400,y=250)
image = PhotoImage(file=config.butpath)
image = image.subsample(16)
playbut = tk.Button(root, image=image, bg=config.bg, command=play)
playbut["border"] = "0"
playbut.pack(pady=1,padx=1)
playbut.pack_forget()
inpu = StringVar()
inp = Entry(width=34,font=config.font,textvariable=inpu)
inp.pack(pady=1,padx=1)
inp.pack_forget()
inp.insert(END,"proj/prog/tscript/slov.txt")
text = tk.Label(root,height=1,font=config.text,fg=config.butbg,bg=config.bg,text="Задать путь к словарю")
text["border"] = "0"
text.pack()
text.pack_forget()
getbutton = tk.Button(root,bg=config.butbg,command=setdictionary,text="установить",fg=config.bg,font = config.text)
getbutton.pack()
getbutton.pack_forget()
slovo1 = tk.Text(root, height=2, font=config.text, fg="white", bg=config.bg)
slovo1["border"] = "2"
slovo1.pack_forget()
slovo2 = tk.Text(root, height=2, font=config.text, fg="white", bg=config.bg)
slovo2["border"] = "2"
slovo2.pack_forget()
slovo3 = tk.Text(root, height=2, font=config.text, fg="white", bg=config.bg)
slovo3["border"] = "2"
slovo3.pack_forget()
slovo4 = tk.Text(root, height=2, font=config.text, fg="white", bg=config.bg)
slovo4["border"] = "2"
slovo4.pack_forget()
slovo5 = tk.Text(root, height=2, font=config.text, fg="white", bg=config.bg)
slovo5.insert(END,"enter some text")
slovo5["border"] = "2"
slovo5.pack_forget()
name = tk.Label(root,height=1,font=config.name,fg=config.butbg,bg=config.bg,text="T9 ")
name.place(x=420,y=50)
sname = tk.Label(root, height=1, font=config.name, fg=config.butbg, bg=config.bg, text="настройки")
sname.pack_forget()
qt = tk.Button(root,bg="red",command=quit,text="✖",fg=config.bg,font = config.text)
qt.pack_forget()
#t9

def my_mainloop():
    global w1
    global w2
    global w3
    global w4
    global w5
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
    root.after(1, my_mainloop)
root.after(1, my_mainloop)
tlist = []
alist = []
check = len(alist)
def t9():
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

    word = ""
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
