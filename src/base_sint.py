import sys
import os
caminho_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_vendor = os.path.join(caminho_projeto, 'vendor')
if caminho_vendor not in sys.path:
	sys.path.insert(0, caminho_vendor)

import requests
import json
import re
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from datetime import datetime, timezone
from bs4 import BeautifulSoup as sp


#EXCEPTS
class ErroConta(Exception):
	"erro ao não inserir uma conta válida"
	pass


def limpa_data(data_original):
	formato = "%a, %d %b %Y %H:%M:%S %z"
	dt_local = datetime.strptime(data_original, formato)
	dt_utc = dt_local.astimezone(timezone.utc)
	iso_universal = dt_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
	return dt_local

def captura_perfil(alvo):
	r = requests.get(alvo)
	html = sp(r.text, 'html.parser')
	if html.title == None:
		raise ErroConta('Não encontrada!')
		return
	dados = {}
	dados.update({'photo':html.find('img', {'class':'avatar'}).attrs['src']})
	nomes = []
	for n in html.find('h1', {'class':'vcard-names'}).find_all('span'):
		nomes.append(n.text.strip())
	dados.update({'names':', '.join(nomes)})
	for a in html.find_all('div'):
		try:
			if 'user-profile-bio' in a.attrs['class']:
				dados.update({'bio':a.text.strip()})
				break
		except:
			pass
	for a in html.find_all('a'):
		if '?tab=followers' in a.attrs['href']:
			dados.update({'followers':int(a.find('span').text.strip())})
		if '?tab=following' in a.attrs['href']:
			dados.update({'following':int(a.find('span').text.strip())})
	socials = []
	for s in html.find_all('li'):
		try:
			if s.attrs['itemprop'] == 'social':
				socials.append (s.find('a').attrs['href'])
		except:
			pass
	dados.update({'social links':', '.join(socials)})
	return json.loads(json.dumps(dados, indent=2, ensure_ascii=False))
	
def captura_repos(alvo):
	r = requests.get(alvo+'?tab=repositories')
	html = sp(r.text, 'html.parser')
	repos = []
	for a in html.find('div', {'id':'user-repositories-list'}).find_all('li'):
		if 'Forked from' in a.text:
			continue
		titulo = (a.find('a').text.strip())
		link = ('https://github.com'+a.find('a').attrs['href'])
		repos.append(link)
	return repos

def captura_commits(link):
	url_final = link.rstrip('/') + '/commits/main/'
	requisicao = Request(url_final)
	with urlopen(requisicao, timeout=10) as resposta:
		html_puro = resposta.read().decode('utf-8')
	html = sp(html_puro, 'html.parser')
	commits = []
	for l in html.find_all('li'):
		try:
			if l.attrs['data-testid']:
				commits.append ('https://github.com'+l.attrs['data-commit-link'])
		except:
			pass
	return commits

def checa_commit(commit):
	r = requests.get(commit+'.patch')
	commit = {}
	for a in r.text.splitlines():
		if 'Subject: [PATCH]' in a:
			commit.update({'subject':a.split('] ')[1]})
		if 'From: ' in a:
			if 'users.noreply.github.com' in a:
				break
			commit.update({'email':a.split(': ')[1].split(' <')[1].split('>')[0]})
			commit.update({'name':a.split(': ')[1].split(' <')[0]})
		if 'Date: ' in a:
			data = (a.split(': ')[1])
			dato = limpa_data(data)
			commit.update({'date':str(dato)})
	return commit
