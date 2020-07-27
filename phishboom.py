#!/usr/env/python3
#codint: utf-8


#Autor: xaxxjs (https://github.com/sergioab7)

import smtplib
from smtplib import SMTP 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders


import os,sys
from beautifultable import BeautifulTable
from colorama import Fore, Back, Style
import signal
import warnings
from time import sleep
warnings.filterwarnings("ignore")


def banner():
    print("""
                ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄ 
                ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌
                ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌
                ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌
                ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌ ▐░▐░▌ ▐░▌
                ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌
                ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌   ▀   ▐░▌
                ▐░▌          ▐░▌       ▐░▌     ▐░▌               ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
                ▐░▌          ▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌
                ▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
                 ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                        """+Fore.MAGENTA+"""                        [+]By: xaxxjs   
                                                [+]Web: https://sergioab7.github.io/ 
                                                [+]Github: https://github.com/sergioab7  

    [*] command: help                     

"""+Fore.RESET)
os.system("clear")
banner()

def signal_handler(key,frame):
    print(Fore.YELLOW + "\n[*]" + Fore.RESET + "¡Bye-Bye! ( ͡❛ ͜ʖ ͡❛)  \n")
    print(Style.RESET_ALL)
    sys.exit(1)

signal=signal.signal(signal.SIGINT,signal_handler)

class phishboom:
    def __init__(self):
        self.current_mail="None"
        self.cantidad_passwords=0
        self.current_password="None"
        self.victim_mail="None"
        self.template="None"
        self.url_to_send="None"
        self.subject="None"
        self.add_files="None"

        self.guardado_subject=""
        self.agregar_cuentas=[]


    def options(self):
        try:
            table=BeautifulTable()
            table.set_style(BeautifulTable.STYLE_GRID)
            test=table.columns.header=[Fore.CYAN+"NAME"+Fore.RESET,Fore.CYAN+"CURRENT"+Fore.RESET,Fore.CYAN+"REQUIRED"+Fore.RESET,Fore.CYAN+"DESCRIPTION"+Fore.RESET]
            table.append_row([f"my_mail",self.current_mail,"yes","set your fake email"])
            table.append_row([f"my_password",self.current_password,"yes","set password email"])
            table.append_row([f"victim_mail",self.victim_mail,"yes","set the NUMBER of victim mails"])
            table.append_row([f"template",self.template,"yes","set template [facebook,instagram]"])
            table.append_row([f"subject",self.subject,"yes","set subject of email"])
            table.append_row([f"url",self.url_to_send,"yes","set url to phising(ngrok, etc..)"])
            table.append_row([f"add_files",self.add_files,"no","set add_files to send with mail"])
            table.append_row([f"run", None ,None,"run exploit"])
            for i in test:
                table.left_padding_widths[i]=2
                table.right_padding_widths[i]=4
            print(table)
        except Exception as e:
            print("Error: %s"%(e))
    
    def help(self):
        print(Fore.BLUE + """
        -------------------------------------------------------------------------
       |*************************** COMMANDS ************************************|                                    
       |                                                                         |
       | [+] set:                                                                |
       |     [!] Examples:                                                       |
       |             set my_mail test@test.com                                   |
       |             set my_password password123                                 |
       |             set victim_mail 2                                           |
       |                     [1] Account: test@gmail.com                         |
       |                     [2] Account: test2@hotmail.com                      |
       |             set template facebook                                       |
       |             set url <url phising>                                       |
       |             set subject <messaage>                                      |
       |             set add_files <files>      [NOT REQUIRED]                   |
       |                                                                         |
       | [+] unset:                                                              |
       |             unset <NAME>                                                | 
       |                                                                         |
       | [+] options:  table of options [name,current,description]               |
       | [+] run:      send exploit [you must fill in all the parameter]         |
       |                                                                         |
       | [+] clear:    clear terminal                                            | 
       | [+] help:     this help menu                                            |
       |                                                                         |
        -------------------------------------------------------------------------
        """+Fore.RESET)
    def start(self):
        self.options()
        while True:
            try:
                consola=input(Fore.RED + "[main]$>> " + Fore.RESET)
                consola=consola.lower()
                self.parametro=consola.split()
                if(consola=="options"):
                    self.options()
                elif(consola=="clear"):
                    os.system("clear")
                    banner()
                    self.options() 
                elif(consola=="help"):
                    self.help()
                elif(consola=="run"):
                    sleep(1.5)
                    self.run()
                elif(self.parametro[0]=="set"):
                    if(self.parametro[1]=="my_mail"):
                        print(Fore.YELLOW+"\t[+] Established MAIL: %s"%(self.parametro[2]+Fore.RESET))
                        self.current_mail=self.parametro[2]
                    if(self.parametro[1]=="my_password"):
                        print(Fore.YELLOW+"\t[+] Established PASSWORD: %s"%(self.parametro[2]+Fore.RESET))
                        self.current_password=self.parametro[2]
                    if(self.parametro[1]=="victim_mail"):
                       # print(Fore.YELLOW+"\t[+] Establecido VICTIM_MAIL: %s"%(self.parametro[2]+Fore.RESET))
                       # self.victim_mail=self.parametro[2]
                       self.cantidad_passwords=int(self.parametro[2])
                       self.numero=self.cantidad_passwords
                       self.agregar_cuentas=[]
                       for i in range(0, self.numero):
                           self.numeros_cuenta=input(Fore.YELLOW+f"\t[{i+1}]"+Fore.RESET+"Account :")
                           self.agregar_cuentas.append(self.numeros_cuenta)
                       self.victim_mail=self.numero
                       print(Fore.YELLOW+"\t[+] %s Account(s) established correctly"%(self.numero)+Fore.RESET)

                    if(self.parametro[1]=="template"):
                        print(Fore.YELLOW+"\t[+] Established TEMPLATE: %s"%(self.parametro[2]+Fore.RESET))
                        self.template=self.parametro[2]

                    if(self.parametro[1]=="subject"):
                        self.guardado_subject=""
                        for i in self.parametro[2:]:
                            self.guardado_subject +=i
                            self.guardado_subject +=" "
                        print(Fore.YELLOW+"\t[+] Established SUBJECT: %s"%(self.guardado_subject+Fore.RESET))
                        self.subject=self.guardado_subject 

                    if(self.parametro[1]=="url"):
                        print(Fore.YELLOW+"\t[+] Established URL: %s"%(self.parametro[2]+Fore.RESET))
                        self.url_to_send=self.parametro[2]  

                    if(self.parametro[1]=="add_files"):
                        print(Fore.YELLOW+"\t[+] Established ADD_FILES: %s"%(self.parametro[2]+Fore.RESET))
                        self.add_files=self.parametro[2]  

                elif(self.parametro[0]=="unset"):
                    try:
                        if(self.parametro[1]=="add_files"):
                            self.add_files="None"
                        if(self.parametro[1]=="my_mail"):
                            self.current_mail="None"
                        if(self.parametro[1]=="my_password"):
                            self.current_password="None"
                        if(self.parametro[1]=="victim_mail"):
                            self.victim_mail="None"
                            for i in range(0, len(self.agregar_cuentas)-1):
                                self.agregar_cuentas.pop(i)
                            self.agregar_cuentas.pop(0)
                        if(self.parametro[1]=="template"):
                            self.template="None"
                        if(self.parametro[1]=="subject"):
                            self.subject="None"
                        if(self.parametro[1]=="url"):
                            self.url_to_send="None"
                    except:
                        print("[-] Error, parametro no detectado.")

                else:   
                    print(Fore.YELLOW + "[-]"+Fore.RESET+"Command not found")
                    print(Fore.YELLOW + "[!]"+Fore.RESET+"INFO: set <NAME> <YOUR SET>")
                    print(Fore.YELLOW + "[!]"+Fore.RESET+"More info with command: <help>")
            except Exception as e:
                print("[-] Error: %s"%(e))

    def email_facebook(self, recipients):
        
        if(self.add_files == "None"):

            body="""
                <center><img src="https://gyazo.com/31a9acc0bf433ee84bab8ca0bf772b17.png" alt="fac" width="580px" height="265px"/></center>
                <center><a href="{}"><img src="https://gyazo.com/a0c22b6d481af7944feb7b2dca25e9db.png" with="100px" height="40px" /></a></center>
                <center><p style="color: #b5b5b5">Se ha enviado este mensaje a petición tuya.</p></center>
                <center><p style="color: #b5b5b5">Facebook Ireland Ltd., Attention: Community Operations, 4 Grand Canal Square, Dublin 2, Ireland</p></center>
            """.format(self.url_to_send)
            msg=MIMEMultipart()

            msg['Subject']=self.guardado_subject
            msg['From']=self.current_mail
            msg['To'] = (', ').join(recipients.split(','))

            msg.attach(MIMEText(body,'html'))

            server=SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.current_mail,self.current_password)
            server.send_message(msg)
            
            server.quit()
            
        else:
            archivo_adjunto=open(self.add_files, "rb") #header
            adjunto_MIME=MIMEBase('application', 'octet-stream')
            adjunto_MIME.set_payload((archivo_adjunto).read())
            encoders.encode_base64(adjunto_MIME)
            nombre_adjunto=self.add_files #body
            adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
        

            body="""
                <center><img src="https://gyazo.com/31a9acc0bf433ee84bab8ca0bf772b17.png" alt="fac" width="580px" height="265px"/></center>
                <center><a href="{}"><img src="https://gyazo.com/a0c22b6d481af7944feb7b2dca25e9db.png" with="100px" height="40px" /></a></center>
                <center><p style="color: #b5b5b5">Se ha enviado este mensaje a petición tuya.</p></center>
                <center><p style="color: #b5b5b5">Facebook Ireland Ltd., Attention: Community Operations, 4 Grand Canal Square, Dublin 2, Ireland</p></center>
            """.format(self.url_to_send)
            msg=MIMEMultipart()

            msg['Subject']=self.guardado_subject
            msg['From']=self.current_mail
            msg['To'] = (', ').join(recipients.split(','))

            msg.attach(adjunto_MIME)
            msg.attach(MIMEText(body,'html'))

            server=SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.current_mail,self.current_password)
            server.send_message(msg)
            
            server.quit()
    
    def email_instagram(self, recipients):

        if(self.add_files == "None"):

            body="""
                <center><img src="https://gyazo.com/514bc73f1f39606a9ccce1c11bba331d.png" alt="new_insta" width="500px" height="200px" /></center>
                <center><a href="{}"><img src="https://i.gyazo.com/404d3dd24768851f9fcf08846762f9c8.png" with="100px" height="40px" /></a></center>
                <center><img src="https://gyazo.com/7d39fc5471d3174988013d7e61a9a49f.png" alt="instagram" width="500px" height="100px" />
            """.format(self.url_to_send)
            msg=MIMEMultipart()

            msg['Subject']=self.guardado_subject
            msg['From']=self.current_mail
            msg['To'] = (', ').join(recipients.split(','))

            msg.attach(MIMEText(body,'html'))

            server=SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.current_mail,self.current_password)
            server.send_message(msg)
            
            server.quit()
            
        else:
            archivo_adjunto=open(self.add_files, "rb") #header
            adjunto_MIME=MIMEBase('application', 'octet-stream')
            adjunto_MIME.set_payload((archivo_adjunto).read())
            encoders.encode_base64(adjunto_MIME)
            nombre_adjunto=self.add_files #body
            adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
        

            body="""
                <center><img src="https://gyazo.com/514bc73f1f39606a9ccce1c11bba331d.png" alt="new_insta" width="500px" height="200px" /></center>
                <center><a href="{}"><img src="https://i.gyazo.com/404d3dd24768851f9fcf08846762f9c8.png" with="100px" height="40px" /></a></center>
                <center><img src="https://gyazo.com/7d39fc5471d3174988013d7e61a9a49f.png" alt="instagram" width="500px" height="100px" />
            """.format(self.url_to_send)
            msg=MIMEMultipart()

            msg['Subject']=self.guardado_subject
            msg['From']=self.current_mail
            msg['To'] = (', ').join(recipients.split(','))

            msg.attach(adjunto_MIME)
            msg.attach(MIMEText(body,'html'))

            server=SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.current_mail,self.current_password)
            server.send_message(msg)
            
            server.quit()

    def run(self):
        try:
            if(self.current_mail == "None" or self.current_password == "None" or self.victim_mail == "None" or self.template == "None" or self.subject == "None"):
                print(Fore.RED + "[-]"+Fore.RESET + "You must fill in the fields ")
            else:
                if(self.template=="facebook"):
                    print(Fore.YELLOW + "[+] Lanzando script..." + Fore.RESET)
                    for i in self.agregar_cuentas:
                        self.email_facebook(i)
                    print(Fore.YELLOW+"[+] Message sent succesfully"+Fore.RESET)
                elif(self.template=="instagram"):
                    print(Fore.YELLOW + "[+] Lanzando script..." + Fore.RESET)
                    for i in self.agregar_cuentas:
                        self.email_instagram(i)
                    print(Fore.YELLOW+"[+] Message sent succesfully"+Fore.RESET)
                else:
                    print(Fore.RED + "[-]"+Fore.RESET + "You must fill in the fields ")
        except Exception as e:
            print("Error: %s"%(e))

if __name__ == "__main__":
    menu=phishboom()
    menu.start()
