from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://www.instagram.com")

time.sleep(3)
#giris_yap = browser.find_element_by_xpath("//*[@id='mount_0_0_JJ']/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[2]/p/a/font/fon")
#giris_yap.click()

username = browser.find_element(By.NAME, 'username')
password = browser.find_element(By.NAME, 'password')

username.send_keys("") #kullanici adi
password.send_keys("")   #sifre

time.sleep(2)

giris_yap = browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
giris_yap.click()

time.sleep(10)
browser.close()
