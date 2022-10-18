#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 21:36:43 2022

@author: madhavsharma
"""


## Importing required libraries
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


## Initializing a scraper class
class scraper():
    
    ## Initializing variables
    global driver, df
    driver = webdriver.Safari()
    
    
    ## Function to open the specified URL
    def openURL():
        baseURL = ('https://www.enr.com/toplists/2019-Top-100-CM-for-Fee-Firms')
        driver.get(baseURL)
        driver.maximize_window()
         
    
    ## Function to scrape the data into csv
    def scrape():
        ## Handle Pop-ups
        cookies = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/section/div/div/form/input[4]")
        cookies.click()
        sleep(2)
        
        ## Column XPATHS
        rank_2019 = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
        rank_2018 = driver.find_elements(By.XPATH, "//tbody/tr/td[2]")
        firms = driver.find_elements(By.XPATH, "//tbody/tr/td[3]")
        firm_type = driver.find_elements(By.XPATH, "//tbody/tr/td[4]")
        revenue_2018 = driver.find_elements(By.XPATH, "//tbody/tr/td[5]")
        
        
        ## Iterating and saving scraped data into a Dataframe
        Construction_Firms_Data = []
        for i in range(len(rank_2019)):
            temp = {'Rank_2019' : rank_2019[i].text,
                    'Rank_2018' : rank_2018[i].text,
                    'Firm'      : firms[i].text,
                    'Firm_Type' : firm_type[i].text,
                    'Total_2018_Revenue($ MILL.)' :revenue_2018[i].text
                    }
            Construction_Firms_Data.append(temp)
        
        
        ## Finally loading the data into the Dataframe
        df = pd.DataFrame(Construction_Firms_Data)
        print(df)
        
        
        ## Exporting DataFrame to CSV
        df.to_csv('Construction_Firms_Data.csv')
    
    
    ## Calling functions
    openURL()
    scrape()
        
