# https://letcode.in/test
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
actions = ActionChains(driver)

# # Hover
# driver.get("https://the-internet.herokuapp.com/hovers")
# print(driver.page_source)
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

# #EDIT FIELDS

# driver.get("https://letcode.in/edit")
# driver.maximize_window()
# Textbox1 = driver.find_element(By.XPATH, "//input[@id='fullName']")
# Textbox1.send_keys("YenTTK")
# time.sleep(2)

# Textbox2 = driver.find_element(By.XPATH, "//input[@id='join']")
# Textbox2.send_keys("Append text")
# time.sleep(2)
# actions.key_down(Keys.TAB).perform()
# time.sleep(2)

# Textbox3 = driver.find_element(By.XPATH, "//input[@id='getMe']")
# value = Textbox3.get_attribute("value")
# print(f"Text có trong textbox03: {value}")

# Textbox4 = driver.find_element(By.XPATH, "//input[@id='clearMe']")
# actions.move_to_element(Textbox4).key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
# Textbox4.clear()
# time.sleep(2)

# Textbox5 = driver.find_element(By.XPATH, "//input[@id='noEdit']")
# if not Textbox5.is_enabled():
#     print(" The input field is disabled.")
# else:
#     print("The input field is NOT disabled.")

# Textbox6 = driver.find_element(By.XPATH, "//input[@id='dontwrite']")
# if Textbox6.get_attribute("readonly") is not None:
#      print("The input field is readonly.")
# else:
#     print("The input field is NOT readonly.")

# #BUTTON

# driver.get("https://letcode.in/button")
# driver.maximize_window()
# Btn01 = driver.find_element(By.XPATH, "//button[@id='home']")
# Btn01.click()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# print("Đã quay lại trang buttons thành công")

# Btn02 = driver.find_element(By.XPATH, "//button[@id='position']")
# x = Btn02.location['x']
# y = Btn02.location['y']
# print(f"Toạ độ button là: X = {x}, Y = {y}")

# Btn03 = driver.find_element(By.XPATH, "//button[@id='color']")
# BtnColor = Btn03.value_of_css_property("background-color")
# print(f"Background color: {BtnColor}")

# Btn04 = driver.find_element(By.XPATH, "//button[@id='property']")
# size = Btn04.size
# width = size['width']
# height = size['height']
# print(f"Width: {width}px")
# print(f"Height: {height}px")

# BtnCommon = driver.find_elements(By.XPATH, "//button[@id='isDisabled']")
# print(F"SL: {len(BtnCommon)}")
# Btn05 = BtnCommon[0]
# if not Btn05.is_enabled():
#     print("Button is disabled.")
# else:
#     print("is NOT disabled.")

# Btn06 = BtnCommon[1]
# actions.click_and_hold(Btn06).pause(2).release().perform()
# time.sleep(2)
# print(f"Tên btn: {Btn06.text}")


# WAIT

driver.get("https://letcode.in/waits")
driver.maximize_window()
Btn = driver.find_element(By.XPATH, "//button[@id='accept']")
Btn.click()
time.sleep(10)
alert = driver.switch_to.alert
print(f"✅ Alert message: {alert.text}") 
