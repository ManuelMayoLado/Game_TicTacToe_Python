# -*- coding: utf-8 -*-

from os import system,name

def limpar_pantalla():
	system("clear") if name == "posix" else system("cls")
	
def mostrar_titulo():
	limpar_pantalla()
	print("-"*15+"\n"+"|- 3 EN RAIA -|"+"\n"+"-"*15+"\n")

def mostrar_taboleiro(tab):
	print("    0   1   2")
	for fila in range(3):
		print("  |"+("-"*3+"|")*3)
		print(str(fila)+" "+"| "+" | ".join(tab[fila])+" |")
	print("  |"+("-"*3+"|")*3)
	
def comprobar_taboleiro(nxogador,tab):
	simb = "X" if nxogador == 1 else "O"
	for i in range(len(tab)):
		if 		(("".join(tab[i]).replace(" ","") == simb*3)
			or 	("".join([tab[0][i],tab[1][i],tab[2][i]]).replace(" ","") == simb*3)):
			return nxogador
		if (("".join([tab[0][0],tab[1][1],tab[2][2]]).replace(" ","") == simb*3)
			or 	("".join([tab[2][0],tab[1][1],tab[0][2]]).replace(" ","") == simb*3)):
			return nxogador
	return None
	
taboleiro = [
			[".",".","."],
			[".",".","."],
			[".",".","."]
			]
			
xogador = 1

resultado = None

while True:
	
	mostrar_titulo()
	
	mostrar_taboleiro(taboleiro)
	
	if resultado in [1,2]:
		print "\n*** VICTORIA!"+" --- O xogador "+str(resultado)+" vence en esta partida! ***"
		raw_input()
		break
	
	print("\n\n** XOGADOR "+str(xogador)+ (" <X>" if xogador==1 else " <O>")+ " **")
	
	print("\n-- Columna:")
	columna = raw_input(">> ")
	
	print("-- Fila:")
	fila = raw_input(">> ")
	
	if "exit" in [columna,fila]:
		break
	
	try:
		columna = int(columna)
		fila = int(fila)
		
		if 0 <= columna <= 2 and 0 <= fila <= 2 and taboleiro[fila][columna] == ".":
			Correcto = True
		else:
			Correcto = False
	
	except:
		Correcto = False
	
	if Correcto:
		taboleiro[fila][columna] = "X" if xogador == 1 else "O"
		resultado = comprobar_taboleiro(xogador,taboleiro)
		xogador = 2 if xogador == 1 else 1
		
	else:
		print("\nAlgo fixeches mal!")
		raw_input()