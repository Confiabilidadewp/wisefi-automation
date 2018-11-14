import time
import Login
import Shell_interact as shell
from Test_Cases.Simple_password import Configure_SSID_CP_Simple_Password as SSID
from Test_Cases.Simple_password import Configure_simple_password as config_cp
from Test_Cases.Simple_password import Test_Simple_password
import random_number as number

class begin:

    def __init__(self, parameters="none"):
        self.parameters = parameters

    def now(self):
        ####Disconnecting and removing configurations#####

        shell.shell('ifconfig wlp2s0 0.0.0.0 && iw dev wlp2s0 disconnect').run()
        shell.shell('route del default ').run()
        shell.shell('echo "" > /etc/resolv.conf').run()

        ####Starting Test CP Simple Password####

        login = Login.Login('http://192.168.7.59:8000', 'admin', '12121212').run()
        ssid = SSID.SSID_CP(login, ".AUTOMATION_WISEFI_S_PASS.").configure_ssid_cp_simple_password()
        NPassword = number.create(152000, 985250).run()
        config_cp.SSID_CP(login, NPassword).configure_simple_password()
        time.sleep(90)
        Test = Test_Simple_password.Simple_Password(NPassword, 1, ssid).test()

        ####Adding internet again, to be able to send report file####

        shell.shell('ifconfig wlp2s0 0.0.0.0 && iw dev wlp2s0 disconnect').run()
        shell.shell('route add default gw 192.168.7.1').run()
        shell.shell('echo "nameserver 8.8.8.8" > /etc/resolv.conf').run()
        print(Test)

        return Test



