# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

#CONSTANTES 

ANCHO_CADRO = 80
ALTO_CADRO = 80

MARCO = 5
PE = 50

GROSOR_LINHA = 2

COLOR_FONDO = [150,150,150]
COLOR_LINHAS = [80,80,80]

ANCHO_VENTANA = ANCHO_CADRO*3 + MARCO*2
ALTO_VENTANA = ALTO_CADRO*3 + MARCO*2 + PE

#XOGO

lista_casillas = [	[0,0,0],
					[0,0,0],
					[0,0,0]]

ganador = False
casilla_rato = False

pygame.init()
ventana = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
font = pygame.font.SysFont("System", ANCHO_VENTANA/20)

on = True

while on:

	reloj = pygame.time.Clock()
	
	#DEBUXAR
	
	ventana.fill(COLOR_FONDO)
	
	rect_xogo = pygame.Rect(MARCO, MARCO, ANCHO_VENTANA-(MARCO*2), ALTO_VENTANA-(MARCO*2+PE))
	pygame.draw.rect(ventana, [250,250,250], rect_xogo)
						
	for linha in range(len(lista_casillas)):
		for casilla in range(len(lista_casillas[linha])):
			if casilla_rato == [casilla,linha]:
				rect_sel = pygame.Rect(MARCO+ANCHO_CADRO*casilla, MARCO+ALTO_CADRO*linha, 
							ANCHO_CADRO, ALTO_CADRO)
				pygame.draw.rect(ventana, [240,240,240], rect_sel)
			
	for i in range(4):
		pygame.draw.line(ventana, COLOR_LINHAS, [MARCO, MARCO+i*ALTO_CADRO],
						[ANCHO_VENTANA-MARCO, MARCO+i*ALTO_CADRO], GROSOR_LINHA)
		pygame.draw.line(ventana, COLOR_LINHAS, [MARCO+i*ANCHO_CADRO, MARCO],
						[MARCO+i*ANCHO_CADRO, ALTO_VENTANA-(MARCO+PE)], GROSOR_LINHA)
	
	#UPDATE DA PANTALLA
	
	pygame.display.update()
	
	#MOUSE
	
	pos_mouse = pygame.mouse.get_pos()
	if (MARCO < pos_mouse[0] < ANCHO_VENTANA-MARCO
		and MARCO < pos_mouse[1] < ALTO_VENTANA-(MARCO+PE)):
		casilla_rato = [(pos_mouse[0]-MARCO)/ANCHO_CADRO,(pos_mouse[1]-MARCO)/ALTO_CADRO]
	else:
		casilla_rato = False
	
	#EVENTOS
	
	for evento in pygame.event.get():
	
		#EXIT
		
		if evento.type == pygame.QUIT:
			pygame.display.quit()
			on = False
	
	reloj.tick(60)
