#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Se importa clase consultas de modulo APIs
from APIs import consultas

if __name__ == '__main__':
	#Instanciamos clase consultas
	metodo = consultas()

	#texto = 'If i was the sea and your a rock, would raise the tide, to kiss your mouth'
	texto = 'Si yo fuese el mar, y tu una roca, haría subir la marea, para besar tu boca'
	print '/********** TEXTO ANALIZAR **********/'
	print texto
	print '/********** FIN TEXTO ANALIZAR **********/\n'
	
	metodo.text_processing(texto)
	metodo.sentiment(texto)
	metodo.sentiment140(texto)