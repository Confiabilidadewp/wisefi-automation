# import socket
# import sys
from Test_Cases import Cad_ind, Simp_pass, CPF
from Test_Cases.Voucher import Init_voucher
import Report_plotly as report
Tests = []
Results = []
class Controller:

    def __init__(self, Case=None):
        self.Case = int(Case)

    def check(self):
        try:
            print(type(self.Case))

            if self.Case == 1:
                print("Voucher", self.Case)
                # result = Voucher.Voucher(self.Case["voucher"], self.Case["time"], self.Case["ssid"]).test()
                result = Init_voucher.begin().now()
                Results.append(result)
                Tests.append("Voucher")
                report.info(Tests, Results).run()
                print("Final Result",result)
                return result

            elif self.Case == 2:
                print("CPF", self.Case)
                result = CPF.CPF(self.Case["cpf"], self.Case["time"], self.Case["ssid"]).test()
                return result

            elif self.Case == 3:
                print("Cadastro Individual", self.Case)
                result = Cad_ind.Cad_ind(self.Case["cpf"], self.Case["time"], self.Case["ssid"], self.Case["telefone"], self.Case["email"], self.Case["nome"]).test()
                return result

            elif self.Case == 4:
                print("Senha Simples", self.Case)
                result = Simp_pass.Simp_pass(self.Case["password"], self.Case["time"], self.Case["ssid"]).test()
                return result

            else:
               print("Não foi", self.Case)

        except:
            print("erro occurred in:", BaseException.args())