from selenium.webdriver.support.select import Select

class SSID_CP:

    def __init__(self, driver, ssid):
        self.driver = driver
        self.ssid = ssid


    def configure_ssid_cp_voucher(self):

        #driver = Login.Login(self.url, self.username, self.password).run()
        self.driver.set_page_load_timeout(45)
        self.driver.find_element_by_id("button_network").click()
        self.driver.find_element_by_id("button_wlan").click()
        self.driver.find_element_by_id("1_edit").click()
        self.driver.find_element_by_id("ssid1").clear()
        self.driver.find_element_by_id("ssid1").send_keys(self.ssid)
        select_temp = Select(self.driver.find_element_by_id("id_ssid1Security"))
        select_temp.select_by_value("5")
        select_temp = Select(self.driver.find_element_by_id("id_ssid1CaptivePortal"))
        select_temp.select_by_value("2")
        self.driver.find_element_by_id("save").click()
        print("SSID ALTERADO PARA CP VOUCHER")
        self.driver.quit()
        return self.ssid

