# https://letcode.in/test
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
actions = ActionChains(driver)

# # Hover
driver.get("https://the-internet.herokuapp.com/hovers")
print(driver.page_source)
# driver.maximize_window()
# FirstAVT = driver.find_element(By.XPATH, "//img[@src='/img/avatar-blank.jpg']")
# actions.move_to_element(FirstAVT).perform()
# try: 
#     NameAvt= driver.find_element(By.XPATH, "//div[@class='figcaption']/h5[text()='name: user1']")
#     print(f"Tên avatar đầu tiên: {NameAvt.text}")
# except:
#     print(f"Không tìm thấy avt")

# # # # Right Click
# driver.get("https://the-internet.herokuapp.com/context_menu")
# driver.maximize_window()
# Box = driver.find_element(By.XPATH, "//div[@id='hot-spot']")
# actions.context_click(Box).perform()
# alert = driver.switch_to.alert
# print(f"Tên box: {alert.text}")
# try: 
#     alert = driver.switch_to.alert
#     print(f"Tên box: {alert.text}")
# except:
#     print(f"không thấy box nào")


# # # # Double Click
# driver.get("https://demo.guru99.com/test/simple_context_menu.html")
# driver.maximize_window()
# Button = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")
# actions.double_click(Button).perform()
# try: 
#     alert = driver.switch_to.alert
#     print(f"Tên box: {alert.text}")
# except:
#     print(f"không thấy box nào")

# # # Click & Hold
# driver.get("https://letcode.in/button")
# driver.maximize_window()
# NeededBtn = driver.find_elements(By.XPATH, "//button[@id='isDisabled']")
# print(F"SL: {len(NeededBtn)}")
# driver.execute_script("arguments[0].scrollIntoView(true);", NeededBtn[1])
# time.sleep(1)
# actions.click_and_hold(NeededBtn[1]).pause(3).release().perform()
# time.sleep(2)
# print(f"Tên btn: {NeededBtn[1].text}")


# # # # Gõ phím
# driver.get("https://letcode.in/edit")
# driver.maximize_window()
# Textbox = driver.find_element(By.XPATH, "//input[@id='fullName']")
# Textbox.send_keys("Hello")
# time.sleep(2)
# actions.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
# time.sleep(2)
# Textbox.send_keys("Updated name")
# time.sleep(2)
