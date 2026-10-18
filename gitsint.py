#Libs
import os
import platform
import json
import re
import argparse
import sys

#LIBME
from src.base_sint import captura_perfil, captura_repos, captura_commits, checa_commit

#Outros
versao = '0.1'
sistema = platform.system()

#Classes
class texto():
	reseta = '\u001b[0m'
	negrito = '\u001b[1m'
	italico = '\u001b[3m'
	underline = '\u001b[4m'
	piscapisca = '\u001b[5m'
	invertido = '\u001b[7m'
	strike = '\u001b[9m'
	doisunderline = '\u001b[21m'
	class cor():
		preto = '\u001b[38;5;240m'
		branco = '\u001b[38;5;255m'
		azul = '\u001b[38;5;4m'
		verde = '\u001b[38;5;40m'
		vermelho = '\u001b[38;5;124m'
		amarelo = '\u001b[38;5;11m'
		azul_claro = '\u001b[38;5;87m'
		verde_claro = '\u001b[38;5;85m'
		vermelho_claro = '\u001b[38;5;196m'
		amarelo_claro = '\u001b[38;5;220m'
	class fundo():
		preto = '\u001b[48;5;240m'
		branco = '\u001b[48;5;255m'
		azul = '\u001b[48;5;4m'
		verde = '\u001b[48;5;40m'
		vermelho = '\u001b[48;5;124m'
		amarelo = '\u001b[48;5;11m'
		azul_claro = '\u001b[48;5;87m'
		verde_claro = '\u001b[48;5;85m'
		vermelho_claro = '\u001b[48;5;196m'
		amarelo_claro = '\u001b[48;5;220m'
def clear():
	if sistema == "Windows":
		os.system("cls")
	else:
		os.system('clear')
def log(txt):
	print(f'{texto.negrito}{texto.italico}{texto.cor.branco}{txt}{texto.reseta}')
def sucesso(txt):
	print (f'{texto.negrito}{texto.cor.verde_claro}{txt}{texto.reseta}')
def erro(txt):
	print (f'{texto.fundo.vermelho} {texto.reseta} {texto.negrito}{texto.italico}{texto.cor.vermelho_claro}{txt}{texto.reseta} {texto.fundo.vermelho} {texto.reseta}')
def opc(um, dos):
	print (f'{texto.negrito}{texto.cor.branco}[{texto.cor.vermelho_claro}{um}{texto.cor.branco}] {texto.cor.vermelho_claro}{dos}{texto.reseta}')
def opc2(um, dos):
	print (f'{texto.negrito}{texto.cor.branco}[{texto.cor.amarelo}{um}{texto.cor.branco}] {texto.cor.amarelo}{dos}{texto.reseta}')
def titulo(tetulorkkkkk):
	print (f'{texto.negrito}{texto.cor.branco}| {texto.underline}{texto.cor.vermelho_claro}{tetulorkkkkk}{texto.reseta} {texto.negrito}{texto.cor.branco}|{texto.reseta}\n')

def alerta(tipo, mensagem):
	estilos = {
		'sucesso': ('✓', texto.cor.verde_claro),
		'erro':    ('✗', texto.cor.vermelho_claro),
		'alerta':  ('⚠', texto.cor.amarelo_claro),
		'info':    ('ℹ', texto.cor.branco),
		'ajuda':   ('?', texto.cor.amarelo_claro)
	}

	tipo_lower = tipo.lower()
	if tipo_lower not in estilos:
		tipo_lower = 'info'
        
	simbolo, cor = estilos[tipo_lower]
	largura_conteudo = len(mensagem) + 4
    
	print(f'{texto.negrito}{texto.cor.branco}╭{"─" * (largura_conteudo + 2)}╮{texto.reseta}')
	print(f'{texto.negrito}{texto.cor.branco}│  {cor}{simbolo}  {mensagem}{texto.cor.branco} │{texto.reseta}')
	print(f'{texto.negrito}{texto.cor.branco}╰{"─" * (largura_conteudo + 2)}╯{texto.reseta}')

