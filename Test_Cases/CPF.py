import sys
from selenium import webdriver
import time

from Socket_tester import sock
from Connect_SSID import connect


class CPF:

    def __init__(self, cpf='000.000.000-00', time=90, ssid='__keep_out__'):
        self.cpf = cpf
        self.time = time*60+30
        self.ssid = ssid

    def test(self):
        try:

            print("The test has began with CPF number:", self.cpf, "time:", self.time, "ssid:", self.ssid)
            result = connect(self.ssid, ip_address='192.168.4.61/24', ip_gw='192.168.4.1', dns_address='8.8.8.8', wireless_int='wlp2s0').run()
            if result:
                print("in test, result is:", result)
                options = webdriver.ChromeOptions()
                options.add_argument('--no-sandbox')
                browser = webdriver.Chrome('/home/lu050023/ChromeDriver/chromedriver', chrome_options=options)
                browser.set_page_load_timeout(15)
                browser.get("http://www.ufsc.br")
                browser.find_element_by_id("cpf").send_keys(self.cpf)
                browser.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[2]/button").click()

                try:
                    urlAlert = browser.find_element_by_xpath(
                        "/html/body/div/div/div/div[2]/form/div[@class=\'alert alert-danger\']")
                    print("Atingiu o tempo limite")
                    return False

                except:
                    print("exception urlAlert")

                try:
                    urlSucc = browser.find_element_by_xpath(
                        "/html/body/div/div/div/div[2]/form/div[@class=\'alert alert-success\']")
                    print("check in success")
                    result = sock('8.8.8.8', self.time).run()
                    if result:
                        print('slef.time=', self.time)
                        time.sleep(self.time)
                        result = sock('8.8.8.8', self.time).run()
                        if result:
                            print("Was with access yet")
                            return False
                        else:
                            print("has blocked the access, success!!")
                            return True
                    else:
                        print("Not yet connected")
                        return False


                except:
                    print("exception urlSucc")
                    return False

            else:
                print("in Voucher, was not able to connect on SSID: ", self.ssid["ssid"], result)
                return False

        except:
            print("Something went wrong on CPF module with:", sys.exc_info()[0], sys.exc_info()[1])


