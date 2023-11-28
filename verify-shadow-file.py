import hashlib
import os
import smtplib
from email.message import EmailMessage

def calcular_hash(archivo):
    with open(archivo, 'rb') as f:
        bytes = f.read()
        hash = hashlib.sha256(bytes).hexdigest()
    return hash

def enviar_correo():
    msg = EmailMessage()
    msg.set_content('El archivo SHADOW ha sido modificado, por favor revisar.')
    msg['Subject'] = 'ALERTA: El archivo SHADOW ha sido modificado'
    msg['From'] = 'elian.262000@gmail.com'
    msg['To'] = 'e.bustamante02@ufromail.cl'
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('elian.262000@gmail.com', 'System.out.print("b747_$dreamliner");')
    s.send_message(msg)
    s.quit()

archivo = '/etc/shadow'
hash_inicial = calcular_hash(archivo)

while True:
    hash_actual = calcular_hash(archivo)
    if hash_actual != hash_inicial:
        enviar_correo()
        hash_inicial = hash_actual