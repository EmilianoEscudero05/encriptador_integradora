import cv2
import os
import string

def estegano():
    img_nombre = input("Ingrese el nombre de su imagen: ")

    img = cv2.imread(img_nombre) 

    msg = input("Ingresa el mensaje secreto: ")
    password = input("Ingresa una contraseña: ")

    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m = 0
    n = 0
    z = 0

    # Insertar el mensaje en la imagen
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    nombre_archivo = "estegano_" + img_nombre

    # Guardar la imagen con el mensaje oculto
    cv2.imwrite(nombre_archivo, img)
    os.system("start " + nombre_archivo)  # Abrir la imagen en Windows

    message = ""
    n = 0
    m = 0
    z = 0

    # Pedir la contraseña para descifrar
    pas = input("Ingresa la contraseña para descifrar el mensaje: ")
    if password == pas:
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Mensaje:", message)
    else:
        print("No estás autorizado para leer el mensaje")
