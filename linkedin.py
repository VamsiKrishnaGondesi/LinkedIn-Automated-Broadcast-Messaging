#LinkedIn Automated Broadcast Messaging.
#Source Code.

#Importing selenium mmodule, time module.

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#To be specific when you run chrome in headless mode you need to include flag --no-sandbox:

Chrome_Options = Options().add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path="/path to chromedriver executable file/",chrome_options=Chrome_Options)

#Message compose window pop-up

driver.get('https://www.linkedin.com/messaging/compose/')
time.sleep(50)

#Accessing textarea to input users.

text_area = driver.find_element_by_id('ember/xx/-search-field')
i=['/receiver users usernames/']

#Inputting users via the ember field key.

for j in i:

    text_area.send_keys(j)
    time.sleep(3)
    text_area.send_keys( Keys.RETURN)
    time.sleep(3)



time.sleep(5)

#webdriver.ActionChains(driver).move_to_element_with_offset(text_area,356,748).click().perform()
#Input message at the message compose.
time.sleep(5)
active_ele = driver.switch_to.active_element
active_ele.send_keys("Hello! This message is to test my code. If you are able to look at this message, I am successful!")
time.sleep(3)

#If xpath == msg form class, then send he message by clicking send button.

el3 = driver.find_element_by_xpath("//*[@class='msg-form__send-button artdeco-button artdeco-button--1']")
el3.click()
