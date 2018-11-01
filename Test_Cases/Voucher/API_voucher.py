import requests

import random_number as number
class API_Voucher:

    def __init__(self, url, username, password):
        self.username = username
        self.password = password
        self.url = url

    def create_voucher(self):
        #r = requests.get('http://localhost:8000/cp/api/vouchers/', auth=(self.username, self.password))
        #print(r.json())
        Nvoucher = number.create(1000,4000).run()
        voucher = requests.post(self.url, auth=(self.username, self.password), data={'cod': str(Nvoucher), 'id': 2, 'period': 'minute', 'status': 0, 'numDevices': 10, 'time': 1})
        print(voucher.status_code)
        return Nvoucher
