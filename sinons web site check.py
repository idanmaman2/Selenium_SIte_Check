from selenium import webdriver
import tkinter 
import time
import threading 
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
now = datetime.datetime.now()
print(now)
time.sleep(2)
import csv
import difflib
from selenium.webdriver.chrome.options import Options
TIMES2=1
TIMES3= 1000
proc= 0 
text2="" 

time.sleep (10 )
def check (t) :
    for i in t :
        if i.is_alive():
            return False
    return True 
def translate():
    global proc 
    global b 
    options = Options()
    options.add_argument('--headless')
 
    webpage = r"https://lottery-experiment-test.herokuapp.com/" # edit me
    driver = webdriver.Chrome(executable_path=r"D:\chromedriver.exe" )
    wait = WebDriverWait(driver, 10)

    driver.get(webpage)
    sbox = driver.find_element_by_id("template_num")
    sbox.send_keys('7')
    sbox.send_keys(Keys.ENTER)
    x=[] 
  
 
       
       
    print("good")
    driver.refresh()
    submit1 = driver.find_element_by_name("first_name")
    submit1.send_keys("will it crash? ;)  IDHM©")

    submit2 = driver.find_element_by_name("last_name")
    submit2.send_keys(" will it crash? ;)  IDHM©")
 
    submit3 = driver.find_element_by_name("age")
    submit3.send_keys(19)
    submit4 = driver.find_element_by_id("send_metadata")
    submit4.click()        
    submit5 = driver.find_element_by_id("close_pre_img") 
    submit5.click() 
    submit6 = driver.find_element_by_id("send_card")
    submit6.click() 
    submit7 = driver.find_element_by_id("send_comment")
    submit7.click()
 
    driver.quit()
     
j=0
while(True) : 
    print(j) 
    threads = []
    for i in range(20): 
        threads.append(threading.Thread(target=translate) )
    for thread in threads:
     thread.start()
    while(not(check(threads))) :
        pass
    j+=1 





 
