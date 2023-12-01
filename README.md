# Monitoreo de archivo Shadow

Este script de Python monitorea cambios en el archivo `/etc/shadow` en un sistema Linux. Este archivo contiene las contraseñas de los usuarios en formato hash. Si el archivo cambia (lo que podría indicar que se ha cambiado una contraseña), el script envía un correo electrónico de alerta.

## Uso

1. Asegurarse de tener un servidor SMTP en ejecución en tu máquina local. Este script está configurado para usar Sendmail, pero puedes modificarlo para usar otro servidor si lo prefieres.

2. Modificar el archivo JSON `config.json` con la dirección de correo electrónico a la que se enviarán las alertas y desde cuál correo. Este es el formato:
    
    ```json
    {
        "FROM": "<from-email-address>",
        "TO": "<to-email-address>"
    }
    ```


3. Ejecuta el script con Python 3:

```bash
python3 verify-shadow-file.py
```
El script se ejecutará indefinidamente, comprobando el archivo /etc/shadow cada 10 segundos. Si detecta un cambio en el archivo, enviará un correo electrónico de alerta a la dirección especificada, esperando 5 segundos antes de volver a enviar otro correo electrónico.

## Advertencia

Este script lee el archivo /etc/shadow, que contiene información sensible. Asegurarse de tener los permisos adecuados para leer este archivo y de manejar la información que proporciona de manera segura.