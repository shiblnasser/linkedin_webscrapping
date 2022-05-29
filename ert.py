from typing import final
from selenium import webdriver
import time

import xlrd

text_file = open("output.txt", 'a')
text_file.write("\n\n")


workbook = xlrd.open_workbook('C:\\Users\\SHIBL NASSER\\Downloads\\linkedin.xls')
worksheet = workbook.sheet_by_name('Sheet1')



driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://www.linkedin.com/login")

time.sleep(1)

driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[1]/input').send_keys('emial@gmail.com')
driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[2]/input').send_keys('Password')
driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()


for i in range(worksheet.nrows):
    value = worksheet.cell(i, 0).value.strip()
    try:
        driver.get(value)
        text = ""
        try:
            text = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/h1').text
        except:
            text = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/h1').text
        
    except:
        text_file.write(" | ".join(temp) + "\n")
        print(x)
        continue




        
text_file.close()
