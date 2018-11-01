# import socket
import sys
from selenium import webdriver
import time

from Socket_tester import sock
from Connect_SSID import connect


class Voucher:
    
    def __init__(self, vnumber, time=90, ssid='__keep_out__'):
        self.vnumber = vnumber
        self.time = time*60+30
        self.ssid = ssid
    
    def test(self):
        try:

            print("The test has began with voucher number:", self.vnumber, "time:", self.time, "ssid:", self.ssid)
            result = connect(self.ssid, ip_address='192.168.7.61/24', ip_gw='192.168.7.1', dns_address='8.8.8.8', wireless_int='wlp2s0').run()
            if result:
                print("in test, result is:", result)
                options = webdriver.ChromeOptions()
                options.add_argument('--no-sandbox')
                browser = webdriver.Chrome('/home/lu050023/ChromeDriver/chromedriver', chrome_options=options)
                browser.set_page_load_timeout(45)
                browser.get('http://www.ufsc.br')
                browser.find_element_by_id("voucher").send_keys(self.vnumber)
                browser.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[2]/button").click()
                try:
                    urlAlert = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[@class=\'alert alert-danger\']")
                    print("Atingiu o tempo limite")
                    return 0

                except:
                    print("exception urlAlert")



                try:
                    urlSucc = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[@class=\'alert alert-success\']")
                    print("check in success")
                    browser.close()
                    result = sock('8.8.8.8', self.time).run()
                    if result:
                        print('slef.time=',self.time)
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
                print("in Voucher, was not able to connect on SSID: ", self.ssid["ssid"], result)
                return 0

        except:
            print("Something went wrong on Voucher module with:", sys.exc_info()[0], sys.exc_info()[1])

