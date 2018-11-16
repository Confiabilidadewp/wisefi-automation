from sys import platform

class Global_variables:

    def __init__(self, info=""):
        self.info = info


    def platform_directory(self):


        if platform == "linux" or platform == "linux2":
            return '/root/PycharmProjects/wisefi-automation/chromedriver'

        elif platform == "win32":
            return 'chromedriver'

    def get(self):
        consult = Global_variables
        result = {'directory': consult.platform_directory(self),
                  'WisefiAddress': 'http://192.168.7.59:8000',
                  'WisefiUser': 'admin',
                  'WisefiPass': '12121212',
                  'WirelessInt': 'wlp2s0',
                  'WirelessIp': '192.168.7.61/24',
                  'WirelessGw': '192.168.7.1',
                  'Dns': '8.8.8.8'
                  }


        return result[self.info]




