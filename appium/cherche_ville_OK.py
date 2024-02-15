from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "14"
caps["appium:deviceName"] = "emulator-5556"
caps["appium:ANDROID_HOME"] = "C:\\Users\\Administrateur\\AppData\\Local\\Android\\Sdk"
caps["appium:JAVA_HOME"] = "C:\\Program Files\\Java\\jre-1.8"
caps["appium:appPackage"] = "com.graph.weather.forecast.channel"
caps["appium:appActivity"] = "activities.SettingActivity"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(10)

def cherche_ville_existe(nom_ville: str) -> bool :

    # click accepter permissions
    el1 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_one_time_button")
    el1.click()
    time.sleep(1)
    # changer le format heure (24h)
    el2 = driver.find_element(by=AppiumBy.ID, value="com.graph.weather.forecast.channel:id/tg_format_time_setting")
    el2.click()
    time.sleep(1)
    # cliquer sur le bouton accepter
    el3 = driver.find_element(by=AppiumBy.ID, value="com.graph.weather.forecast.channel:id/tvDone")
    el3.click()
    time.sleep(1)
    #Click on title in the search bar
    el4 = driver.find_element(by=AppiumBy.ID, value="com.graph.weather.forecast.channel:id/tvTitle")
    el4.click()
    time.sleep(1)
    #Click on "add location"
    el5 = driver.find_element(by=AppiumBy.ID, value="com.graph.weather.forecast.channel:id/ll_add_location")
    el5.click()
    time.sleep(1)
    #Click on search bar
    el6 = driver.find_element(by=AppiumBy.ID, value="com.graph.weather.forecast.channel:id/et_search_location")
    el6.click()
    time.sleep(1)
    #write "Lille" in the search bar
    el6.send_keys(nom_ville)
    time.sleep(5)
    try :
        #Click on the city
        el6 = driver.find_element(by=AppiumBy.ID, value="com.graph.weather.forecast.channel:id/tv_info_location_search")
        el6.click()
        time.sleep(3)
        el7 = driver.find_element(by=AppiumBy.ID, value="com.graph.weather.forecast.channel:id/tvInfoLocation")
        el7.click()
        time.sleep(3)

        el16 = driver.find_element(by=AppiumBy.ID, value="com.graph.weather.forecast.channel:id/tvTitle")

        if el16.get_attribute("text") == f"{nom_ville}, France":
            print("Test OK")

    except :
        print("Test KO")

    driver.quit()

print("Résultat de test de recherche d'une ville existante :")
cherche_ville_existe("Dunkerque")
