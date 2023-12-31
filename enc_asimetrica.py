# Algoritmo RSA (Rivest, Shamir & Adleman)

import random
import math

def es_primo(numero):
    if numero == 1:
        return False
    elif numero % 2 == 0:
        return False
    elif numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                return False
    return True

def cifrar(palabra):
    letras_palabra = []
    for i in palabra:
        letras_palabra.append(i)

    for k in range(len(letras_palabra)):
        letra_ascii = ord(letras_palabra[k])
        c = (letra_ascii**e) % n
        letras_palabra[k] = c
    
    return letras_palabra

def descifrar(letras_cifradas, d2, n2):
    for i in range(len(letras_cifradas)):
        letra = chr((letras_cifradas[i]**d2) % n2)
        letras_cifradas[i] = letra
    
    palabra = ""
    for k in letras_cifradas:
        palabra += k
    
    return palabra

def gcd_extendido(e, z):
    if e == 0:
        return (z, 0, 1)
    else:
        gcd, x, y = gcd_extendido(z % e, e)
        return (gcd, y - (z // e) * x, x)

def inverso_multiplicativo(e, z):
    gcd, x, y = gcd_extendido(e, z)
    return x % z

# p & q: numeros primos y p != q
p = q = 1

while (not es_primo(p)):
    p = random.randint(1, 100)

while (not es_primo(q) or q == p):
    q = random.randint(1, 100)

n = p * q
z = (p - 1) * (q - 1)

# e: impar, sin multiplos comunes con z, 1 < e < z, MCD(z ,e) = 1
e = 2
while (e % 2 == 0 or math.gcd(e, z) != 1):
    e += 1

d = inverso_multiplicativo(e, z)

# Clave pública: (e, n)
# Clave privada: (d, n)


opcion = -1
cifrada = []
descifrada = ""

while (opcion != "3"):
    print("""
-----------------------
    1. Cifrar
    2. Descifrar
    3. Salir
    """)
    opcion = input("Ingrese una opción: ")
    print("-----------------------")

    # C = código cifrado
    # M = código ASCII de cada letra
    if (opcion == "1"):
        mi_palabra = input("Ingresa una frase o palabra: ")
        # C = (M^e)mod n
        cifrada = cifrar(mi_palabra)
        print(f'Palabra o frase cifrada: {cifrada}')
        print(f'Clave pública: ({e}, {n})')
        print(f'Clave privada: ({d}, {n})')
    
    elif (opcion == "2"):
        if (len(cifrada) == 0):
            print("La palabra no ha sido cifrada")
        else:
            # Darle formato al input de la palabra cifrada
            mi_palabra_cifrada = input("Ingresa la palabra cifrada ([#, #...]): ")
            mi_palabra_cifrada = mi_palabra_cifrada.replace('[', '')
            mi_palabra_cifrada = mi_palabra_cifrada.replace(']', '')
            mi_palabra_cifrada = mi_palabra_cifrada.split(', ')
            mi_palabra_cifrada = mi_palabra_cifrada = (int(val) for val in mi_palabra_cifrada)
            mi_palabra_cifrada = list(mi_palabra_cifrada)

            # Darle formato al input de la clave privada
            clave_p = input("Ingresa clave privada (d, n): ")
            clave_p = clave_p.replace('(', '')
            clave_p = clave_p.replace(')', '')
            clave_p = clave_p.split(", ")
            clave_p = (int(num) for num in clave_p)
            clave_p = list(clave_p)

            d2 = clave_p[0]
            n2 = clave_p[1]

            # (C^d)mod n = M
            descifrada = descifrar(mi_palabra_cifrada, d2, n2)
            print(f'Palabra o frase descifrada: {descifrada}')




