
from os import PRIO_PGRP
import requests
from lxml import html
url = "https://annuaire.uha.fr/index.php"
co = str(input("Valeur token :"))
cookies = {'Annuaire': 'ST-290900-cYrLP5PDOfi0Jc2IoCyl--Y8PuY-cas6uhafr'}
class anuaire:
	def __init__(self, url):
		self.name = str()
		self.tel = str()
		self.nom = str()
		self.prenom = str()
		self.uni = str()
		self.mail = str()
		self.name = str()
		self.tree = 0
		self.listeleve = []
		self.listprof = []
		self.tels = []
		self.noms = []
		self.prenoms = []
		self.unis = []
		self.mails = []
	def search(self,name,type):
		user = name
		if type == "prof" : requests.get("https://annuaire.uha.fr/index.php?type=pers",cookies=cookies)
		elif type == "eleve" : requests.get("https://annuaire.uha.fr/index.php?type=etud",cookies=cookies)
		else: exit(-1)
		response = requests.post(url, allow_redirects=False, data={
				'search': user,
				'action': 'Chercher'
			}, cookies=cookies)
		#print (response.content)
		self.tree = html.fromstring(response.content)
		self.nom = list(self.tree.xpath('//span[@class="majuscules"]/text()'))
		self.prenom = list(self.tree.xpath('//span[@class="gras"]/text()'))
		del self.prenom[-1]
		self.uni = self.tree.xpath('//div[@class="xl-col-6 l-col-6 m-col-6 ml-col-6 s-col-12 sl-col-12"]/p/text()')
		self.mail = list(self.tree.xpath('//div[@class="xl-col-6 l-col-6 m-col-6 ml-col-6 s-col-12 sl-col-12 droite"]/p/a/text()'))
		self.tel = list(self.tree.xpath('//div[@class="xl-col-6 l-col-6 m-col-6 ml-col-6 s-col-12 sl-col-12 droite"]/p/span/a/text()'))
		if not bool(self.prenom): return ""
		if not bool(self.tel): self.tel = ""
		else: self.tel = self.tel[0]
		return dict(nom=str(str(self.nom[0]) +" "+ str(self.prenom[0])), adresse=str(self.mail[0]),cp="", ville="", tel=str(self.tel))
			
	
	def getlist(self,term):
		requests.get("https://annuaire.uha.fr/index.php?type=pers",cookies=cookies)
		response = requests.post(url, allow_redirects=False, data={
				'search': term,
				'action': 'Chercher'
			}, cookies=cookies)
		self.tree = html.fromstring(response.content)
		self.noms = self.tree.xpath('//span[@class="majuscules"]/text()')
		self.prenoms = self.tree.xpath('//span[@class="gras"]/text()')
		self.listprof.append(str(self.nom) +" "+ str(self.prenom))
		requests.get("https://annuaire.uha.fr/index.php?type=etud",cookies=cookies)
		response = requests.post(url, allow_redirects=False, data={
				'search': term,
				'action': 'Chercher'
			}, cookies=cookies)
		self.tree = html.fromstring(response.content)
		self.noms = self.tree.xpath('//span[@class="majuscules"]/text()')
		self.prenoms = self.tree.xpath('//span[@class="gras"]/text()')
		self.listeleve.append(str(self.nom) +" "+ str(self.prenom))
	def searchglobal(self,term):
		user = term
		res = []
		self.search(user,"eleve")
		self.prenoms = list(self.prenom)
		self.noms = list(self.nom)
		if len(self.prenoms) != 1:
			for i in range(0,len(self.noms)):
				print("search for",str(self.prenoms[i]+" "+self.noms[i]))
				res.append(self.search(self.prenoms[i]+" "+self.noms[i],"eleve"))
		else:
			res.append(self.search(user,"eleve"))
		requests.get("https://annuaire.uha.fr/index.php?type=pers",cookies=cookies)
		response = requests.post(url, allow_redirects=False, data={
				'search': user,
				'action': 'Chercher'
			})
		self.tree = html.fromstring(response.content)
		self.noms = list(self.tree.xpath('//span[@class="majuscules"]/text()'))
		self.prenoms = list(self.tree.xpath('//span[@class="gras"]/text()'))
		for i in range(0,len(self.noms)):
			print("search for",str(self.prenoms[i]+" "+self.noms[i]))
			res.append(self.search(self.prenoms[i]+" "+self.noms[i],"prof"))
		return res






