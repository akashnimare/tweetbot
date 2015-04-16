from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
print "Opening browser"
driver = webdriver.Chrome()
driver.get("https://www.twitter.com")
time.sleep(3)
print "Logging into Twitter"
form = driver.find_element_by_class_name('front-signin')
username = form.find_element_by_name("session[username_or_email]")
username.send_keys('Paste your username')
password = form.find_element_by_name("session[password]")
password.send_keys('Password Madafakar')
password.send_keys(Keys.RETURN)
print "Logged into twitter"
time.sleep(5)
form = driver.find_element_by_class_name('timeline-tweet-box')
tweet =form.find_element_by_id("tweet-box-home-timeline")
print "Let's tweet"
tweet.send_keys('Tweeting using selenium #python #selenium')
driver.find_element_by_xpath("//form[@class='t1-form tweet-form']//div[@class='tweet-button']/button").click(); 
print "Yeahh"
