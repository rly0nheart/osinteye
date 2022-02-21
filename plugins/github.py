import requests
from lib.colors import red,white,green,reset

# Getting github profile information    	
def github(self,args):
    response = self.session.get(self.url)
    if response.status_code != 200:
    	exit(f"{white}[{red}-{white}] github: user not found{reset} ")
    response = response.json()

    data = {'Profile photo': response['avatar_url'],
	             'Username': response['login'],
	             'User ID': response['id'],
	             'Node ID': response['node_id'],
	             'Bio': response['bio'],
	             'Blog': response['blog'],
	             'Location': response['location'],
	             'Followers': response['followers'],
    	         'Following': response['following'],
	             'Twitter handle': response['twitter_username'],
	             'Gists (public)': response['public_gists'],
	             'Repositories (public)': response['public_repos'],
	             'Organization': response['company'],
	             'Is hireable?': response['hireable'],
	             'Is site admin?': response['site_admin'],
	             'Joined On': response['created_at'],
	             'Last Updated': response['updated_at']
    }
    print(f"\n{white}{response['name']} | Github{reset}")
    for key,value in data.items():
        print(f"{white}├─ {key}: {green}{value}{reset}")
    print("\n")
    
    # Repositories
    print(f"\n{white}[{green}*{white}] Fetching @{green}{args.username}{white}' repositories...{reset}")
    response = self.session.get(f"https://api.github.com/users/{args.username}/repos?per_page=100").json()
    for repo in response:
        license = repo['license']
        if license is not None:
            license = repo['license']['name']
        repo_info = {'ID': repo['id'],
                              'Is private?': repo['private'],
                              'Forks': repo['forks'],
                              'Stars': repo['stargazers_count'],
                              'Watchers': repo['watchers'],
                              'License': license,
                              'Branch': repo['default_branch'],
                              'Visibility': repo['visibility'],
                              'Language': repo['language'],
                              'About': repo['description'],
                              'Open issues': repo['open_issues'],
                              'Topics': repo['topics'],
                              'Is archived?': repo['archived'],
                              'Homepage': repo['homepage'],
                              'Created at': repo['created_at'],
                              'Updated at': repo['updated_at'],
                              'Pushed at': repo['pushed_at'],
                              'Clone url': repo['clone_url'],
                              'SSH url': repo['ssh_url']
        }
        print(f"\n{white}{repo['full_name']}{reset}")
        for key,value in repo_info.items():
            print(f"{white}├─ {key}: {green}{value}{reset}")
