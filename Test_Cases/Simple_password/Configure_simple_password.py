from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class SSID_CP:

    def __init__(self, driver, senha):
        self.driver = driver
        self.senha = senha


    def configure_simple_password(self):
        try:

            self.driver.set_page_load_timeout(45)
            time.sleep(0.5)
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "button_cp"))).click()
            time.sleep(0.5)
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "cp_simple_password"))).click()
            time.sleep(0.5)
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password1"))).clear()
            self.driver.find_element_by_id("password1").send_keys(self.senha)
            self.driver.find_element_by_id("password2").clear()
            self.driver.find_element_by_id("password2").send_keys(self.senha)
            select_temp = Select(self.driver.find_element_by_id("id_time"))
            select_temp.select_by_value("other")
            self.driver.find_element_by_id("valueTime").clear()
            self.driver.find_element_by_id("valueTime").send_keys("1")
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "save")))
            element.click()
            print("Password configured")
            self.driver.quit()
        except Exception as e:
            print("ERROR:", e)
        # return self.ssid
