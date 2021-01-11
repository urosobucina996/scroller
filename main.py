
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import os

def main():

    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("http://www.9gag.com")
    scroll = { "top" : 0, "behavior" : 'smooth'}
    for i in range(1,10):
        scroll["top"] = i*350
        browser.execute_script("window.scrollTo("+json.dumps(scroll)+")")
        time.sleep(3)

    browser.close()

if __name__ == '__main__':
    main()
