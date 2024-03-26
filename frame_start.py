#!/usr/bin/env python3
import tkinter as tk
import subprocess

def start_game():
    user_input = text_box.get("1.0", tk.END).strip()
    if user_input.startswith("daumgamestarter://"):
        command = f"GDK_BACKEND=x11 nohup python3 ./fakeDaumgameStarter.py '{user_input}' >/dev/null 2>&1"
        subprocess.Popen(command, shell=True)
        root.destroy()
    else:
        status_label.config(text="잘못된 입력입니다. 올바른 입력을 해주세요.")

root = tk.Tk()
root.title("리눅스 POE 게임 스타터")
root.geometry("800x250+500+1500")

text_box = tk.Text(root, width=160, height=10)
text_box.pack()

start_button = tk.Button(root, text="게임시작", command=start_game)
start_button.pack()

exit_button = tk.Button(root, text="EXIT", command=root.destroy)
exit_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
