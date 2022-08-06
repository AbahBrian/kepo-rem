import requests
import os
import schedule
import time
import pandas as pd

from datetime import datetime
from datetime import datetime as dt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger

sched = BlockingScheduler()

trigger = OrTrigger([CronTrigger(day_of_week='mon-sun', hour='16', minute='30')])
trigger2 = OrTrigger([CronTrigger(day_of_week='mon-sun', hour='19', minute='00')])
trigger3 = OrTrigger([CronTrigger(day_of_week='mon-sun', hour='21', minute='00')])
trigger4 = OrTrigger([CronTrigger(day_of_week='mon-sun', hour='23', minute='00')])     

@sched.scheduled_job(trigger)
def scheduled_job():
    
    opt = Options()
    opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    opt.add_argument("--headless")
    opt.add_argument("--disable-extensions")
    opt.add_argument("--disable-gpu")
    opt.add_argument("--no-sandbox")
    opt.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)

    driver.get("https://ieiapps.epson.biz/kepo/Progress")

    time.sleep(5)
    driver.find_element(By.NAME, "username").send_keys("iei41008")
    time.sleep(5)
    driver.find_element(By.NAME, "password").send_keys("Jinmarusaja123*")
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR,"input[type=\"submit\"i]").click()

    time.sleep(10)

    try:
            login = driver.find_element(By.XPATH,"//h3[@class='display-5']")    
            if login.is_displayed():
                print ("Anda Berhasil Login")
    except NoSuchElementException:
            print ("Ada Masalah Saat Login, Pastikan ID dan Password Benar") 

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='E3 PRODUCT ENGINEERING DEPT']"))).click()

    name_list = []
    curl_list = []

    curl = (driver.find_elements(By.XPATH,"//table[@id='progress']/tbody/tr/td[4]"))

    for value in curl:
            curl_list.append(value.text)

    name = (driver.find_elements(By.XPATH,"//table[@id='progress']/tbody/tr/td[2]"))

    for value in name:
            name_list.append(value.text)



    df = pd.DataFrame(curl_list,name_list,columns=['KEPO'])

    df1 = df[df['KEPO']<='1'] 

    rss = df1.to_string(index = True)

    print(rss)

    url = "https://wa-api-kope.herokuapp.com/send-group-message"

    payload={
    'id': '120363041834899854@g.us',
    'message': 'Assalamualaikum, Berikut adalah Nama Teman-Teman yang belum closed Kepo' + '\n' + rss}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print (response)

    driver.quit()

@sched.scheduled_job(trigger2)
def scheduled_job():
    
    opt = Options()
    opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    opt.add_argument("--headless")
    opt.add_argument("--disable-extensions")
    opt.add_argument("--disable-gpu")
    opt.add_argument("--no-sandbox")
    opt.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)

    driver.get("https://ieiapps.epson.biz/kepo/Progress")

    time.sleep(5)
    driver.find_element(By.NAME, "username").send_keys("iei41008")
    time.sleep(5)
    driver.find_element(By.NAME, "password").send_keys("Jinmarusaja123*")
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR,"input[type=\"submit\"i]").click()

    time.sleep(10)

    try:
            login = driver.find_element(By.XPATH,"//h3[@class='display-5']")    
            if login.is_displayed():
                print ("Anda Berhasil Login")
    except NoSuchElementException:
            print ("Ada Masalah Saat Login, Pastikan ID dan Password Benar") 

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='E3 PRODUCT ENGINEERING DEPT']"))).click()

    name_list = []
    curl_list = []

    curl = (driver.find_elements(By.XPATH,"//table[@id='progress']/tbody/tr/td[4]"))

    for value in curl:
            curl_list.append(value.text)

    name = (driver.find_elements(By.XPATH,"//table[@id='progress']/tbody/tr/td[2]"))

    for value in name:
            name_list.append(value.text)



    df = pd.DataFrame(curl_list,name_list,columns=['KEPO'])

    df1 = df[df['KEPO']<='1'] 

    rss = df1.to_string(index = True)

    print(rss)

    url = "https://wa-api-kope.herokuapp.com/send-group-message"

    payload={
    'id': '120363041834899854@g.us',
    'message': 'Assalamualaikum, Berikut adalah Nama Teman-Teman yang belum closed Kepo' + '\n' + rss}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response)

    driver.quit()

