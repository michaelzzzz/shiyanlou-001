#coding=utf-8
from datetime import time
from time import sleep

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.lphtsccft.zlqqt2'
desired_caps['appActivity'] = 'com.lphtsccft.zlg.startup.ZlgGuidePageActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    permit_button = driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')

except NoSuchElementException:
    print('no permit_button')
else:
    permit_button.click()

try:
    confirm_button = driver.find_element_by_id('com.lphtsccft.zlqqt2:id/guide_page_tv_confirm')
except NoSuchElementException:
    print('no confirm_button')
else:
    confirm_button.click()

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y

l = get_size()
print(l)

def swiptleft():
    l = get_size()
    x1 = int(l[0]*0.9)
    x2 = int(l[0]*0.1)
    y1 = int(l[1]*0.5)
    driver.swipe(x1,y1,x2,y1,1000)

sleep(1)
for i in range(3):
    swiptleft()
    sleep(0.5)

sleep(1)


def touch_tap(x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
    '''
    method explain:点击坐标
    parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
    Usage:
        device.touch_tap(277,431)      #277.431为点击某个元素的x与y值
    '''
    screen_width = driver.get_window_size()['width']  # 获取当前屏幕的宽
    screen_height = driver.get_window_size()['height']  # 获取当前屏幕的高
    a = (float(x) / screen_width) * screen_width
    x1 = int(a)
    b = (float(y) / screen_height) * screen_height
    y1 = int(b)
    driver.tap([(x1, y1), (x1, y1)], duration)

touch_tap(l[0]*0.5,l[1]*0.9375)

sleep(1)

try:
    close_button = driver.find_element_by_id('com.lphtsccft.zlqqt2:id/ipo_dialog_close')
except NoSuchElementException:
    print("no close_button")
else:
    close_button.click()

