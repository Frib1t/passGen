import time
from time import sleep
import signal
import sys
import string
import os
import hashlib
import secrets


def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)


# Ctrl+C
signal.signal(signal.SIGINT, def_handler)


def password():
    letras = string.ascii_letters
    digitos = string.digits
    caracteres = string.punctuation
    abc = letras + digitos + caracteres

    print("Hola, vamos a generar tu clave... ")
    sleep(2)
    os.system("cls")
    while True:
        passwd = input("[1] Si desea generar una clave aleatoria\n"
                       "[2] Si desea hashear su clave\n")

        if passwd == "1":
            pwd = ''
            longitud = int(input("Indique la longitud de su password: "))
            for i in range(longitud):
                pwd += ''.join(secrets.choice(abc))
            os.system("cls")
            print("Esta es su clave, guardela en un lugar seguro: " + pwd)
            input("Pulse una tecla para salir...")
            exit()

        if passwd == "2":
            os.system("cls")
            method()
        else:
            input("Seleccione una opción valida")
            os.system("cls")


def method():
    while True:
        clave = input("Introduzca su clave: ")
        sleep(1)
        os.system("cls")
        conf = input("Su clave es {} [S/N]\n".format(clave))

        if conf == "S" or conf == "s":
            while True:
                print("Escoge como quieres encriptar tu clave: ")
                metodo = input("[1] md5          [3] sha256 \n"
                               "[2] sha1         [4] sha512 \n"
                               ": ")
                if metodo == "1":
                    md5 = hashlib.md5(clave.encode('utf-8')).hexdigest()
                    print("Tu hash md5 es: " + md5)
                    input("Pulse una tecla para salir...")
                    exit()
                if metodo == "2":
                    sha1 = hashlib.sha1(clave.encode('utf-8')).hexdigest()
                    print("Tu hash sha1 es: " + sha1)
                    input("Pulse una tecla para salir...")
                    exit()
                if metodo == "3":
                    sha256 = hashlib.sha256(clave.encode('utf-8')).hexdigest()
                    print("Tu hash sha256 es: " + sha256)
                    input("Pulse una tecla para salir...")
                    exit()
                if metodo == "4":
                    sha512 = hashlib.sha512(clave.encode('utf-8')).hexdigest()
                    print("Tu hash sha512 es: " + sha512)
                    input("Pulse una tecla para salir...")
                    exit()
                else:
                    input("Seleccione una opción valida")
                    os.system("cls")
        if conf == "N" or conf == "n":
            input("Introduzca su clave nuevamente")
            os.system("cls")
        else:
            input("Introduzca su clave nuevamente")
            os.system("cls")


def main():
    print("Licencia Apache\n"
          "Creador: Frib1t\n"
          "Gracias por usar el programa...")
    time.sleep(3)
    os.system("cls")
    password()


if __name__ == '__main__':
    main()
