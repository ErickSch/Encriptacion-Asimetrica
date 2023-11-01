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

def descifrar(letras_cifradas):
    for i in range(len(letras_cifradas)):
        letra = chr((letras_cifradas[i]**d) % n)
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
# Probar buscando con un for loop, el menor valor que satisfaga la condicion
e = 2
while (e % 2 == 0 or math.gcd(e, z) != 1):
    e += 1

d = inverso_multiplicativo(e, z)

# Clave pública: (e, n)
# Clave privada: (d, n)


# mi_palabra = "Hola como estas yo bien y tu"

mi_palabra = input("Ingresa una frase o palabra: ")

cifrada = cifrar(mi_palabra)
print(f'palabra cifrada: {cifrada}')

descifrada = descifrar(cifrada)
print(f'palabra descifrada: {descifrada}')

