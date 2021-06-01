import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

weburl = os.getenv('WEB_URL')
time.sleep(200)
check=1
while(check>0):
    gChromeOptions = webdriver.ChromeOptions()
    gChromeOptions.add_argument("window-size=1920x1480")
    gChromeOptions.add_argument("disable-dev-shm-usage")
    gChromeOptions.add_argument("incognito")
    gDriver = webdriver.Chrome(
        chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
    )
    
    gDriver.get(weburl)
    time.sleep(600)
    gDriver.close()
    print("Times Run (incognito4) = ", check)
    check=check+1
