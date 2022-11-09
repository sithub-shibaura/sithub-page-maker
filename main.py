#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import time
import datetime
from time import ctime
import sys
import os


# you have to run this: pip install 
import ntplib

class TerminalColor:
    BLACK     = '\033[30m'
    RED       = '\033[31m'
    GREEN     = '\033[32m'
    YELLOW    = '\033[33m'
    BLUE      = '\033[34m'
    PURPLE    = '\033[35m'
    CYAN      = '\033[36m'
    WHITE     = '\033[37m'
    END       = '\033[0m'
    BOLD      = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE   = '\033[07m'

class MyNTPClient(object):
    def __init__(self, ntp_server_host):
        self.ntp_client = ntplib.NTPClient()
        self.ntp_server_host = ntp_server_host

    def get_nowtime(self, timeformat = '%Y/%m/%d %H:%M:%S'):
        try:
            res = self.ntp_client.request(self.ntp_server_host)
            nowtime = datetime.datetime.strptime(ctime(res.tx_time), "%a %b %d %H:%M:%S %Y")
            return nowtime.strftime(timeformat)
        except Exception as e:
            print("An error occured")
            print("The information of error is as following")
            print(type(e))
            print(e.args)
            print(e)
            # sys.exit(1)

def main():
    ntp_client = MyNTPClient('ntp.nict.jp')
    print_time = 0
    while True:
        if ntp_client.get_nowtime() != print_time:
            print_time = ntp_client.get_nowtime()
            os.system('cls')
            print(TerminalColor.RED + print_time + TerminalColor.END)
            print(TerminalColor.GREEN + print_time + TerminalColor.END)
            print(TerminalColor.YELLOW + print_time + TerminalColor.END)
            print(TerminalColor.BLUE + print_time + TerminalColor.END)
            print(TerminalColor.PURPLE + print_time + TerminalColor.END)
            print(TerminalColor.CYAN + print_time + TerminalColor.END)
            print(TerminalColor.WHITE + print_time + TerminalColor.END)
            print(TerminalColor.REVERCE + print_time + TerminalColor.END)


if __name__ == "__main__":
    main()