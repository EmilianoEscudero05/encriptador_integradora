from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
def encriptar():
    # solicito el núero de bits que tendrá la llave
    try:
        bits = int(input("¿De cuántos bits desea su llave de encriptación? (128, 192, 256): "))
        bits_bytes = {128: 16, 192: 24, 256: 32}
        if bits in bits_bytes:
            print(f"su llave será de {bits_bytes[bits]} bytes")
        else:
            print("Error: Solo se permiten llaves de 128, 192 o 256 bits.")

    except ValueError:
        
        print("Ingrese un valor válido")
        exit()

    #solicito el nombre o ruta del archivo y lo abro
    try:
        nombre = input("Ingrese el nombre o ruta del archivo a encriptar: ")
        with open(nombre, "rb") as f:
            data= f.read()
    except FileNotFoundError:
        print("Archivo no encontrado.")



    # LLave de encriptación Y cifrador.

    key = get_random_bytes(bits_bytes[bits])
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce

    #guardando la llave para futuras desencirptaciones (codigo de chat :,v)


    prefix = "key"
    extension = ".txt"


    num = 1
    while os.path.exists(f"{prefix}{num}{extension}"):
        num += 1


    filename = f"{prefix}{num}{extension}"

    with open(filename, "wb") as k:
        k.write(key)

    #fin del codigo de chat Bv

    #guardo el texto cifrado en una variable y el tag en otra
    cifrado, tag = cipher.encrypt_and_digest(data)

    #guardando las variables en un archivo.
    encriptado_nombre = "encrypted_"+ nombre

    if os.path.isfile(encriptado_nombre):
        print("El archivo ya existe")
    else:
        with open(encriptado_nombre, "wb") as f:
            f.write(tag)
            f.write(nonce)
            f.write(cifrado)





