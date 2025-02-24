from Crypto.Cipher import AES
import os

def desencriptar():
    #solicito los archivos y guardo sus nombres en una variable
    filename = input("Ingrese el nombre del archivo a desencriptar: ")
    key = input("Ingrese el nombre del archivo que contiene la llave: ")
    #si los archivos no existen se termina el codigo, si existen, se leen
    if not os.path.isfile(filename):
        print("El archivo que intenta desencriptar no existe.")
        exit()
    else:
        with open (filename, "rb") as enc_file:
            tag = enc_file.read(16)
            nonce = enc_file.read(16)
            info = enc_file.read()
    if not os.path.isfile(key):
        print("El archivo especificado no existe")
        exit()
    else:
        with open(key, "rb") as key_file:
            key = key_file.read()
    

    #Crear cifrador
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    #Descifrando
    plaintext = cipher.decrypt_and_verify(info, tag)

    #guardando 
    nombre =   filename.replace("encrypted_", "decrypted_") #Reemplazando el nombre viejo
    with open (nombre, "wb") as dec:
        dec.write(plaintext)

