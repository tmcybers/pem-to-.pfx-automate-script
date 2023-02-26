import os

# Ruta al archivo de certificado PEM
cert_file = '/ruta/al/certificado.pem'

# Ruta al archivo de clave privada PEM
private_key_file = '/ruta/a/clave/privada.pem'

# Ruta de salida para el archivo PFX
output_file = '/ruta/de/salida/archivo.pfx'

# Solicitar contraseña para el archivo PFX
password = input("Introduce una contraseña para el archivo PFX: ")

# Comando openssl para convertir PEM a PFX
cmd = f'openssl pkcs12 -export -out {output_file} -inkey {private_key_file} -in {cert_file} -password pass:{password}'

# Ejecutar el comando
os.system(cmd)

# Comprobar si se ha creado el archivo PFX
if os.path.exists(output_file):
    print(f"Archivo PFX generado exitosamente en: {output_file}")
else:
    print("Error al generar el archivo PFX.")
