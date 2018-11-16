# import socket
import sys
from selenium import webdriver
import time

from Socket_tester import sock
from Connect_SSID import connect
import Global_variables



class Simple_Password:

    def __init__(self, password, time=90, ssid='__keep_out__'):
        self.password = password
        self.time = time * 60 + 30
        self.ssid = ssid

    def test(self):

        try:

            print("The test has began with password:", self.password, "time:", self.time, "ssid:", self.ssid)
            result = connect(self.ssid, ip_address='192.168.7.61/24', ip_gw='192.168.7.1', dns_address='8.8.8.8',
                             wireless_int='wlp2s0').run()
            if result:

                print("in test, result is:", result)
                options = webdriver.ChromeOptions()
                options.add_argument('--no-sandbox')
                result = Global_variables.Global_variables
                driver = webdriver.Chrome(result('directory').get(), chrome_options=options)
                driver.set_page_load_timeout(45)
                driver.get('http://www.ufsc.br')
                driver.find_element_by_id("password").send_keys(self.password)
                driver.find_element_by_id("btSend").click()

                try:
                    urlAlert = driver.find_element_by_xpath(
                        "/html/body/div/div/div/div[2]/form/div[@class=\'alert alert-danger\']")
                    print("Atingiu o tempo limite")
                    return 0
                except:
                    print("exception urlAlert")

                '''
                try:
                    urlAlert = driver.find_element_by_class_name("alert alert-danger")
                    print("Senha incorreta")
                    return 0
                except:
                    print("exception urlAlert")
                '''

                try:
                    urlSucc = driver.find_element_by_xpath(
                        "/html/body/div/div/div/div[2]/form/div[@class=\'alert alert-success\']")
                    print("check in success")
                    driver.close()
                    result = sock('8.8.8.8', self.time).run()
                    if result:
                        print('sleep.time=', self.time)
                        time.sleep(self.time)
                        result = sock('8.8.8.8', self.time).run()
                        if result:
                            print("Was with access yet")
                            return 0
                        else:
                            print("has blocked the access, success!!")
                            return 1
                    else:
                        print("Not yet connected")
                        return 0

                except:
                    print("exception urlSucc")
                    return 0

            else:
                print("in Password, was not able to connect on SSID: ", self.ssid["ssid"], result)
                return 0

        except:
            print("Something went wrong on Password module with:", sys.exc_info()[0], sys.exc_info()[1])