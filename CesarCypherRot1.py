def descifrar_cesar_rot1(texto_cifrado):
    texto_descifrado = ""

    for caracter in texto_cifrado:
        if caracter.isalpha():
            ascii_valor = ord(caracter)
            nuevo_ascii_valor = ascii_valor - 1
            if caracter.islower():
                if nuevo_ascii_valor < ord('a'):
                    nuevo_ascii_valor += 26
            elif caracter.isupper():
                if nuevo_ascii_valor < ord('A'):
                    nuevo_ascii_valor += 26
            texto_descifrado += chr(nuevo_ascii_valor)
        else:
            texto_descifrado += caracter

    return texto_descifrado


texto_cifrado = input("Introduce el texto cifrado: ")
texto_descifrado = descifrar_cesar_rot1(texto_cifrado)
print("Texto descifrado:", texto_descifrado)
