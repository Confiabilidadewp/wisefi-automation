import urllib3
import sys
import argparse


from Controller import Controller


urllib3.disable_warnings()

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Basic Functions')
    parser.add_argument('-c', '--case',
                        help='Test Case',
                        required='True',
                        default='cpf')
    results = parser.parse_args(args)
    return (results.case)


def main():
    c = check_arg(sys.argv[1:])
    #print('mode:', m, 'ip:', ip, 'port:', p, 'username:', user, 'password:', pas, 'channel:', ch, ver, int, soc, db, Hid, Iid)

    Controller(c).check()

main()