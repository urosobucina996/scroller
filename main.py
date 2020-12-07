# import webbrowser 
# import pyautogui

# url = 'http://www.9gag.com'

# # new=1 opens in new browser, open otvara url
# # webbrowser.register('mozilla',webbrowser.get('mozilla'))
# width, height= pyautogui.size()
# try:
#     pyautogui.moveTo(width/2,height/2)
#     webbrowser.open(url,new=1)
# except KeyboardInterrupt:
#     print("Your script executed!")
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    
    browser=webdriver.Chrome(ChromeDriverManager().install())
    browser.get("http://www.9gag.com")
    for i in range(1,10):
        browser.execute_script("window.scrollTo(0,"+str(i*300)+")")
        time.sleep(3)

    browser.close()


# browser=webdriver.Chrome(ChromeDriverManager().install())
# browser.get("http://www.9gag.com")
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(3)
#browser.close()

if __name__ == '__main__':
    main()
