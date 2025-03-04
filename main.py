import os
try:
    from colorama import Fore as F
    from Crypto.Cipher import AES
    from rich.progress import track as t
except ModuleNotFoundError:
    os.system('pip install -r requirements.txt')
    

import encriptar
import decrypt  
import time
from rich.console import Console

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


opciones = f"""
{F.RED}╭══════════════════════════════════╦ $ ╦══════════════════════════════════╮
    {F.MAGENTA}[01] {F.WHITE}Encriptar               {F.MAGENTA}Creado por: 
    {F.MAGENTA}[02] {F.WHITE}Desencriptar            {F.WHITE}Emiliano Félix, Enrique Ramos, 
                                Emilio Ávalos, Jetró Castro y Armando Ascencio.
    
{F.RED}╰══════════════════════════════════╦ $ ╦══════════════════════════════════╯
"""


while True:
    print(F.GREEN + logo + F.RESET)
    print(opciones + F.RESET)
    try:
        eleccion = int(input("Seleccione una opción: "))
        
        if eleccion == 1:
            encriptar.encriptar()
        elif eleccion == 2:
            decrypt.desencriptar()

        else:
            print("Opción inválida, seleccione un número del 1 al 3.")
        continuar = input("¿Desea realizar otra operación (s/n)").lower()
        if continuar != "s":
            print(Console().print("Saliendo del programa", style="bold yellow"))
            break

    except ValueError:
        print("Ingrese un valor numérico válido.")
    

