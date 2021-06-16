# conding: utf-8
# email: qfsfdxlqy@163.com
# GitHub: https://github.com/2015qyliang

from selenium import webdriver
import pyautogui
import time
import glob

# http://npm.taobao.org/mirrors/chromedriver/
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.ezbiocloud.net/16SrRNA_list?tn=Root')
# change "show ** entries"
time.sleep(60)

filepath = 'C:/Users/lqy/Downloads/'
for i in range(1,661):
	driver.find_element_by_link_text(str(i)).click()
	time.sleep(3)
	print('-- Ongoing:', i, '--')
	# driver.findElement(By.linkText(str(i)).click()
	pyautogui.hotkey('ctrl', 's')
	time.sleep(1)
	pyautogui.typewrite( "ezbiocloudpage_" + str(i))
	time.sleep(1)
	pyautogui.press('enter')
	pyautogui.press('enter')
	j = 1
	while len(glob.glob(filepath + '*_' + str(i) + '.html')) == 0:
		time.sleep(1)
		print('-- Waiting for', str(i), '-->', str(j))
		j += 1
	print('-- Dowbloaded Page:', i, '--')

