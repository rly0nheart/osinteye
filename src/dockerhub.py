import requests
from lib.colors import red,white,green,reset

# Getting user's DockerHub profile information'              
def dockerhub(self):
    response = self.session.get(self.url)
    if response.status_code != 200:
        exit(f"{white}[{red}-{white}] dockerhub: user not found{reset} ")
    response = response.json()
            
    data = {'ID': response['id'],
	             'Profile': response['profile_url'],
	             'Gravatar': response['gravatar_url'],
	             'Username': response['username'],
	             'Location': response['location'],
	             'Account type': response['type'],
	             'Organization': response['company'],
	             'Joined on': response['date_joined']
    }
    print(f"\n{white}{response['full_name']} | Dockerhub{reset}")
    for key,value in data.items():
        print(f"{white}├─ {key}: {green}{value}{reset}")
