import random

print("piedra,papel o tijera, v0.3")

print("1=piedra")
print("1=papel")
print("1=tijera")

tirada = int(input("escoge tu tirada"))

tiradaordenador = random.randint(1,3)

print(tirada)
print(tiradaordenador)

if tiradaordenador==1:
	print("el ordenador ha sacado piedra")
elif tiradaordenador==2;
	print("el ordenador ha sacado papel")
elif tiradaordenador==3;
	print("el ordenador ha sacado tijera")

if tirada == 1 and tiradaordenador == 1;
	print ("empate")
if tirada == 1 and tiradaordenador == 2;
	print ("maquina gana")
if tirada == 1 and tiradaordenador == 3;
	print ("jugador gana")
if tirada == 2 and tiradaordenador == 1;
	print ("jugador gana")
if tirada == 2 and tiradaordenador == 2;
	print ("empate")
if tirada == 2 and tiradaordenador == 3;
	print ("maquina gana")
if tirada == 3 and tiradaordenador == 1;
	print ("maquina gana")
if tirada == 3 and tiradaordenador == 2;
	print ("jugador gana")
if tirada == 3 and tiradaordenador == 3;
	print ("empate")