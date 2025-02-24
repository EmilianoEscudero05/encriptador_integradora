from colorama import Fore as F
import encriptar, decrypt






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
print(opciones+F.RESET)

eleccion = int(input("seleccione una opción: "))

try:
    if eleccion == 1:
        encriptar.encriptar()
    elif eleccion == 2:
        decrypt.desencriptar()

except ValueError:
    print("Ingrese un valor valido")
    
    





