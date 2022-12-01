import webbrowser
import time
import pyautogui

# 실행전 준비 : 크롬실행, 백준로그인, 백준허브 확장프로그램 실행

baekjoon_num = "".split(" ") 
# baekjoon_num = "1000 1001 1002".split(" ")
webbrowser.register('chrome', None,
                    webbrowser.BackgroundBrowser("크롬 실행위치"))
# webbrowser.register('chrome', None,
#                     webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))


for i in baekjoon_num:
    url = "https://www.acmicpc.net/status?from_mine=1&problem_id={}&user_id=유저ID".format(i)
    webbrowser.get('chrome').open(url)
    time.sleep(8)
    pyautogui.hotkey('ctrl', 'w')
