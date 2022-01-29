#!/usr/bin/env python3

import logging
import random
import argparse
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from lib.headers import user_agents
from lib.colors import red,green,white,reset
from src import about_me,instagram,github,dockerhub


class osintEye:
	def __init__(self,args):
		self.session = requests.session()
		self.session.headers = {'User-Agent': f'{random.choice(user_agents)}'}
		
		if args.about:
			self.url = f'https://about.me/{args.username}'
		elif args.instagram:
			self.url = f'https://www.instagram.com/{args.username}/?__a=1'
		elif args.github:
			self.url = f'https://api.github.com/users/{args.username}'
		elif args.dockerhub:
			self.url = f'https://hub.docker.com/v2/users/{args.username}'
		
	def main(self):
		if args.about:
			about_me.about_me(self)
		elif args.instagram:
			instagram.instagram(self)
		elif args.github:
			github.github(self,args)
		elif args.dockerhub:
			dockerhub.dockerhub(self)
		else:
		    exit(f'{white}osint{red}eye{white}: use {green}-h{white} or {green}--help{white} to view help message.{reset}')
	                                                          

start_time = datetime.now()	               	   
parser = argparse.ArgumentParser(description=f'{white}Username reconnaisance tool{reset}',epilog=f'{white}osint{red}Eye{white}  extracts a target\'s information from {green}About.me{white}, {green}Instagram{white}, {green}Github{white}, and {green}Dockerhub{white}.  developed by {green}Richard Mwewa {white}| https://github.com/{green}rly0nheart{reset}')
parser.add_argument('username',help=f'{white}[{green}REQUIRED{white}] target username{reset}')
parser.add_argument('--about',action='store_true')
parser.add_argument('--instagram',help=f'{white}[{green}OPTIONAL{white}] get target\'s Instagram information{reset}',action='store_true')
parser.add_argument('--github',help=f'{white}[{green}OPTIONAL{white}] get target\'s GitHub information{reset}',action='store_true')
parser.add_argument('--dockerhub',help=f'{white}[{green}OPTIONAL{white}] get target\'s DockerHub information{reset}',action='store_true')
parser.add_argument('-v', '--verbose', help=f'{white}[{green}RECOMMENDED{white}] enable verbosity{reset}', dest='verbose', action='store_true')
parser.add_argument('--version',version=f'{white}2022.1.0.0 released on 29th January 2022{reset}',action='version')
args = parser.parse_args()
if args.verbose:
    logging.basicConfig(format=f"{white}[{green}*{white}] %(message)s{reset}",level=logging.DEBUG)
