#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os, httplib, socket

###### criar uma função aonde vai scanear o site em busca de pagina de admin etc...
#def buscar():
try:
        os.system("clear")
        print('''\033[31m
                    ___________________________________
                    |  Author: Marcos Alexandre       |
                    |  Data: 07/04/2017               |
                    |  e-mail:systemmendax@gmail.com  |
                    |_________________________________|
                    ___________  _______     ______   _______
                    |          | |     |     |     | |   ___|
                    |___    ___| |     |_____|     | |  |___
                       |    |    |                 | |   ___|
                       |    |    |      _____      | |  |___
                       |____|    |_____|     |_____| |______|
                       \033[0;0m''')
        print('''\033[32m
                                _______     ______
                                |     |     |     |
                                |     |_____|     |
                                |                 |
                                |      _____      |
                                |_____|     |_____|

                                \033[0;0m''')

        ###################### Inciando o script informe seu nickname ########################################
        nickname_do_usuario = raw_input("\tDigite seu nickname --: ") # Pega nickname do usuario
        print "\t\t Seja Bem Vindo { "+ '\033[31m' + nickname_do_usuario + '\033[0;0m'+" }"
        print
        print("\t\t\tScript Simples Desenvolvida para achar painel de Admin\n")
        print
        print("As página que le achar se destacada!!!!\n")
        ################ Dicionario de palavra para achar painel de Admin 
        pagina = ['admin.php','admin',
                  'painel','login',
                  'admin-login','admin-index',
                  'web-admin','admin/index.php',
                  'admin/admin.php','login/home.php',
                  'adm','admin_login.php','controle',
                  'controle-agencia','controle-agencia-rs',
                  'panel','sistem','administracao'


                  ]

        valor1 = 0 # vai receber o numero de pg encontradas
        valor2 = 0 # vai receber valor de pg testada
        try:
            site = raw_input("\tinforme o Site: ")
            site = site.replace("http://","")
            print("\tOlhando Site: " + site + "....")
            conn = httplib.HTTPConnection(site)
            conn.connect()
            print "\t[$] Sim o site está Online"
        except (httplib.HTTPResponse, socket.error) as Exit:
            raw_input("\t [!] Ocorreu um erro ou site está offline ou url invalida")
            exit()
        continuar = raw_input("quer continuar? y ou n: ")
        if continuar == "y" :
            print("\t [+] Scaneando: " + site + "....")
            for url in pagina:
                url = url.replace("\n","")
                url = "/" + url
                host = site + url
                print("\t [#] Olhando: " + host + "....")
                conexao = httplib.HTTPConnection(site)
                conexao.request("GET",admin)
                responder = conexao.getresponse()
                valor2 = valor2 + 1
                ### mostrando pagina Encontrada
                if responder.status == 200:
                    valor1 = valor1 + 1
                    print

                    print "%s %s" % ("\033[41m -->" + host, "\033[0;1m ""\033[32m Páginas Encontrada !")
                    raw_input("Pressione Enter para continuar scaneando \n \033[0;0m")
                elif responder.status == 404:
                    valor2 = valor2
                elif responder.status == 302:
                    print "%s %s" % ("\033[31m -->" + host,"\033[0;0m" "esta página foi redirecionda (302 - redirecionda)")
                else:
                     conexao.close()
                print("\n\nCompletado \n")
                print valor1, "--------- Páginas Encontrada -----------"
                print valor2, "Total de Páginas Escaneadas"

except (httplib.HTTPResponse, socket.error):
    print "\n\t[!] cancelada"
except (KeyboardInterrupt, SystemExit):
    print "\n\t[!] cancelada"
