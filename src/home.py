try:
	import os
	from requests import *
	from bs4 import BeautifulSoup as bs
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


url = 'http://nekopoi.care'
ua = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

def link():
	ab = get('http://nekopoi.care'+dd["href"],headers=ua).text
	ac = bs(ab,'html.parser')
	ad = ac.find('div',attrs={'class':'arealinker'})
	ae = ad.findAll('div',attrs={'class':'liner'})
	nol = 0
	for link in range(0,len(ae)):
		af = ae[nol].find('div',attrs={'class':'name'})
		print(f'[+] '+af.text)
		ag = ae[nol].find('div',attrs={'class':'listlink'})
		ah = ag.findAll('a')
		aw = 0
		for linkpoi in range(0,len(ah)):
			print(f'{reset}[+] {biru}Server:{hijau}',ah[aw].text,f'{magenta}Link =>{hijau}',ah[aw]["href"])
			aw += 1
		print(f'{reset}[!]{hijau} Silahkan Copy linknya dan pastekan di browser anda!\n')
		nol += 1
##################################################
try:
	a = get(url,headers=ua).text
	b = bs(a,'html.parser')
	c = b.findAll('div',attrs={'class':'eropost'})
	co = 0
	for x in range(0,len(c)):
		d = c[co].find('a')
		print(f"{hijau}[{co}{reset}]"+d.text)
		co += 1
###################################################
	aa = get(url,headers=ua).text
	bb = bs(aa,'html.parser')
	cc = bb.findAll('div',attrs={'class':'eropost'})

	an = input(f'[{hijau}>{reset}] Masukkan Pilihan: ')
	if an == '0':
		dd = cc[0].find('a')
		link()
	elif an == '1':
		dd = cc[1].find('a')
		link()
	elif an == '2':
		dd = cc[2].find('a')
		link()
	elif an == '3':
		dd = cc[3].find('a')
		link()
	elif an == '4':
		dd = cc[4].find('a')
		link()
	elif an == '5':
		dd = cc[5].find('a')
		link()
	elif an == '6':
		dd = cc[6].find('a')
		link()
	elif an == '7':
		dd = cc[7].find('a')
		link()
	elif an == '8':
		dd = cc[8].find('a')
		link()
	elif an == '9':
		dd = cc[9].find('a')
		link()
	else:
		print(f"{merah}[!] Masukkan Pilihan Yang Benar!!")
except ConnectionError:
	print(f'{merah}[!]{reset} Periksa Koneksi Internet Anda!!\n{merah}[!]{reset}Pastikan Anda Menggunakan vpn!!')