def caixa_sint(link_titulo, bloco_texto):
    linhas = [l.strip() for l in bloco_texto.strip().split('\n') if l.strip()]
    
    # Conta o tamanho ignorando os códigos ANSI (\033...), mas mantém a cor intacta
    comprimento = lambda t: len(re.sub(r'\033\[[0-9;]*m', '', t))
    
    maior_linha = max(comprimento(l) for l in linhas)
    largura_conteudo = max(maior_linha, comprimento(link_titulo) + 6)
    
    # 1. Topo (Exibe o link com a cor original)
    espaco_tracos = largura_conteudo - comprimento(link_titulo)
    metade_esq = espaco_tracos // 2
    metade_dir = espaco_tracos - metade_esq
    print(f"┌{'─' * (metade_esq - 1)} {texto.cor.vermelho_claro}{link_titulo}{texto.cor.branco} {'─' * (metade_dir+1)}┐")
    
    # 2. Miolo (Exibe suas linhas com as cores originais do seu print)
    for linha in linhas:
        espacos_vazios = largura_conteudo - comprimento(linha)
        print(f"│ {linha}{' ' * espacos_vazios} │")
        
    # 3. Base
    print(f"└{'─' * (largura_conteudo + 2)}┘")
	
def logo():
	print (f"""                          
{texto.cor.azul_claro}   █████████   ███   █████     {texto.cor.vermelho_claro}█████████  █████ ██████   █████ ███████████
{texto.cor.azul_claro}  ███▒▒▒▒▒███ ▒▒▒   ▒▒███     {texto.cor.vermelho_claro}███▒▒▒▒▒███▒▒███ ▒▒██████ ▒▒███ ▒█▒▒▒███▒▒▒█
{texto.cor.azul_claro} ███     ▒▒▒  ████  ███████  {texto.cor.vermelho_claro}▒███    ▒▒▒  ▒███  ▒███▒███ ▒███ ▒   ▒███  ▒ 
{texto.cor.azul_claro}▒███         ▒▒███ ▒▒▒███▒   {texto.cor.vermelho_claro}▒▒█████████  ▒███  ▒███▒▒███▒███     ▒███    
{texto.cor.azul_claro}▒███    █████ ▒███   ▒███     {texto.cor.vermelho_claro}▒▒▒▒▒▒▒▒███ ▒███  ▒███ ▒▒██████     ▒███    
{texto.cor.azul_claro}▒▒███  ▒▒███  ▒███   ▒███ ███ {texto.cor.vermelho_claro}███    ▒███ ▒███  ▒███  ▒▒█████     ▒███    
{texto.cor.azul_claro} ▒▒█████████  █████  ▒▒█████ {texto.cor.vermelho_claro}▒▒█████████  █████ █████  ▒▒█████    █████   
{texto.cor.azul_claro}  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒    ▒▒▒▒▒   {texto.cor.vermelho_claro}▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒ ▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒  {versao}   

{texto.italico}{texto.cor.branco}┬─► Tool for capturing patches from commits.
└────► Lovingly developed by {texto.cor.azul_claro}https://t.me/fatalsec
{texto.reseta}""")
	
