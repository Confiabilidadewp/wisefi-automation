import plotly
import plotly.plotly as py
import plotly.graph_objs as go

class info:

    def __init__(self, tests="nok", results="nok"):
        self.tests = tests
        self.results = results

    def run(self):
        try:
            plotly.tools.set_credentials_file(username='cardosoluke', api_key='8flan6vkd9EXqxqHH5tb')
            labels = self.tests
            values = self.results

            trace = go.Pie(labels=labels, values=values)

            py.iplot([trace], filename='WiseFi_Automation')


        except Exception as e:
            print(e)
# try:
#     labels = ['login','cpf','voucher', 'password','wpa2','wpa','without password']
#     values = ['ok','nok','nok','ok','ok','ok','nok']
#
#     trace = go.Pie(labels=labels, values=values)
#
#     py.iplot([trace], filename='Tests_Cases')
# except:
#     print ('end 1')