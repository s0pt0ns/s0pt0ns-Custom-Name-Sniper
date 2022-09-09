import requests
import string
import ctypes
import threading
import datetime
import os
import colorama
from colorama import Fore, Back, Style

colorama.init()
os.system('cls')

colors = ['BLUE', 'GREEN', 'MAGENTA', 'RED', 'YELLOW']

valid = 0
invalid = 0
controller = 0
printed = 0

nerdstats = open('Settings/NerdStatsToggle.txt', 'r')
colortoggle = open('Settings/ColorToggle.txt', 'r')
nerdstats = nerdstats.read()
colortoggle = colortoggle.read()
nerdstats = nerdstats.lower()
colortoggle = colortoggle.lower()
if colortoggle == 'yes':
    colortoggle = True
else:
    colortoggle = False
if nerdstats == 'yes':
    nerdstats = True
else:
    nerdstats = False

ctypes.windll.kernel32.SetConsoleTitleW(f'Custom Name Checker | Valid: {valid} | Invalid: {invalid}')

def filecheck():

    global controller
    global valid
    global invalid
    global colortoggle

    file = open('names.txt', 'r')
    file = file.read()
    file = file.split('\n')

    if colortoggle == True:
        print(f"[Join the discord]: {Fore.YELLOW}discord.gg/{Fore.GREEN}termed{Style.RESET_ALL}")
    else:
        print(f"[Join the discord]: discord.gg/termed{Style.RESET_ALL}")

    print(f"Unfortunately some people cannot use computers so, Please put the usernames into 'names.txt'\n{Fore.YELLOW}IF YOU HAVE ALREADY DONE THIS YOU ARE WELCOME TO CONTINUE{Style.RESET_ALL}")
    input("Press enter to continue ...")

    
    
    def do():

        global valid
        global invalid
        global controller
        global colors
        global printed
        global colortoggle
        global nerdstats
        
        os.system('cls')

        for TFile in file:
            
            threading.Lock()
            TFile = TFile.strip(string.punctuation)
            if len(TFile) > 2:
                controller += 1
                if len(TFile) > 20:
                    controller += 1
                else:
                    url = f'https://auth.roblox.com/v1/usernames/validate?request.username={TFile}&request.birthday=1977-03-04&request.context=Signup'
                    r = requests.get(url)
                    r = r.json()
                    r = r['code']

                    statisticview = requests.get(url)
                    statisticview = statisticview.json()

                    if r == 0:
                        valid +=1
                        if colortoggle == True:
                            print(f'[{datetime.datetime.now()}]: [{Back.LIGHTGREEN_EX}{Fore.BLACK}1{Style.RESET_ALL}]: [{Fore.GREEN}Valid{Style.RESET_ALL}]: ' + TFile)
                        else:
                            print(f'[{datetime.datetime.now()}]: [1]: [Valid{Style.RESET_ALL}]: ' + TFile)
                        valids = open('validnames.md', 'a')
                        valids.write(f'\n{TFile}')
                        valids.close()
                        ctypes.windll.kernel32.SetConsoleTitleW(f'Custom Name Checker | Valid: {valid} | Invalid: {invalid}')
                        printed += 1
                    else:
                        invalid += 1
                        if colortoggle == True:
                            if nerdstats == True:
                                print(f"[{datetime.datetime.now()}]: [{Back.RED}{Fore.WHITE}0]{Style.RESET_ALL}: [{Fore.YELLOW}Checking{Style.RESET_ALL}]:  {Fore.RED}{TFile}{Style.RESET_ALL}...")
                                print(f"{Fore.YELLOW}{statisticview}\n{Fore.WHITE}Response Code: {requests.get(url).status_code}{Style.RESET_ALL}")
                            else:
                                print(f"[{datetime.datetime.now()}]: [{Back.RED}{Fore.WHITE}0{Style.RESET_ALL}]: [{Fore.YELLOW}Checking{Style.RESET_ALL}]:  {Fore.RED}{TFile}{Style.RESET_ALL}...")
                        else:
                            if nerdstats == True:
                                print(f"[{datetime.datetime.now()}]: [0]: [Checking]:  {TFile}{Style.RESET_ALL}...")
                                print(f"{statisticview}\n{requests.get(url).status_code}")
                            else:
                                print(f"[{datetime.datetime.now()}]: [0]: [Checking]:  {TFile}{Style.RESET_ALL}...")

                        ctypes.windll.kernel32.SetConsoleTitleW(f'Custom Name Checker | Valid: {valid} | Invalid: {invalid}')
                        printed += 1
            if printed > 30:
                os.system('cls')
                printed = 0 
                print(f"[Join the discord]: {Fore.YELLOW}discord.gg/{Fore.GREEN}termed{Style.RESET_ALL}")
                print(f"[Support discord server]: {Fore.YELLOW}discord.gg/{Fore.GREEN}ygd68PveqX{Style.RESET_ALL}")
                print(f"[Credits]: {Fore.YELLOW}ALL CREDITS GO TO pr0t0ns{Style.RESET_ALL}")

    do()
filecheck()