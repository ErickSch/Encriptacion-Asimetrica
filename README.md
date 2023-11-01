# Encriptación-Asimétrica

## Integrantes

- Jeannette Arjona
- Erick Schiller
- Alejandro Guzmán
- Mariano Barberi
- Aldo Barraza

## Descripción

- Algoritmo RSA (Rivest, Shamir & Adleman) de cifrado asimétrico para el cifrado y descifrado de texto.

## Requerimientos

- Python instalado.

## Funcionamiento

1. Elegir p y q: dos números aleatorios, ambos deben de ser números primos y distintos.

2. Calcular n: n = p * q.

3. Calcular z: z = (p - 1) * (q - 1).

4. Elegir e: número aleatorio y que el mayor común divisor entre e y z sea el 1.

5. Calcular d: d se calcula obteniendo el inverso multiplicativo de e utilizando el algoritmo de Euclides extendido.

6. Clave pública = (e, n) , clave privada = (d, n). La clave pública puede ser compartida, la clave privada no.

7. Cifrado: C = (M^e)mod n. (C: código cifrado, M: código ASCII de cada caracter).

8. Descifrado: (C^d)mod n = M. (C: código cifrado, M: código ASCII de cada caracter).

## Pruebas

- Prueba 1: Python

![Prueba1](/Prueba1.png)

- Prueba 2: Esto es una prueba

![Prueba1](/Prueba2.png)

### Referencias:

- Calcular clave privada RSA - Google Search. (s. f.). https://www.google.com/search?q=calcular+clave+privada+rsa&sca_esv=578379591&sxsrf=AM9HkKlcwwfax-Ewf8Z8bvU3L3ikapcFmQ%3A1698811272770&ei=iM1BZeDULvrSkPIPj7-E4AQ&oq=calcular+clave+priva&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIhRjYWxjdWxhciBjbGF2ZSBwcml2YSoCCAAyBhAAGBYYHkjEMVAAWJkkcAJ4AZABAJgBmAGgAaEUqgEEMS4yMbgBA8gBAPgBAagCFMICBBAjGCfCAgcQIxiKBRgnwgIHEAAYigUYQ8ICCxAuGIAEGLEDGIMBwgINEAAYigUYsQMYgwEYQ8ICCBAAGIAEGLEDwgIREC4YgAQYsQMYgwEYxwEY0QPCAgsQABiABBixAxiDAcICBxAjGOoCGCfCAhYQABgDGI8BGOUCGOoCGLQCGIwD2AEBwgIKEAAYigUYsQMYQ8ICDBAjGIoFGBMYgAQYJ8ICDhAAGIAEGLEDGIMBGIsDwgIOEAAYigUYsQMYgwEYiwPCAgsQABiKBRixAxiDAcICBxAuGIoFGEPCAgoQABiKBRhDGIsDwgIFEAAYgATCAggQABgWGB4YD-IDBBgAIEGIBgG6BgYIARABGAs&sclient=gws-wiz-serp#fpstate=ive&vld=cid:74b9ea95,vid:Kvd70s64MIU,st:0
- Córdoba, D. (2023, 14 febrero). RSA: ¿Cómo funciona este algoritmo de cifrado? Junco TIC. https://juncotic.com/rsa-como-funciona-este-algoritmo/
- pdf: https://cs.uns.edu.ar/~ldm/data/ss/info/ejemplo-rsa.pdf
