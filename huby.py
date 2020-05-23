#libs
import requests
import json

#main
class GithubGetInfo():

	def __init__(self, user):
		self._user = user


	def get_repos(self):
		re = requests.get(
			f'https://api.github.com/users/{self._user}/repos')		
		if re.status_code == 200:
			return re.json()
		else:
			print("conexão impossivel")


	def get_followers(self):
		re = requests.get(
			f'https://api.github.com/users/{self._user}/followers')
		if re.status_code == 200:
			return re.json()
		else:
			return re.status_code

	def show_repos(self):
		dados_api = self.get_repos()
		if type(dados_api) is not int:
			print("\t[REPOSITORIOS]")
			for i in range(len(dados_api)):
				print("\t ╚═ "+dados_api[i]['html_url'])
		else:
			print(dados_api)

	def show_followers(self):
		dados_api = self.get_followers()
		if type(dados_api) is not int:
			print("\n\t[SEGUIDORES]")
			for i in range(len(dados_api)):
				print("\t ╚═ "+dados_api[i]['html_url'])
		else:
			print(dados_api)

	def menu():
		banner = """
             __    __   ,_ __  __   _
            ( /  /( /  /( /  )( /  /
             /--/  /  /  /--<  (__/
            /  /_ (_,/_ /___/   _/_
                   V.1          //
                by HaguacomH  (/
		"""
		print(banner)


get_info = GithubGetInfo.menu()
get_info = GithubGetInfo('joaroquedev')
get_info.show_repos()
get_info.show_followers()
