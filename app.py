# %%
# installing_library's
# !pip install selenium chromedriver_autoinstaller pandas undetected_chromedriver


# %%

# importing libraries
import time
import undetected_chromedriver as uc
from selenium import webdriver
import csv
import urllib.request as req
import random
from datetime import datetime
import pathlib
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv
import chromedriver_autoinstaller
import pandas as pd
import os

# opening chrome
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.realtor.com/')

# %%
# main code

def capcha_solver():
    try:
        driver.find_element(By.CSS_SELECTOR,'#px-captcha')
        print('Please Solve The Capcha....')
        time.sleep(1)
    except:
        return False
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR,'#px-captcha')
            time.sleep(1)
        except:
            print('Capcha Solved')
            return False
# capcha solver


# read the datafile if exists otherwise create a new one


def scrap_init():
    if os.path.exists('./data.csv'):
        df=pd.read_csv('./data.csv')
    else:
        df=pd.DataFrame(columns=['name','location','phone','sold'])
    print('Scrapping initialized.....')
    try:
        driver.find_element(By.CSS_SELECTOR,'#agent_list_wrapper')
    except:
        print('No Agents List found')
        return False
    realators=driver.find_element(By.CSS_SELECTOR,'.search-result > span').text
    pages=driver.find_elements(By.CSS_SELECTOR,'[aria-label="pagination"] a')
    pages=pages[-2].text
    print('#Info: ',realators.upper(),' And ',pages,' Pages Found')
    try:
        driver.find_element(By.CSS_SELECTOR,'#agent_list_wrapper')
    except:
        return "Couldn't found Agent list."
    
    while True:
        pages=driver.find_elements(By.CSS_SELECTOR,'[aria-label="pagination"] a')
        pages=pages[-2].text
        capcha_solver()
        for row in driver.find_elements(By.CSS_SELECTOR,'#agent_list_wrapper .cardWrapper > ul > div'):
            name_node=row.find_elements(By.CSS_SELECTOR,'.agent-name')
            name=''
            for n in name_node:
                name+=n.text
            # name formatting
            
            phone_node=row.find_elements(By.CSS_SELECTOR,'.agent-phone')
            phone=''
            for n in phone_node:
                phone+=n.text
            # phone formatting


            details=row.find_elements(By.CSS_SELECTOR,'.agent-detail-item')
            sold='N/A'
            for s in details:
                if 'sold' in s.text.lower():
                    sold=s.text.split(' ')[1]
            # sold formatting


            group_node=row.find_elements(By.CSS_SELECTOR,'.agent-group')
            group=''
            for n in group_node:
                group+=n.text
            # group formatting


            row=[name,group,phone,sold]
            # df=df.append(row,ignore_index=True)
            df.loc[len(df)] = row # only use with a RangeIndex!
        df.to_csv('data.csv',index=False)

        current_page=driver.find_element(By.CSS_SELECTOR,'[aria-label="pagination"] a.current').text
        print('Scrapping Current Page:',current_page)
        if pages==current_page:
            print('Scraping Done')
            return df
        
        click=False
        for pag in driver.find_elements(By.CSS_SELECTOR,'[aria-label="pagination"] a'):
            if click==True:
                pag.click()
                break
            if pag.text==current_page:
                click=True
                
        
        
       
            


    
# scapping intilized

scrap_init()

# %%
for name in driver.find_elements(By.CSS_SELECTOR,'.agent-name'):
    print(0,name.text)


