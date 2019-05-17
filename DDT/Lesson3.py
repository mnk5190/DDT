import openpyxl
from selenium import webdriver
import DDT.XUtils

path = "C:/Users/khan/Desktop/QA/Data driven testing/Login.xlsx"

driver = webdriver.Chrome(executable_path="C:/Users/khan/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
rows = DDT.XUtils.getRowCount(path, "Sheet1")

# r represents the row number
for r in range(2, rows+1):
    username = DDT.XUtils.readData(path, "Sheet1", r, 1)
    password = DDT.XUtils.readData(path, "sheet1", r, 2)

    driver.find_element_by_xpath("//input[@name='userName']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//input[@name='login']").click()


    if driver.title == "Find a Flight: Mercury Tours:":
        print("Test has passed")
        DDT.XUtils.writeData(path, "Sheet1", r, 3, "PASS")
    else:
        print("Test has failed!")
        DDT.XUtils.writeData(path, "Sheet1", r, 3, "FAIL")

    driver.find_element_by_xpath("//a[contains(text(),'Home')]").click()




