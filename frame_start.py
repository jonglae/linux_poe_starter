 #!/usr/bin/env python3
from tkinter import *
import subprocess
import os

root = Tk()
root.title("리눅스 POE 게임 스타터")
root.geometry("800x200+500+1500")

def exit_windows():
    root.destroy()

txt = Text(root, width=160, height=10)
txt.pack()
scr_txt1 = txt.pack()
# print("srctxt",scr_txt1)

def write_text():
    scr_txt2= txt.get("1.0","end")
    result = scr_txt2[24:]
    result = "nohup python3 "+"./fakeDaumgameStarter.py "+"'daumgamestarter://"+result+"'"+">/dev/null 2>&1"
    print("입력받은 텍스트",result)
    # os.system('cd')
    # os.system('pwd')
    os.system(result)
    exit_windows()

btn = Button(root, text="게임시작",command=write_text)
btn2 = Button(root, text="EXIT",command=exit_windows)

btn.pack()
btn2.pack()

root.mainloop()