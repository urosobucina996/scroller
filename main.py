import webbrowser 
import pyautogui

url = 'http://www.9gag.com'

# new=1 opens in new browser, open otvara url
# webbrowser.register('mozilla',webbrowser.get('mozilla'))
width, height= pyautogui.size()
try:
    pyautogui.moveTo(width/2,height/2)
    webbrowser.open(url,new=1)
except KeyboardInterrupt:
    print("Your script executed!")
