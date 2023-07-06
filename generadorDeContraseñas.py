import random

characters="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length=int(input("Introduzca la longitud de la contraseña: "))

password=""

for i in range(length):
    password+=random.choice(characters)

print("La contraseña es: ", password)
