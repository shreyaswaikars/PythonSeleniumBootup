from selenium import webdriver
email="ataps@ataps.com"
pwd="password"
driver=webdriver.Chrome("C:\Selenium\Drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://demowebshop.tricentis.com/")
driver.find_element_by_link_text("Log in").click()
driver.find_element_by_id("Email").send_keys(email)
driver.find_element_by_id("Password").send_keys(pwd)
driver.find_element_by_xpath(".//input[@value='Log in']").click()
if(driver.find_element_by_xpath(".//a[@class='account']").text == email):
    print("Test pass")
    driver.find_element_by_link_text("Log out")
    driver.close()
else:
    print("Test failed")
    driver.close()