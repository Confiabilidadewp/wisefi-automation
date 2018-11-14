
from Test_Cases.Voucher import Test_Voucher
import time
import Login
import Shell_interact as shell
from Test_Cases.Voucher import Configure_SSID_CP_Voucher as SSID
from Test_Cases.Voucher import API_voucher as get_voucher

class begin:

    def __init__(self, parameters="none"):
        self.parameters = parameters

    def now(self):
        ####Disconnecting and removing configurations#####

        shell.shell('ifconfig wlp2s0 0.0.0.0 && iw dev wlp2s0 disconnect').run()
        shell.shell('route del default ').run()
        shell.shell('echo "" > /etc/resolv.conf').run()

        ####Starting Test####

        login = Login.Login('http://192.168.7.59:8000', 'admin', '12121212').run()
        ssid = SSID.SSID_CP(login, ".AUTOMATION_WISEFI_VOUCHER.").configure_ssid_cp_voucher()
        voucher = get_voucher.API_Voucher('http://192.168.7.59:8000/cp/api/vouchers/', 'admin', '12121212').create_voucher()
        time.sleep(90)
        Test = Test_Voucher.Voucher(voucher, 1, ssid).test()

        ####Adding internet again, to be able to send report file####

        shell.shell('ifconfig wlp2s0 0.0.0.0 && iw dev wlp2s0 disconnect').run()
        shell.shell('route add default gw 192.168.7.1').run()
        shell.shell('echo "nameserver 8.8.8.8" > /etc/resolv.conf').run()
        print(Test)

        return Test



