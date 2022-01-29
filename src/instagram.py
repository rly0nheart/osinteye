from lib.colors import red,white,green,reset

# Getting instagram profile information	
def instagram(self):
	response = self.session.get(self.url)
	if response.status_code != 200:
		exit(f"{white}[{red}-{white}] instagram: user not found{reset}")
	response = response.json()
	user = response['graphql']['user']
		   
	data = {'Profile photo': user['profile_pic_url_hd'],
	             'Username': user['username'],
	             'User ID': user['id'],
	             'External URL': user['external_url'],
	             'Bio': user['biography'],
	             'Followers': user['edge_followed_by']['count'],
	             'Following': user['edge_follow']['count'],
 	            'Pronouns': user['pronouns'],
	             'Images': user['edge_owner_to_timeline_media']['count'],
	             'Videos': user['edge_felix_video_timeline']['count'],
	             'Reels': user['highlight_reel_count'],
	             'Is private?': user['is_private'],
	             'Is verified?': user['is_verified'],
	             'Is business account?': user['is_business_account'],
	             'Is professional account?': user['is_professional_account'],
	             'Is recently joined?': user['is_joined_recently'],
	             'Business category': user['business_category_name'],
	             'Category': user['category_enum'],
	             'Has guides?': user['has_guides']
	}
	print(f"\n{white}{user['full_name']} | Instagram{reset}")
	for key, value in data.items():
	   print(f"{white}├─ {key}: {green}{value}{reset}")
