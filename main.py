import sys,os,time,random
try:
	from requests import Session
	from requests.exceptions import *
	from bs4 import BeautifulSoup as bs
	from colorama import Fore as fore, init
	init(autoreset=True)
	merah = fore.LIGHTRED_EX
	kuning = fore.LIGHTYELLOW_EX
	hijau = fore.LIGHTGREEN_EX
	biru = fore.LIGHTBLUE_EX
	magenta = fore.LIGHTMAGENTA_EX
	cyan = fore.LIGHTCYAN_EX
	hitam = fore.LIGHTBLACK_EX
	putih = fore.LIGHTWHITE_EX
	reset = fore.RESET
	r = Session()
except ImportError:
	sys.exit('Please install requirements.txt')


def menu():
	os.system('cls' if os.name == 'nt' else 'clear')
	print(f"""{magenta}    _   __     __                     _ 
   / | / /__  / /______  {hijau}____  ____  {merah}(_){magenta}
  /  |/ / _ \/ //_/ __ \{hijau}/ __ \/ __ \/ / {magenta}
 / /|  /  __/ ,< / /_/ {hijau}/ /_/ / /_/ / /  {magenta}
/_/ |_/\___/_/|_|\____{hijau}/ .___/\____/_/   {magenta}
                     {hijau}/_/                {reset}
{putih}[{hijau}+{putih}]{hijau} coded {putih}AkasakaID
{putih}[{hijau}+{putih}] {cyan}nekopoi cli version
""")
ua = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
url = 'https://nekopoi.care'

def dl(link,proxy):
	a = r.get('https://nekopoi.care'+link,headers=ua,proxies={'http':'http://'+proxy,'https':'https://'+proxy}).text
	b = bs(a,'html.parser')
	c = b.find('div',attrs={'class':'arealinker'})
	d = c.findAll('div',attrs={'class':'liner'})
	for e in d:
		f = e.find('div',attrs={'class':'name'}).text
		print(f)
		g = e.find('div',attrs={'class':'listlink'})
		h = e.findAll('a')
		for i in h:
			print(i.text,i['href'])

def rumah(url,proxy):
	try:
		a = r.get(url,headers=ua,proxies={'http':'http://'+proxy,'https':'https://'+proxy}).text
		b = bs(a,'html.parser')
		c = b.find('div',attrs={'class':'rightarea'}).find('div',attrs={'id':'boxid'})
		d = c.findAll('div',attrs={'class':'eroinfo'})
		z = 1
		for e in d:
			f = e.find('h2').text
			print(f'{cyan}{z}{merah}.{putih}{f}')
			z += 1
		print(f'{cyan}00{merah}.{putih}go to next page')
		print(f'{cyan}99{merah}.{putih}exit')
		while True:
			try:
				pil = int(input(f'{kuning}masukan pilihanmu : {cyan}'))
				if pil == 0 or pil == 00:
					url = 'https://nekopoi.care'+b.find('a',attrs={'class':'next page-numbers'})['href']
					menu()
					rumah(url,proxy)
					break
				elif pil == 99 or pil == 9:sys.exit(f'\n{merah}bye bye ^_^')
				else:
					link = d[pil-1].find('a')
					dl(link['href'],proxy)
					break
			except ValueError:continue
			except IndexError:continue
	except KeyboardInterrupt:sys.exit(f'\n{merah}bye bye ^-^')
	except ConnectionError:sys.exit(f'\nno internet, please check your connection ^-^')

def cari(url,proxy):
	try:
		a = r.get(url,headers=ua,proxies={'http':'http://'+proxy,'https':'https://'+proxy}).text
		b = bs(a,'html.parser')
		if b.find('div',attrs={'class':'postsbody'}).find('h2').text == "Tidak ada hasil":
			print('tidak ada hasil !!')
			query = input('apa yang anda cari ? ')
			cari(f'https://nekopoi.care/?s={query}&post_type=anime',proxy)
		c = b.find('div',attrs={'class':'result'}).find('ul').findAll('li')
		z = 1
		for d in c:
			print(f'{cyan}{z}{merah}.{putih}'+d.find('h2').find('a').text)
			z += 1
		print(f'{cyan}00{merah}.{putih}go to next page')
		print(f'{cyan}99{merah}.{putih}exit')
		while True:
			try:
				pil = int(input('masukkan pilihanmu : '))
				if pil == 00:
					url = 'https://nekopoi.care'+b.find('a',attrs={'class':'next page-numbers'})['href']
					menu()
					cari(url,proxy)
					break
				elif pil == 99:
					sys.exit(f'\n{merah}bye bye ^-^')
				else:
					g = c[pil-1].find('h2').find('a')['href']
					if '/hentai/' in g:
						print('pilihan yang anda pilih tidak bisa didownload karena pilihan yang anda pilih adalah informasi anime !!')
						continue
					dl(g,proxy)
					break
			except IndexError:continue
			except ValueError:continue
	except KeyboardInterrupt:sys.exit(f'{merah}\nbye bye ^-^')
if __name__ == "__main__":
	menu()
	while True:
		try:
			print('try getting proxy..                    ',flush=True,end='\r')
			time.sleep(1)
			a = r.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=50&country=all&ssl=all&anonymity=all',headers=ua).text
			pr = a.split()
			prx = random.choice(pr)
			print(f'try to connecting nekopoi.care  ',end='\r',flush=True)
			a = r.get('https://nekopoi.care',headers=ua,proxies={'http':'http://'+prx,'https':'https://'+prx},timeout=60)
			while True:
				try:
					asj = int(input(f'{cyan}1{merah}.{putih}beranda [update]                         \n{cyan}2{merah}.{putih}cari\n{kuning}masukan pilihanmu {merah}:{cyan}'))
					if asj == 1:
						menu()
						rumah(url,prx)
						break
					elif asj == 2:
						menu()
						query = input('apa yang anda cari ? ')
						cari(f'https://nekopoi.care/?s={query}&post_type=anime',prx)
						break
					else:print(f'{merah}masukan pilihan yang benar')
				except ValueError:continue
		except ConnectionError:print(f'failed to connect nekopoi.care',flush=True,end='\r')
		except HTTPError or SSLError:print(f'failed to connect nekopoi.care',flush=True,end='\r')
		except KeyboardInterrupt:sys.exit()