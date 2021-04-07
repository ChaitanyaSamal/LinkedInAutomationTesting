from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\chintu\PycharmProjects\FirstSeleniumTest\drivers\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("https://onlinecourses-archive.nptel.ac.in/ ")
#driver.find_element_by_name("q").send_keys("Linkedin")

#driver = webdriver.Chrome(r"C:\Users\Yogesh\Downloads\chromedriver.exe")
driver.get("https://onlinecourses-archive.nptel.ac.in/")
driver.maximize_window()
print (driver.title)
#driver.find_element_by_id("input").send_keys("python")
driver.find_element_by_link_text("Login").click()
print (driver.title)
userID = driver.find_element_by_id("identifierId")
userID.send_keys("thakurrushikesh068@gmail.com")
driver.find_element_by_class_name("CwaK9").click()
#driver.find_element_by_id("yDmH0d")
time.sleep(3)
a1=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
a1.send_keys("kabsjsnajsnkas")