@sched.scheduled_job(trigger3)
def scheduled_job():
    
    opt = Options()
    opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    opt.add_argument("--headless")
    opt.add_argument("--disable-extensions")
    opt.add_argument("--disable-gpu")
    opt.add_argument("--no-sandbox")
    opt.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)

    driver.get("https://ieiapps.epson.biz/kepo/Progress")

    time.sleep(5)
    driver.find_element(By.NAME, "username").send_keys("iei41008")
    time.sleep(5)
    driver.find_element(By.NAME, "password").send_keys("Jinmarusaja123*")
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR,"input[type=\"submit\"i]").click()

    time.sleep(10)

    try:
            login = driver.find_element(By.XPATH,"//h3[@class='display-5']")    
            if login.is_displayed():
                print ("Anda Berhasil Login")
    except NoSuchElementException:
            print ("Ada Masalah Saat Login, Pastikan ID dan Password Benar") 

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='E3 PRODUCT ENGINEERING DEPT']"))).click()

    name_list = []
    curl_list = []

    curl = (driver.find_elements(By.XPATH,"//table[@id='progress']/tbody/tr/td[4]"))

    for value in curl:
            curl_list.append(value.text)

    name = (driver.find_elements(By.XPATH,"//table[@id='progress']/tbody/tr/td[2]"))

    for value in name:
            name_list.append(value.text)



    df = pd.DataFrame(curl_list,name_list,columns=['KEPO'])

    df1 = df[df['KEPO']<='1'] 

    rss = df1.to_string(index = True)

    print(rss)

    url = "https://wa-api-kope.herokuapp.com/send-group-message"

    payload={
    'id': '120363041834899854@g.us',
    'message': 'Assalamualaikum, Berikut adalah Nama Teman-Teman yang belum closed Kepo' + '\n' + rss}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response)

    driver.quit()

@sched.scheduled_job(trigger4)
def scheduled_job():
    
    opt = Options()
    opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    opt.add_argument("--headless")
    opt.add_argument("--disable-extensions")
    opt.add_argument("--disable-gpu")
    opt.add_argument("--no-sandbox")
    opt.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)

    driver.get("https://ieiapps.epson.biz/kepo/Progress")

    time.sleep(5)
    driver.find_element(By.NAME, "username").send_keys("iei41008")
    time.sleep(5)
    driver.find_element(By.NAME, "password").send_keys("Jinmarusaja123*")
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR,"input[type=\"submit\"i]").click()

    time.sleep(10)

    try:
            login = driver.find_element(By.XPATH,"//h3[@class='display-5']")    
            if login.is_displayed():
                print ("Anda Berhasil Login")
    except NoSuchElementException:
            print ("Ada Masalah Saat Login, Pastikan ID dan Password Benar") 

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='E3 PRODUCT ENGINEERING DEPT']"))).click()

    name_list = []
    curl_list = []

    curl = (driver.find_elements(By.XPATH,"//table[@id='progress']/tbody/tr/td[4]"))

    for value in curl:
            curl_list.append(value.text)

    name = (driver.find_elements(By.XPATH,"//table[@id='progress']/tbody/tr/td[2]"))

    for value in name:
            name_list.append(value.text)



    df = pd.DataFrame(curl_list,name_list,columns=['KEPO'])

    df1 = df[df['KEPO']<='1'] 

    rss = df1.to_string(index = True)

    print(rss)

    url = "https://wa-api-kope.herokuapp.com/send-group-message"

    payload={
    'id': '120363041834899854@g.us',
    'message': 'Assalamualaikum, Berikut adalah Nama Teman-Teman yang belum closed Kepo' + '\n' + rss}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response)

    driver.quit()

sched.start() 

