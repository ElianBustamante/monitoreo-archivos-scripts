import hashlib
import os
import smtplib
import time
import sys
import json
from email.message import EmailMessage

import json

# Función para obtener los correos desde el archivo de configuración
def obtener_correos():
    with open('config.json', 'r') as f:
        config = json.load(f)
    from_address = config.get('FROM')
    to_address = config.get('TO')
    if not from_address or not to_address:
        print("El archivo de configuración debe contener los correos 'FROM' y 'TO'.")
        return None, None
    return from_address, to_address

# Función para testear el envío de correos
def testear_correo():
    from_address, to_address = obtener_correos()
    if not from_address or not to_address:
        return
    
    msg = EmailMessage()
    msg.set_content('Este es un correo de prueba.')
    msg['Subject'] = 'Prueba de correo'
    msg['From'] = from_address
    msg['To'] = to_address
    try:
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()
    except smtplib.SMTPException:
        print("Error al enviar el correo de prueba. Finalizando el programa.")
        sys.exit(1)

# Función para calcular el hash del archivo
def calcular_hash(archivo):
    with open(archivo, 'rb') as f:
        bytes = f.read()
        hash = hashlib.sha256(bytes).hexdigest()
    return hash

# Función para enviar el correo de alerta
def enviar_correo():
    from_address, to_address = obtener_correos()

    msg = EmailMessage()
    msg.set_content('El archivo SHADOW ha sido modificado, por favor revisar.')
    msg['Subject'] = 'ALERTA: El archivo SHADOW ha sido modificado'
    msg['From'] = from_address
    msg['To'] = to_address
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

# Función para iniciar el monitoreo del archivo, verificando si ha sido modificado o no, y enviando el correo de alerta.
def iniciar_monitoreo():
    archivo = '/etc/shadow'
    hash_inicial = calcular_hash(archivo)
    while True:
        hash_actual = calcular_hash(archivo)
        if hash_actual != hash_inicial:
            enviar_correo()
            print('\n[Estado archivo SHADOW: MODIFICADO]')
            print('*** [ALERTA] Archivo SHADOW ha sido modificado ***\n')
            time.sleep(5)
        else: 
            print('\n[Estado archivo SHADOW: CORRECTO]\n')

        for i in range(10, 0, -1):
            print(f"\rVerificando archivo SHADOW en: {i:<2}", end="")
            time.sleep(1)

# Función para mostrar el menú principal
def menu_principal():
    print("\nScript de monitoreo de archivo SHADOW\n")
    print("[1] Iniciar monitoreo de archivo")
    print("[2] Finalizar")
    opcion = input("\nSeleccione una opción: ")
    return opcion

opcion = menu_principal()
while opcion != '2':
    if opcion == '1':
        testear_correo()
        iniciar_monitoreo()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
    opcion = menu_principal()
