from selenium import webdriver
import time
def test_tabs_open_close():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.w3schools.com/") #first_tab
        first_tab = driver.window_handles[0]
        driver.execute_script("window.open('https://www.pzu.com.ua/')") #second_tab
        second_tab = driver.window_handles[1]
        driver.execute_script("window.open('https://www.ilovepdf.com/uk/')") #third_tab
        third_tab = driver.window_handles[2]
        driver.execute_script("window.open('https://anc.ua/')") #forth_tab
        forth_tab = driver.window_handles[3]
        driver.execute_script("window.open('https://rozetka.com.ua/ua/')") #fifth_tab
        fifth_tab = driver.window_handles[4]
        time.sleep(10)

        driver.switch_to.window(third_tab)
        driver.close()
        time.sleep(3)
        driver.switch_to.window(fifth_tab)
        driver.close()
        time.sleep(3)
        driver.switch_to.window(first_tab)
        driver.close()
        time.sleep(3)
        driver.switch_to.window(forth_tab)
        driver.close()
        time.sleep(3)
        driver.switch_to.window(second_tab)
        driver.close()
        time.sleep(3)
    finally:
        driver.quit()

