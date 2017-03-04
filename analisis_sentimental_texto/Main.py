#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Se importa clase consultas de módulo APIs
from APIs import consultas

# Se importa clase detectar de módulo DetectarLenguaje 
from DetectarLenguaje import detectar

# Función de arranque de código, inicia script principal (Main.py)
if __name__ == '__main__':
	#Instanciamos clase consultas
	metodo = consultas()
	#Instanciamos clase detectar
	obtener = detectar()

	texto_i = 'If i was the sea and your a rock, would raise the tide, to kiss your mouth'
	#texto_i = 'Si yo fuese el mar, y tu una roca, haría subir la marea, para besar tu boca'
	#texto_i = 'La casa es más bonita'
	texto = texto_i.decode('utf-8')
	print '/********** TEXTO ANALIZAR **********/'
	print texto
	print '/********** FIN TEXTO ANALIZAR **********/\n'
	
	metodo.text_processing(texto)
	metodo.sentiment(texto)
	metodo.sentiment140(texto)
	metodo.repustate(texto)

	obtener.detectar_lenguaje(texto)