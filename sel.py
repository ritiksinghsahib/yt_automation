from selenium import webdriver
import win32com.client as comctl
from bs4 import BeautifulSoup
import time
wsh = comctl.Dispatch("WScript.Shell")


driver=webdriver.Chrome()


driver.get('https://www.youtube.com')
search=driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
n=["laide phulkari","jaan","White gold"]
for i in n:
    search.send_keys(i)
    wsh.SendKeys('{Enter}')
    drive=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
    drive.click()
    while(1):
        response=driver.page_source
        time.sleep(5)
        soup=BeautifulSoup(response,'lxml')

        current=soup.find(class_="ytp-time-current")
        last=soup.find(class_='ytp-time-duration')
        if current.text==last.text:
            continue