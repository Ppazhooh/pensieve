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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



client_up_time = int(sys.argv[1])
display = Display(visible=0, size=(800,600))
display.start()

options=Options()
chrome_driver = '../abr_browser_dir/chromedriver'
# options.add_argument('--user-data-dir=' + chrome_user_dir)
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_driver, chrome_options=options)


scheme = str(sys.argv[2])
# if scheme == 'robustMPC':
#     scheme = ''
# Replace the ip iddress with correct eno1 address of the machine!
url = 'http://' + '100.64.0.1/myindex_' + scheme + '.html'
driver.get(url)

# Wait up to 10 seconds for the videoPlayer element to be present
video = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "videoPlayer"))
)

video.click()

page_title = driver.title

# Print the title
print("Page Title:", page_title)


sleep(client_up_time)
	
driver.quit()
display.stop()
