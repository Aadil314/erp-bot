from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
PATH = "C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://erp.iitkgp.ac.in/SSOAdministration/login.htm?sessionToken=8FD3F295869EAD1CD68CBABC80D704B1.worker1&requestedUrl=https://erp.iitkgp.ac.in/IIT_ERP3/")
driver.maximize_window()

# Login to the Institute ERP website. Note: login credentials have been changed 
# NOTE: if you want to use this app, make changes to your login credentials
user_id = driver.find_element("id","user_id")
user_id.send_keys("***(roll no. here)")
password = driver.find_element("id","password")
password.send_keys("***(password here)")
time.sleep(1)
ques = driver.find_element("id","question")
question = ques.text
ans = driver.find_element("id","answer")
if question == "***(question here)":
    ans.send_keys("***(answer here)")
elif question == "***(question here)":
    ans.send_keys("***(answer here)")
else:
    ans.send_keys("***(answer here)")
time.sleep(1)

# Getting into CDC portal, where the company names are listed
driver.find_element("id","loginFormSubmitButton").click()
driver.implicitly_wait(2)
elements = driver.find_elements("tag name","strong")
for element in elements:
    if "CDC" in element.text:
        CDC = element
CDC.click()
time.sleep(0.5)
student = driver.find_element("class name","text-primary")
student.click()
time.sleep(0.5)
AFI = driver.find_elements("class name","text-default")[0]
AFI.click()
driver.implicitly_wait(2)
driver.switch_to.frame("myframe")
html = driver.find_element("id",'grid37')

# Looping till all the company names are printed along with serial number
c = 0
while True:
    companies = driver.find_elements("id",str(c))
    if len(companies)!=0:
        tds = companies[0].find_elements("tag name",'td')
        print(c+1,tds[1].text)
        c += 1
    else:
        html.send_keys(Keys.PAGE_DOWN)
        html.send_keys(Keys.PAGE_DOWN)
        # time.sleep(0.5)
        if len(driver.find_elements("id",str(c)))!=0:
            continue
        else:
            break
time.sleep(1)

# Checking if there is any change in the number of companies listed and notifying in case new entries are found
with open('data.txt', 'r') as f:
    data = f.read()

num = int(data)

if(num < c):
    with open('data.txt', 'w') as f:
        f.write(str(c))
    print("New entry found!")

time.sleep(5)

driver.close()