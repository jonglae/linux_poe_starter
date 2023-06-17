#!/usr/bin/python3
import sys
import os
import subprocess

POE_PATH = "drive_c/Daum Games/Path of Exile/"
POE_CLIENT_PATH = POE_PATH + "PathOfExile_KG.exe"

def parseURL(url):
  # URL 구분자 삭제
  without_proto = url[18:]

  # DaumGameStarter가 url에서 구분자로 '|'를 쓴다.
  split = without_proto.split("|")
  if len(split) == 1:
    split = without_proto.split("%7C")
  return split

def runPOE(data):
  # POE 설치된 위치
  poe_path = os.environ["HOME"] + "/Games/path-of-exile/"
  wine_path = os.environ["HOME"] + "/.local/share/lutris/runners/wine/lutris-GE-Proton7-43-x86_64/bin/wine"

  print(poe_path)

  # POE 실행을 위한 환경 변수 설정
  poe_env = os.environ.copy()
  poe_env["WINEPREFIX"] = poe_path
  poe_env["WINEFSYNC"] = "1"
  poe_env["WINEESYNC"] = "1"
  # poe_env["WINEDEBUG"] = "+esync"

  # POE 직접 실행
  poe = poe_path + POE_CLIENT_PATH
  # 명령 실행
  subprocess.check_call([wine_path, poe, "--nologo", "-gc", "2", "--kakao", data[3], data[4]], env=poe_env, cwd=poe_path + POE_PATH)

def main():
  if len(sys.argv) == 1:
    print("fakeDaumgamestarter.py - simple implement daumgamestarter for linux wine")
    print("usage: python3 runDaumgamestarter.py 'daumgamestarter://game|env|launcher|token..|etc'")
    return

  parsed = parseURL(sys.argv[1])
  if parsed[0] == "poe":
    runPOE(parsed)
    # 종료 대기를 위해 입력 대기
    # 게임 종료 후 엔터 한번만 누르면 완전히 종료된다.
    input()
  else:
    print("No Compatible: ", sys.argv, parsed)

if __name__ == "__main__":
  main()