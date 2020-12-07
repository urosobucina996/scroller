
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():

    browser=webdriver.Chrome(ChromeDriverManager().install())
    browser.get("http://www.9gag.com")
    for i in range(1,10):
        browser.execute_script("window.scrollTo(0,"+str(i*300)+")")
        #browser.execute_script("window.scrollBy(0,"+str(i*300)+")")
        time.sleep(3)

    browser.close()

if __name__ == '__main__':
    main()
