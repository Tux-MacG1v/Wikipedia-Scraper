import bs4,colorama
import sys
import requests
import os
colorama.init()


# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = "\033[2J"
RED = "\033[31m"   # mode 31 = red forground
RESET = "\033[0m"  # mode 0  = reset
BLUE  = "\033[34m"
YELLOW = "\033[1;33m"
CYAN  = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD    = "\033[m"
REVERSE = "\033[m"
WHITE = "\033[1;37m"

def clear():
    reload(sys)
    sys.setdefaultencoding('utf8')
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][(os.name == 'nt')])
clear()
#...........................
def wikiSCRAPER(url):
	headers = {
	"Host": "en.wikipedia.org",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
	"Accept": "application/json; charset=utf-8; profile=https://www.mediawiki.org/wiki/Specs/Summary/1.2.0",
	"Referer": url,
	"X-Requested-With": "XMLHttpRequest",
	"Connection": "keep-alive",
	"Sec-Fetch-Dest": "empty",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Site": "same-origin",
	"TE": "trailers",
	}
	payload = requests.get(url,headers=headers)
	wiki = bs4.BeautifulSoup(payload.text,"html.parser")
	for txts in wiki.select('p'):
		doc = txts.getText().encode('utf-8')
		print(GREEN + "[+]" + RED + " Text Found From URL:"+ YELLOW +  url)
                open("Page-texts.txt", "a").write(doc + '\n')


urlx = open(raw_input(YELLOW + "INPUT URL-LIST: " + GREEN ),'r').read().splitlines()
for url in urlx:
	url = url.replace('\n', '').replace('\r', '')
	wikiSCRAPER(url)
	
if __name__ == '__main__':
    print(CYAN + "          Wikipedia Scraping Done!!")