clear()
logo()
parser = argparse.ArgumentParser(description=None, epilog = f"Example of use: python3 {sys.argv[0]} --help\npython3 {sys.argv[0]} --get https://github.com/user", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("--get", metavar='GITHUB-LINK', type=str, required=False, help="Perform a full profile scan")
parser.add_argument("--simple", metavar='GITHUB-LINK', type=str, required=False, help="Simple profile scan")
parser.add_argument("--commit", metavar='GITHUB-COMMIT-LINK', type=str, required=False, help="Simple commit parse")
parser.add_argument("--repo", metavar='GITHUB-REPO-LINK', type=str, required=False, help="Simple repo parse")

args = parser.parse_args()

if len(sys.argv) == 1:
	alerta('erro', f"You haven't entered any arguments, try: python3 {sys.argv[0]} --help!")
	exit()

if args.repo:
	alvo = args.repo
	alerta('info', f'Scanning {alvo} ...')
	commites = captura_commits(alvo)
	total = len(commites)
	clear()
	logo()
	alerta('sucesso', f'{total} commits were found!')
	for i in range(total):
		bruto = []
		commit = (commites[i])
		cm = checa_commit(commit)
		for chave in cm.keys():
			bruto.append(f'{texto.negrito}{texto.cor.branco}{chave.upper()} > {texto.cor.azul_claro}{cm[chave]}{texto.reseta}')
		caixa_sint(f'Commit [{i+1}/{total}]', '\n'.join(bruto))
	
if args.commit:
	alvo = args.commit
	alerta('info', f'Scanning {alvo} ...')
	x = checa_commit(alvo)
	clear()
	logo()
	bruto = []
	for chave in x.keys():
		bruto.append(f'{texto.negrito}{texto.cor.branco}{chave.upper()} > {texto.cor.azul_claro}{x[chave]}{texto.reseta}')
	caixa_sint('COMMIT INFO', '\n'.join(bruto))

if args.simple:
	if not 'github.com' in args.simple:
		erro('Error, check if the entered username is a GitHub link.')
		exit()
	alvo = args.simple
	alerta('info', f'Scanning {alvo} ...')
	perfil = captura_perfil(alvo)
	repos = captura_repos(alvo)
	clear()
	logo()	
	alerta('sucesso', f'Success in {alvo} !')
	bruto = []
	for chave in perfil.keys():
		bruto.append(f'{texto.negrito}{texto.cor.branco}{chave.upper()} > {texto.cor.azul_claro}{perfil[chave]}{texto.reseta}')
	bruto.append(f'{texto.negrito}{texto.cor.branco}REPOSITORIES > {texto.cor.azul_claro}{len(repos)}{texto.reseta}')
	caixa_sint(alvo, '\n'.join(bruto))
	
	#REPOS
	bruto = []
	for repo in repos:
		bruto.append(f'{texto.negrito}{texto.cor.branco}REPO > {texto.cor.azul_claro}{repo}{texto.reseta}')
	caixa_sint('REPOS', '\n'.join(bruto))


if args.get:
	if not 'github.com' in args.get:
		erro('Error, check if the entered username is a GitHub link.')
		exit()
	alvo = args.get
	alerta('info', f'Scanning {alvo} ...')
	perfil = captura_perfil(alvo)
	repos = captura_repos(alvo)
	
	clear()
	logo()
	alerta('sucesso', f'Success in {alvo} !')
	bruto = []
	for chave in perfil.keys():
		bruto.append(f'{texto.negrito}{texto.cor.branco}{chave.upper()} > {texto.cor.azul_claro}{perfil[chave]}{texto.reseta}')
	bruto.append(f'{texto.negrito}{texto.cor.branco}REPOSITORIES > {texto.cor.azul_claro}{len(repos)}{texto.reseta}')
	caixa_sint(alvo, '\n'.join(bruto))
	
	#REPOS
	bruto = []
	for repo in repos:
		bruto.append(f'{texto.negrito}{texto.cor.branco}REPO > {texto.cor.azul_claro}{repo}{texto.reseta}')
	caixa_sint('REPOS', '\n'.join(bruto))
	
	#COMMITS
	commits = []
	alerta('info', 'Capturing commits, please wait...')
	for repo in repos:
		commits.extend(captura_commits(repo))
	alerta('sucesso', f'{len(commits)} commits were found!')
	emails = set()
	nomes = set()
	alerta('info', 'The process may take some time, please wait!')
	for commit in commits:
		comite = checa_commit(commit)
		print (comite)
		try:
			emails.add(comite['email'])
			alerta('sucesso', f"Email found! {comite['email']}")
		except:
			None
		try:
			nomes.add(comite['name'])
			alerta('sucesso', f"Name found! {comite['name']}")
		except:
			None
	bruto = []
	for email in emails:
		bruto.append(f'{texto.negrito}{texto.cor.branco}Email > {texto.cor.azul_claro}{email}{texto.reseta}')
	caixa_sint('Emails found', '\n'.join(bruto))
	bruto = []
	for nome in nomes:
		bruto.append(f'{texto.negrito}{texto.cor.branco}Name > {texto.cor.azul_claro}{nome}{texto.reseta}')
	caixa_sint('Names/Usernames found', '\n'.join(bruto))
