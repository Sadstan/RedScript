#ecoding: utf-8
import requests
from os import system
import time
import hashlib

# red.py
# coded by sadstan

# Funcionalidades

# gerador de hashes
# quebrador de hashes
# codigo-fonte
# em breve novas novidades.

# ===============================

def banner():
    print"""
\033[32m \033[1m
 		..:::::::::..
           ..:::aad8888888baa:::..
        .::::d:?88888888888?::8b::::.
      .:::d8888:?88888888??a888888b:::.
    .:::d8888888a8888888aa8888888888b:::.
   ::::dP::::::::88888888888::::::::Yb::::
  ::::dP:::::::::Y888888888P:::::::::Yb::::
 ::::d8:::::::::::Y8888888P:::::::::::8b::::
.::::88::::::::::::Y88888P::::::::::::88::::.
:::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
:::::::Y88888888888P::|::Y88888888888P:::::::
::::::::::::::::888:::|:::888::::::::::::::::
`:::::::::::::::8888888888888b::::::::::::::'
 :::::::::::::::88888888888888::::::::::::::
  :::::::::::::d88888888888888:::::::::::::
   ::::::::::::88::88::88:::88::::::::::::
    `::::::::::88::88::88:::88::::::::::'
      `::::::::88::88::P::::88::::::::'
        `::::::88::88:::::::88::::::'
           ``:::::::::::::::::::''
                ``:::::::::''
\033[0;0m \033[0;0m
\033[36m \033[1m=>\033[0;0m \033[0;0m  1.1
\033[36m \033[1m=>\033[0;0m \033[0;0m  new version
\033[36m \033[1m=>\033[0;0m \033[0;0m  new ferraments
\033[36m \033[1m=>\033[0;0m \033[0;0m  name renoved
\033[36m \033[1m=>\033[0;0m \033[0;0m  help para ajudas
\033[36m \033[1m=>\033[0;0m \033[0;0m  new design

\033[32m \033[1m[+]\033[0;0m \033[0;0m script coded by sadstan
\033[32m \033[1m[+]\033[0;0m \033[0;0m acess github.com/sadstan

\033[33m \033[1m[*]\033[0;0m \033[0;0m Criptografias
\033[33m \033[1m[*]\033[0;0m \033[0;0m md5
\033[33m \033[1m[*]\033[0;0m \033[0;0m sha256
    """

banner()

def help():
    print"""
    codado by Pedro
    \033[36mwww.github.com/sadstan\033[0;0m

Ajuda
	help 	(ajuda)
	exit 	(sair)
Comandos Externos
	ls 	(lista arquivos do seu pc)
	ls -l
Ambiente
	banner	(Imprime a banner do script)

Mais opcoes (hashs etc)
	no-downloader (para acessar outros comandos do script)
	comandos funcionais:
		exit	(Imprime a banner do script)
		banner	(Imprime a banner do script)
		help	(Ajuda) 
		
	podera tambem acessar outros codigos como hashs etc para isso:
		enter hash_md5
	comandos funcionais no console:
		banner	(Imprime a banner do script)
		exit	(Encerra o script)
		ls	(Lista os arquivos)
		ls -l
		help 	(ajuda)

    """

def sistema():
	while True:
		console = raw_input("\n\n~Console \033[31m \033[1m(Setado para Download (HTML) )\033[0;0m \033[0;0m > ")
		if console == "no-downloader":
			while True:
				console_no_downloader = raw_input("~Console \033[31m \033[1m(no_downloader)\033[0;0m \033[0;0m > ")
				if console_no_downloader == "help":
					help()
				elif console_no_downloader == "exit":
					sistema()
				elif console_no_downloader == "ls":
					system("ls")
				elif console_no_downloader == "ls -l":
					system("ls -l")
				elif console_no_downloader == "clear":
					system('reset')
				elif console_no_downloader == "banner":
					banner()
				elif console_no_downloader == "enter hash_md5": #hashes
					print"\n\033[34m \033[0;0m########\nHASH MD5\n######## \033[0;0m \033[0;0m"
					print"""
\033[33m \033[1m[*]\033[0;0m \033[0;0m Criptografias
\033[33m \033[1m[*]\033[0;0m \033[0;0m md5
\033[33m \033[1m[*]\033[0;0m \033[0;0m sha256

\033[32m \033[1m[+]\033[0;0m \033[0;0m md5 actived
\033[32m \033[1m[+]\033[0;0m \033[0;0m digite sua senha

\033[32m \033[1m[+]\033[0;0m \033[0;0m acess github.com/sadstan
					"""
					print"""
\033[34m \033[1m Md5\nCriptografia\nCoded by sadstan\033[0;0m \033[0;0m
					"""
					while True:
						hashes = hashlib.md5()
						hash_console = raw_input("\n\n~Console \033[31m \033[1m(console/no-downloader/md5)\033[0;0m \033[0;0m Entre com a senha > ")
						hashes.update(hash_console)
						print"""						
|------------|
| SUA SENHA  |
|------------|
						"""
						print hashes.hexdigest()

						if hash_console == "exit":
							sistema()
						elif hash_console == "ls":
							system("ls")
						elif hash_console == "ls -l":
							system("ls -l")
						elif hash_console == "clear":
							system("clear")
						elif hash_console == "help":
							help()
						else:
							print"[!]"

				elif console_no_downloader == "enter sha256":

						print"""
************
\033[34m \033[1mSHA256 \033[0;0m
************
						"""
						while True:
							hashes = hashlib.sha256()
							hash_console = raw_input("\n\n~Console \033[31m \033[1m(console/no-downloader/sha256)\033[0;0m \033[0;0m Entre com a senha > ")
							hashes.update(hash_console)
							print"""
************
\033[34m \033[1mSHA256 \033[0;0m
************
							"""
							print hashes.hexdigest()
						
							if hash_console == "exit":
								sistema()
							elif hash_console == "ls":
								system("ls")
							elif hash_console == "ls -l":
								system("ls -l")
							elif hash_console == "clear":
								system("clear")
							elif hash_console == "help":
								help()
				else:
					print('\nloading')
		elif console == "clear":
			system('reset')
		elif console == 'help':
			help()
		elif console == 'exit':
			exit()
		elif console == 'ls':
			system('ls')
			
		try: # tratamento de erros da requisicao web / codigo fonte <=
			time.sleep(5)
			req = requests.get(console)
			arquivo = req.text
			print(arquivo)
		except:
			print("\nhttp ou https")

sistema()
