from selenium import webdriver
def supplyDriver(browser):
    if browser == "chrome":
        return webdriver.Chrome(executable_path=r"C:\Selenium\Drivers\chromedriver.exe")
    elif browser == "firefox":
        return webdriver.Firefox(executable_path=r"C:\TestToolsSoftware\Browser Drivers\geckodriver.exe")
    elif browser == "IE":
        return webdriver.Ie(executable_path=r"C:\TestToolsSoftware\Browser Drivers\IEDriverServer.exe")
    else:
        return None
