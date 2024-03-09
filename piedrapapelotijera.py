import random

print("1=piedra")
print("1=papel")
print("1=tijera")

tirada = input("escoge tu tirada")

tiradaordenador = random.randint(1,3)

print(tirada)
print(tiradaordenador)

if tiradaordenador==1:
	print("el ordenador ha sacado piedra")
elif tiradaordenador==2;
	print("el ordenador ha sacado papel")
elif tiradaordenador==3;
	print("el ordenador ha sacado tijera")