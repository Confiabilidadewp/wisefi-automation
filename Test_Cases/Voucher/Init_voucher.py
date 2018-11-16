
from Test_Cases.Voucher import Test_Voucher
import time
import Login
import Shell_interact as shell
from Test_Cases.Voucher import Configure_SSID_CP_Voucher as SSID
from Test_Cases.Voucher import API_voucher as get_voucher
from Global_variables import Global_variables

class begin:

    def __init__(self, parameters="none"):
        self.parameters = parameters

    def now(self):
        Global = Global_variables
        ####Disconnecting and removing configurations#####

        shell.shell('ifconfig ' + Global('WirelessInt').get() + ' 0.0.0.0 && iw dev ' + Global(
            'WirelessInt').get() + ' disconnect').run()
        shell.shell('route del default ').run()
        shell.shell('echo "" > /etc/resolv.conf').run()

        ####Starting Test####

        login = Login.Login(Global('WisefiAddress').get(), Global('WisefiUser').get(), Global('WisefiPass').get()).run()
        ssid = SSID.SSID_CP(login, ".AUTOMATION_WISEFI_VOUCHER.").configure_ssid_cp_voucher()
        voucher = get_voucher.API_Voucher('http://192.168.7.59:8000/cp/api/vouchers/', 'admin', '12121212').create_voucher()
        time.sleep(90)
        Test = Test_Voucher.Voucher(voucher, 1, ssid).test()

        ####Adding internet again, to be able to send report file####

        shell.shell('ifconfig ' + Global('WirelessInt').get() + ' 0.0.0.0 && iw dev ' + Global(
            'WirelessInt').get() + ' disconnect').run()
        shell.shell('route add default gw ' + Global('WirelessGw').get()).run()
        shell.shell('echo "nameserver '+ Global('Dns').get() +'" > /etc/resolv.conf').run()
        print(Test)

        return Test



