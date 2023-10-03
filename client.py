import os
import sys
import signal
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from pyvirtualdisplay import Display
from time import sleep


display = Display(visible=0, size=(800,600))
display.start()

options=Options()
chrome_driver = '../abr_browser_dir/chromedriver'
# options.add_argument('--user-data-dir=' + chrome_user_dir)
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_driver, chrome_options=options)

url = 'http://' + '100.64.0.1/myindex_' + 'RL' + '.html'
driver.get(url)

page_title = driver.title

# Print the title
print("Page Title:", page_title)


sleep(1000)
	
driver.quit()
display.stop()