from selenium import webdriver
d=webdriver.Chrome(r"C:\Selenium\Drivers\chromedriver.exe")
d.implicitly_wait(10)
d.get("https://agiletestingalliance.org/")
d.find_element_by_link_text("CHAPTERS").click()