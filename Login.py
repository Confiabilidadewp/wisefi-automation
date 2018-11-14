from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import Global_variables

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
result = Global_variables.Global_variables
driver = webdriver.Chrome(str(result('directory').get()), chrome_options=options)
driver.set_page_load_timeout(45)


class Login:

    def __init__(self, url, username, password):

        self.url = url
        self.username = username
        self.password = password

    def run(self):
        print("LOGIN")


        driver.set_page_load_timeout(45)
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element_by_id("username").send_keys(self.username)
        driver.find_element_by_name("password").send_keys(self.password)
        driver.find_element_by_tag_name("button").click()
        title = driver.title


        print(title)
        if driver.find_element_by_id("button_home"):
            botao = driver.find_element_by_id("button_home").get_attribute("id")
            print(botao)
            print("Success Login")
        else:
            print("Login Fail")
        return driver

