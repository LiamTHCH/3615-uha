
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
		self.nom = self.tree.xpath('//span[@class="majuscules"]/text()')
		self.prenom = self.tree.xpath('//span[@class="gras"]/text()')
		del self.prenom[-1]
		self.uni = test = self.tree.xpath('//div[@class="xl-col-6 l-col-6 m-col-6 ml-col-6 s-col-12 sl-col-12"]/p/text()')
		self.mail = test = self.tree.xpath('//div[@class="xl-col-6 l-col-6 m-col-6 ml-col-6 s-col-12 sl-col-12 droite"]/p/a/text()')
		self.tel = self.tree.xpath('//div[@class="xl-col-6 l-col-6 m-col-6 ml-col-6 s-col-12 sl-col-12 droite"]/p/span/a/text()')
		return dict(nom=str(self.nom) +" "+ str(self.prenom), adresse=str(self.mail),cp="", ville=str(self.uni), tel=str(self.tel))
	
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
	def searchglobal(self,nom):
		res = []
		self.listeleve = []
		self.listprof = []
		self.getlist(nom)
		for user in self.listprof:
			print(user)
			res.append(self.search(user,"prof"))
		for user in self.listeleve:
			print(user)
			res.append(self.search(user,"eleve"))
		return res
	def searchglobal2(self,term):
		user = term
		res = []
		print(user)
		requests.get("https://annuaire.uha.fr/index.php?type=pers",cookies=cookies)
		response = requests.post(url, allow_redirects=False, data={
				'search': user,
				'action': 'Chercher'
			})
		self.tree = html.fromstring(response.content)
		self.noms = self.tree.xpath('//span[@class="majuscules"]/text()')
		self.prenoms = self.tree.xpath('//span[@class="gras"]/text()')
		del self.prenoms[-1]
		for i in range(0,len(self.noms)):
			print("search for",str(self.prenoms[i]+" "+self.noms[i]))
			res.append(self.search(self.prenoms[i]+" "+self.noms[i],"prof"))
		self.search(user,"eleve")
		self.prenoms = self.prenom
		self.noms = self.nom
		if len(self.prenoms) != 1:
			for i in range(0,len(self.noms)):
				print("search for",str(self.prenoms[i]+" "+self.noms[i]))
				res.append(self.search(self.prenoms[i]+" "+self.noms[i],"eleve"))
		else:
			res.append(self.search(user,"eleve"))
		return res





