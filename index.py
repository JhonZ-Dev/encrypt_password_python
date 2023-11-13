import hashlib


def cifrar_contrasenia(contrasenia):
    """Cifra la contraseña con el algoritmo sha256 y la devuelve en formato hexadecimal"""
    
    
    #crear un objeti has de la clase hashlib
    sha256 = hashlib.sha256()
    
    #convertir la contraseña a bytes y actualizar e has
    sha256.update(contrasenia.encode('utf-8'))

    #Obtener el hash resultante en formato hexadecimal
    hash_cifrado=sha256.hexdigest()


#Ejemlo de uso
contrasenia_usuario = "jhonmacias12"
