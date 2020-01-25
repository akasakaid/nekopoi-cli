import sys,os,time
try:
	from requests import *
	from bs4 import BeautifulSoup
	from colorama import Fore,Style, init as jancok
	jancok(autoreset=True)
	merah = Fore.RED+Style.BRIGHT
	kuning = Fore.YELLOW+Style.BRIGHT
	hijau = Fore.GREEN+Style.BRIGHT
	biru = Fore.BLUE+Style.BRIGHT
	magenta = Fore.MAGENTA+Style.BRIGHT
	reset = Fore.RESET
except:
	print('Please install requirements.txt')
	sys.exit()
os.system('cls' if os.name == 'nt' else 'clear')
def menu():
	print(f"""{hijau}
  _   _      _         _____      _ {magenta}   _____ _      _____ {hijau}
 | \ | |    | |       |  __ \    (_){magenta}  / ____| |    |_   _|{hijau}
 |  \| | ___| | _____ | |__) |__  _ {magenta} | |    | |      | |  {hijau}
 | . ` |/ _ \ |/ / _ \|  ___/ _ \| |{magenta} | |    | |      | |  {hijau}
 | |\  |  __/   < (_) | |  | (_) | |{magenta} | |____| |____ _| |_ {hijau}
 |_| \_|\___|_|\_\___/|_|   \___/|_|{magenta}  \_____|______|_____|{hijau}
 {reset}[+] CODED : AkasakaID 

{merah}[{reset}1{merah}]{reset} HOME [UPDATE]
{merah}[{reset}2{merah}]{reset} GRAB HENTAI 
{merah}[{reset}3{merah}]{reset} GRAB JAV 
""")
menu()
try:
	ch = int(input(f"[{hijau}>{reset}] Masukkan Pilihanmu: "))
	if ch == 1:
		import src.home
	elif ch == 2:
		print(f'{merah}[{reset}!{merah}]{reset} COOMING SOON')
	elif ch == 3:
		print(f'{merah}[{reset}!{merah}]{reset} COOMING SOON')
	else:
		print(f'{merah}[!] {reset}Liat List Dong Pantek\n{merah}[!]{reset} Jalanin ulang programnya!')
except KeyboardInterrupt:
	print(f'{merah}\n[!] Keluar..!!')
