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
                  'WisefiAddress': '192.168.7.59:8000',
                  'WisefiUser': 'admin',
                  'WisefiPass': '12121212'}
        return result[self.info]




