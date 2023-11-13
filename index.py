import hashlib


def cifrar_contrasenia(contrasenia):
    """Cifra la contraseña con el algoritmo sha256 y la devuelve en formato hexadecimal"""
    
    
    #crear un objeti has de la clase hashlib
    sha256 = hashlib.sha256()
    
    
