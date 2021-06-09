from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import threading 
import bs4 as bs
import csv
import eel
import urllib
import requests
import re
import json
import validators

eel.init("web")

@eel.expose
def getMeTheLinks(queryToAsk, numberOfPages):
    
    numberOfPages = int(numberOfPages)
    queryToAsk = queryToAsk.replace(" ", "%20")

    browser= webdriver.Chrome('chromedriver')

    browser.get('https://www.linkedin.com')
    sleep(1)

    userid = browser.find_element_by_xpath(".//*[@id='session_key']")
    userid.send_keys('devangtechcurve@gmail.com')
    sleep(1)
    userpass = browser.find_element_by_xpath(".//*[@id='session_password']")
    userpass.send_keys('Admin@123')
    sleep(1)
    userpass = browser.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/button")
    userpass.click()

    sleep(5)

    lstOfCompanyLinks = []

    #indian companies

    for i in range(numberOfPages):
        if i == 0:
            thatLink = "https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102713980%22%5D&keywords=" + queryToAsk + "&origin=FACETED_SEARCH"
        else:
            thatLink = "https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102713980%22%5D&keywords=" + queryToAsk + "&origin=FACETED_SEARCH"+"&page="+str(i+1)
        sleep(1)
        
        browser.get(thatLink)
        sleep(2)
        valData = browser.page_source

        allCompanyLinks = re.findall(r"https:\/\/www\.linkedin\.com\/company\/.*?\/", valData)

        lstOfCompanyLinks += list(set(allCompanyLinks))
        
        sleep(0.1)
    
    #unique list of all company links on linkedIn    
    lstOfCompanyLinks = list(set(lstOfCompanyLinks))
    
    companyToEmployees = {}
    companyToAbout = {}
    
    for company in lstOfCompanyLinks:
        companyAboutUs = company+"about/"
        browser.get(companyAboutUs)
        
        sleep(2)
        aboutUsPage = browser.page_source
        
        try:
            websiteName = re.findall(r"\<span class\=\"link\-without\-visited\-state\" dir\=\"ltr\"\>.*?\<\/span\>", aboutUsPage, re.MULTILINE | re.DOTALL)[0]
            websiteName = websiteName.split(">")[1].strip()
            websiteName = websiteName.split("<")[0].strip()
        except:
            websiteName = ""
            
        
            
        print(websiteName)
        
        # f = open("aboutUs.txt", "w")
        # f.write(aboutUsPage)   
        # f.close()
        
        # break

eel.start('main.html', size=(1000, 1000))
