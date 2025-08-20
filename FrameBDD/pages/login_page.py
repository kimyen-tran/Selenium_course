from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://dev.sp.leadplus.net/login"
    # driver = webdriver.Chrome()
    # wait = WebDriverWait(driver, 30)

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        # self.driver.wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
        # self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(username)
        EmailTextbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
        EmailTextbox.send_keys(username)
    def enter_password(self, password):
        # self.driver.find_element(By.XPATH,"//input[@name='password']").clear()
        # self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)
        PassWordTextbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
        PassWordTextbox.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,"//button[@data-at_id='btn__login']").click()

    def get_current_url(self):
        return self.driver.current_url

    # def get_flash_message(self):
    #     return self.driver.find_element(By.ID, "flash").text