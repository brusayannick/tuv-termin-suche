import time
import telegram_send
from plyer import notification
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def termin(gebiet):
    option=webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('incognito')
    driver = webdriver.Chrome(executable_path=r"C:\Users\yanni\OneDrive\Code\Projects\Python\Selenium\chromedriver.exe", chrome_options=option)
    driver.set_window_size(1920, 1080)

    driver.get("https://www.tuv.com/germany/de/termin-führerschein/")

    wait()

    driver.execute_script("CookieSettingsAcceptAll()")

    ort = driver.find_element_by_id("input_hutvLocation")
    ort.clear()
    ort.send_keys(gebiet)
    ort.send_keys(Keys.ARROW_DOWN)
    ort.send_keys(Keys.ENTER)

    wait()

    weiter = driver.find_element_by_xpath("//div[@class='tuv-hutv__steptwo--buttons']//div[@class='tuv-hutv--next-step-license-driver']")
    weiter.click()

    wait()

    driver.execute_script("document.getElementById('ui-datepicker-div').setAttribute('class', 'ui-datepicker ui-widget ui-widget-content ui-helper-clearfix ui-corner-all')")
    driver.execute_script("document.getElementById('ui-datepicker-div').setAttribute('style', 'position: absolute; top: 700px; left: 24.6875px; z-index: 1; display: block;')")

    wait()

    vor = driver.find_element_by_xpath("//div[@class='ui-datepicker-header ui-widget-header ui-helper-clearfix ui-corner-all']//a[@title='<zurück']")
    wait()
    vor.click()

    wait()

    vor = driver.find_element_by_xpath("//div[@class='ui-datepicker-header ui-widget-header ui-helper-clearfix ui-corner-all']//a[@title='Vor>']")
    wait()
    vor.click()

    wait()
    frei = driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//td[@class='ui-datepicker-unselectable ui-state-disabled']")

    o=0
    for i in frei:
        o+=1
    return o

    driver.close()

def main():
    cntnach1 = 0
    cntnach2 = 0
    while True:
        cntvor1 = termin("Düsseldorf")
        if cntvor1>cntnach1:
            notification.notify(title = "Neue Theoriestunden!", message = "Neue Theoriestunden in Düsseldorf")
            telegram_send.send(messages=["Neue Theoriestunden in Düsseldorf!"])
        cntnach1 = cntvor1

        wait()

def wait():
    time.sleep(3)

main()
