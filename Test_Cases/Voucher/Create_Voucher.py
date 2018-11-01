from selenium.webdriver.support.select import Select
from selenium import webdriver
import Login



class Voucher:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def generate_voucher(self):
        print("antes login")
        driver = Login.Login(self.url, self.username, self.password).run()
        print("depois login")
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        #driver = webdriver.Chrome('/home/lu050023/ChromeDriver/chromedriver', chrome_options=options)
        #driver.set_page_load_timeout(45)
        driver.find_element_by_id("button_cp").click()
        driver.find_element_by_id("qtd").send_keys("1")
        driver.find_element_by_id("numDevices").send_keys("1")
        select_temp = Select(driver.find_element_by_id("id_time"))
        select_temp.select_by_value("other")
        driver.find_element_by_id("valueTime").clear()
        driver.find_element_by_id("valueTime").send_keys("1")
        driver.find_element_by_id("generate").click()
        #voucher = driver.find_element_by_id("4_cod").get_attribute
        voucher = 713705
        #print("Voucher gerado", voucher)
        #result = Socket_client_voucher.Socket("WiseFiTest", voucher, "1", 1).S
        driver.close()
        return voucher