from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Android Emulator"
options.app_package = "com.android.calculator2"
options.app_activity = "com.android.calculator2.Calculator"
options.automation_name = "UiAutomator2"
options.set_capability("noReset", True)

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(1)

driver.find_element("id", "com.android.calculator2:id/digit_2").click()
driver.find_element("id", "com.android.calculator2:id/op_add").click()
driver.find_element("id", "com.android.calculator2:id/digit_3").click()
driver.find_element("id", "com.android.calculator2:id/eq").click()

result = driver.find_element("id", "com.android.calculator2:id/result").text
print("Result is:", result)

driver.quit()
