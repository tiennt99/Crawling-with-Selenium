from selenium import webdriver

import time
USERNAME = 'kapfoodnow@gmail.com'
PASSWORD = '12345678'
UserInput = "https://merchant.now.vn/order/export-restaurant"
options = webdriver.ChromeOptions()
options.add_argument("download.default_directory=C:\\Users\\HuuTien\\OneDrive\\Đồ Án")
options.add_argument("--headless")
driver = webdriver.Chrome('./chromedriver')

# open the website
driver.get(UserInput)
driver.implicitly_wait(25)
nextPageButton = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/button')
nextPageButton.click()
user_name_text = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div[4]/div[1]/div[1]/input')
user_name_text.send_keys(USERNAME)
password_text = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div[4]/div[1]/div[2]/input')
password_text.send_keys(PASSWORD)
submit = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div[4]/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div/div/div/div[1]').click()
time.sleep(2)
try:
    driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div/div/div[2]').click()
    time.sleep(1)
except Exception as e:
    print(e.__str__())
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/ul/li[3]/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/ul/li[3]/ul/li[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/section/div[1]/div/div/div[4]/button').click()
time.sleep(10)
driver.find_element_by_xpath(f'//*[@id="app"]/div/div/div[1]/section/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(10)

driver.close()
Initial_path = '\\'
import os
filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
print(filename)

import json
import requests
headers = {"Authorization": "Bearer ya29.a0AfH6SMAEoF0Do48LghWiD6vZB3hC4dWc9gzVc4DYzkcQhWTgcR-TnUIJBTYufsHgpRSkH7SqqDWeF12AOLh37O7yp5Yxl4CFQ5rAlluT3Oqy7YID7odLCNxlyD94BKFLs_lEG6JakMxmfmDyxcl-igJT3bwy"}
para = {
    "name": filename,
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open(filename, "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
