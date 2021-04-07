from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\chintu\PycharmProjects\FirstSeleniumTest\drivers\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("https://www.google.com/ ")
driver.find_element_by_name("q").send_keys("Linkedin")
driver.maximize_window()
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
elem1=driver.find_element_by_class_name("LC20lb")
elem1.click()
elem2=driver.find_element_by_class_name("nav__button-secondary")
elem2.click()
elem3=driver.find_element_by_name("session_key")
elem3.click()
driver.find_element_by_name("session_key").send_keys("youremailhere")
driver.find_element_by_name("session_password").send_keys("your pass")

e1=driver.find_element_by_xpath("/html/body/div/main/div/form/div[3]/button")
e1.click()
time.sleep(5)
e2=driver.find_element_by_xpath("/html/body/div[5]/div[5]/div[3]/div/div/div/div/div[1]/div/div[1]/button[1]")
e2.click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[5]/div[5]/div[3]/div/div/div/div/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]").send_keys("Hello Welcome to Automation Testing")
e3=driver.find_element_by_xpath("/html/body/div[5]/div[5]/div[3]/div/div/div/div/div[1]/div[2]/div/div[1]/div[2]/button/span")
e3.click()
time.sleep(4)
e4=driver.find_element_by_xpath("/html/body/div[5]/div[5]/div[3]/div/div/div/div/div[1]/div[2]/div/div[1]/fieldset/ul/li[3]/button/div")
e4.click()
e5=driver.find_element_by_xpath("/html/body/div[5]/div[5]/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/div/button/span")
e5.click()
# post succesfully

# click profile photo
e6=driver.find_element_by_xpath("/html/body/div[5]/div[5]/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/button/span")
e6.click()
time.sleep(3)
#e7=driver.find_element_by_xpath("/html/body/div[5]/div[5]/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div[2]/artdeco-dropdown/artdeco-dropdown-trigger/li-icon/svg")
#e7.click()
#e8=driver.find_element_by_xpath("/html/body/div[5]/div[5]/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div[2]/artdeco-dropdown/artdeco-dropdown-content/ul/li[3]/artdeco-dropdown-item/div/span[1]")
#e8.click()
# view profile photo
a1=driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[6]/div/div/button/div/span")
a1.click()
time.sleep(4)
a2=driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[6]/div/div/ul/li[1]/a/div[2]/span")
a2.click()
time.sleep(3)
#view successfully


a3=driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[2]/a/span[1]")
a3.click()
time.sleep(3)
a4=driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[4]/a/span[1]")
a4.click()

a1.click()
b1=driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[6]/div/div/ul/li[4]/ul/li[1]/a")
b1.click()
time.sleep(3)
b2=driver.find_element_by_xpath("/html/body/div[5]/div[5]/div[3]/div/div/div/div/div/div[1]/nav/button[3]/span")
b2.click()
time.sleep(3)
a11=driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[3]/a/span[1]")
a11.click()
s1=driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[3]/a/span[1]")
s1.click()
time.sleep(4)
a1.click()
a22=driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[6]/div/div/ul/li[2]/ul/li[1]/a")
a22.click()

time.sleep(5)

#m1= driver.find_element_by_xpath("/html/body/div/main/div[2]/nav/div/ul/li[1]/a")
#m1.click()

#a44 = driver.find_element_by_class_name("heading")
#a44.click()
#driver.find_element_by_xpath("/html/body/div/main/div[2]/div/div/ul/li[4]/div/div/form/fieldset[1]/input").send_keys("Pranita15")
#driver.find_element_by_xpath("/html/body/div/main/div[2]/div/div/ul/li[4]/div/div/form/fieldset[1]/div[2]/input").send_keys("Chaitanya12")
#driver.find_element_by_xpath("/html/body/div/main/div[2]/div/div/ul/li[4]/div/div/form/fieldset[1]/div[4]/input").send_keys("Chaitanya12")
#a123=driver.find_element_by_xpath("/html/body/div/main/div[2]/div/div/ul/li[4]/div/div/form/div/button")
#a123.click()
a1.click()

b3=driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[6]/div/div/ul/li[5]/ul/li/a")
b3.click()

time.sleep(4)
driver.quit()
print("Test is completed successfully")
