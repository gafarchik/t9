import os
import threading
def ui():
    os.system("python proj/prog/main.py")
def t9():
    os.system("python proj/prog/tscript/t9.py")
t1 = threading.Thread(target=ui, args=())
t2 = threading.Thread(target=t9, args=())
t1.start()
t2.start()