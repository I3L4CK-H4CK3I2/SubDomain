#!/usr/bin/python
'coded by l314ck_h4ck3l2 '

import os
import sys
import time
import requests


blue = '\033[34m'
green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
error = '\033[91m'
cyan = '\033[36m'
bold    = "\033[;1m"
reset = "\033[0;0m"


path = 'subdomain_list.txt'
subdomains = open(path , 'r').read().splitlines()

def banner():
    print(f"""{blue}

  _______  __   __  _______  ______   _______  __   __  _______  ___   __    _ 
 |       ||  | |  ||  _    ||      | |       ||  |_|  ||   _   ||   | |  |  | |
 |  _____||  | |  || |_|   ||  _    ||   _   ||       ||  |_|  ||   | |   |_| |
 | |_____ |  |_|  ||       || | |   ||  | |  ||       ||       ||   | |       |
 |_____  ||       ||  _   | | |_|   ||  |_|  ||       ||       ||   | |  _    |
  _____| ||       || |_|   ||       ||       || ||_|| ||   _   ||   | | | |   |
 |_______||_______||_______||______| |_______||_|   |_||__| |__||___| |_|  |__|


 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{cyan}
 ~                           Author : l314ck_h4ck3l2                          ~
 ~                 github : https://github.com/l314ck-h4ck3l2                 ~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{reset}""")

def discover_subdomain(site , domain):
    try:
        req = requests.get(site)
    except requests.ConnectionError:
        print(f'{red} [!] Host is Not True !{reset}')
        sys.exit()
    if req.status_code == 200:
        for subdomain in subdomains:
            url = 'http://' + subdomain + '.' + domain or 'https://' + subdomain + '.' + domain
            try:
                res = requests.get(url)
                print(f'{green} [+] {url}{reset}')
                time.sleep(0.5)
            except requests.ConnectionError:
                print(f'{red} [-] {url}{reset}')
                time.sleep(0.5)

def usage():
    print(f'{error} Usage   : python SubDomain.py [url]{reset}')
    print(f'{error} Example : python SubDomain.py instagram.com{reset}')
    print(f'{error} Example : python SubDomain.py https://www.instagram.com{reset}')
    sys.exit()

def main():
    os.system('cls' or 'clear')
    banner()
    if len(sys.argv) == 2:
        if sys.argv[1].startswith('http://www.'):
            domain = sys.argv[1][11:]
            site = sys.argv[1]
        elif sys.argv[1].startswith('https://www.'):
            domain = sys.argv[1][12:]
            site = sys.argv[1]
        else:
            domain = sys.argv[1]
            site = 'http://www.' + domain or 'https://www.' + domain
        print(f'{yellow} domian : {domain}{reset}')
        print(f'{yellow} site : {site}{reset}')
        print()
        discover_subdomain(site , domain)
    else:
        usage()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f'{red} [-] ^C received . shutting down server !{reset}')
        sys.exit()
