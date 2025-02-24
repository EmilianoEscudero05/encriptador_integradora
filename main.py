import os
try:
    from colorama import Fore as F
    from Crypto.Cipher import AES
except ModuleNotFoundError:
    os.system('pip install requirements.txt')
    from colorama import Fore as F

import encriptar
import decrypt  

logo = f""" 
.----------------.  .----------------.  .----------------.  .----------------.  .----------------.   
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  
| | _____  _____ | || |  _________   | || |  _________   | || |      __      | || |   ______     | |  
| ||_   _||_   _|| || | |  _   _  |  | || | |  _   _  |  | || |     /  \     | || |  |_   _ \    | |  
| |  | |    | |  | || | |_/ | | \_|  | || | |_/ | | \_|  | || |    / /\ \    | || |    | |_) |   | |  
| |  | '    ' |  | || |     | |      | || |     | |      | || |   / ____ \   | || |    |  __'.   | |  
| |   \ `--' /   | || |    _| |_     | || |    _| |_     | || | _/ /    \ \_ | || |   _| |__) |  | |  
| |    `.__.'    | || |   |_____|    | || |   |_____|    | || ||____|  |____|| || |  |_______/   | |  
| |              | || |              | || |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  
'----------------'  '----------------'  '----------------'  '----------------'  '----------------'   
"""
print(F.GREEN + logo + F.RESET)

opciones = f"""
{F.RED}╭══════════════════════════════════╦ $ ╦══════════════════════════════════╮
    {F.MAGENTA}[01] {F.WHITE}Encriptar               {F.MAGENTA}Creado por: 
    {F.MAGENTA}[02] {F.WHITE}Desencriptar            {F.WHITE}Emiliano Félix, Enrique Ramos, 
                                Emilio Ávalos, Jetró Castro y Armando Ascencio.
    {F.MAGENTA}[03] {F.WHITE}Ingresar llave propia  
{F.RED}╰══════════════════════════════════╦ $ ╦══════════════════════════════════╯
"""
print(opciones + F.RESET)

try:
    eleccion = int(input("Seleccione una opción: "))
    
    if eleccion == 1:
        encriptar.encriptar()
    elif eleccion == 2:
        decrypt.desencriptar()

    else:
        print("Opción inválida, seleccione un número del 1 al 3.")
except ValueError:
    print("Ingrese un valor numérico válido.")
