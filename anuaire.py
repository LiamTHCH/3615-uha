
import requests
from lxml import html
url = "https://annuaire.uha.fr/index.php"
co = str(input("Valeur token :"))
cookies = {'Annuaire': co}
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
		self.nom = self.tree.xpath('//span[@class="majuscules"]/text()')
		self.prenom = self.tree.xpath('//span[@class="gras"]/text()')
		del self.prenom[-1]
		self.uni = test = self.tree.xpath('//div[@class="xl-col-6 l-col-6 m-col-6 ml-col-6 s-col-12 sl-col-12"]/p/text()')
		self.mail = test = self.tree.xpath('//div[@class="xl-col-6 l-col-6 m-col-6 ml-col-6 s-col-12 sl-col-12 droite"]/p/a/text()')
		self.tel = self.tree.xpath('//div[@class="xl-col-6 l-col-6 m-col-6 ml-col-6 s-col-12 sl-col-12 droite"]/p/span/a/text()')
		return dict(nom=self.nom + self.prenom, adresse=self.mail,cp="", ville=self.uni, tel=self.tel.string)
	
	def getlist(self,term):
		requests.get("https://annuaire.uha.fr/index.php?type=pers",cookies=cookies)
		response = requests.post(url, allow_redirects=False, data={
				'search': user,
				'action': 'Chercher'
			}, cookies=cookies)
		self.tree = html.fromstring(response.content)
		self.nom = self.tree.xpath('//span[@class="majuscules"]/text()')
		self.prenom = self.tree.xpath('//span[@class="gras"]/text()')
		self.listprof.append(self.nom + self.prenom)
		requests.get("https://annuaire.uha.fr/index.php?type=etud",cookies=cookies)
		response = requests.post(url, allow_redirects=False, data={
				'search': user,
				'action': 'Chercher'
			}, cookies=cookies)
		self.tree = html.fromstring(response.content)
		self.nom = self.tree.xpath('//span[@class="majuscules"]/text()')
		self.prenom = self.tree.xpath('//span[@class="gras"]/text()')
		self.listeleve.append(self.nom + self.prenom)
	def searchglobal(self,nom):
		res = []
		self.getlist(nom)
		for user in self.listprof:
			res.append(self.search(user))
		for user in self.listeleve:
			res.append(self.search(user))
		return res




