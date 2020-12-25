import os
import sys
sys.path.insert(0, 'proj/')

print("███ █  █ ███ ███ ████ █   █   ████ ███ ███ ████ █  █")
print(" █  ██ █ █    █  █  █ █   █   █  █  █   █  █  █ ██ █")
print(" █  █ ██ ███  █  ████ █   █   ████  █   █  █  █ █ ██")
print(" █  █  █   █  █  █  █ █   █   █  █  █   █  █  █ █  █")
print("███ █  █ ███  █  █  █ ███ ███ █  █  █  ███ ████ █  █")
print("\n\n\nDo you want start program after installation?(y/n)")
startprogram = str(input("-->"))
os.system("pip3 install keyboard")
os.system("pip3 install PILLOW")
os.system("pip3 install tkinter")
if startprogram == "y":
    import start
else:
    exit()
input()