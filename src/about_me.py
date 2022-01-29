import requests
from bs4 import BeautifulSoup
from lib.colors import red,white,green,reset

# About.me 
def about_me(self):
    request = requests.get(self.url)
    if request.status_code != 200:
    	print(f'{white}[{red}-{white}] about.me: user not found{reset}')
    else:
    	soup = BeautifulSoup(request.text, 'html.parser')
    	data = {'Name': soup.h1.string,
    	             'Occupation': soup.main.span.get_text(),
    	             'Summary': soup.h2.get_text()
    	}            
    	print(f'\n{white}{soup.title.string}{reset}')
    	for key, value in data.items():
    	    print(f"{white}├─ {key}: {green}{value}{reset}")
    	print(green,soup.p.string,reset)
    	
    	print(f'\n{white}Social links{reset}')
    	for link in soup.main.find_all('a'):
    	    print(green,link.get('href'),reset)
