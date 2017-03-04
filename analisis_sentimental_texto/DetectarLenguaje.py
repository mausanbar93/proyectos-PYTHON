#!/usr/bin/env python
# -*- coding: utf-8 -*-

import langid,textblob,collections
from langdetect import detect

# Se define clase detectar, que va a permitir el analisis y detección del lenguaje de un texto
class detectar:

	# Función utiliza la librería langid para el análisis de texto y determinar lenguaje
	def langid_safe(self,data):
		try:
			return langid.classify(data)[0]
		except Exception as e:
			pass

	# Función utiliza la librería langdetect del paquete de librerías de langid para el análisis de texto y determinar lenguaje
	def langdetect_safe(self,data):
		try:
			return detect(data)
		except Exception as e:
			pass

	# Función utiliza la librería textblob para el análisis de texto y determinar lenguaje
	def textblob_safe(self,data):
		try:
			return textblob.TextBlob(data).detect_language()
		except Exception as e:
			pass

	# Función que permite determinar el lenguaje o idioma de una porción de texto, a través del análisis con las librerías langid y textblob
	def detectar_lenguaje(self,data):
		lista_resp=[]
		resp1 = self.langid_safe(data)
		lista_resp.append(resp1)
		resp2 = self.langdetect_safe(data)
		lista_resp.append(resp2)
		resp3 = self.textblob_safe(data)
		lista_resp.append(resp3)
		print '/********** Detectar Lenguaje **********/'
		print 'R1:',resp1,' R2:',resp2,' R3:',resp3
		contar = collections.Counter(lista_resp)
		contar_es = contar['es']
		contar_en = contar['en']
		print 'es: ',contar_es,' en: ',contar_en
		if contar_es > contar_en:
			lenguaje_i = 'Español'
		else:
			lenguaje_i = 'Inglés'

		lenguaje = lenguaje_i.decode('utf-8')
		print 'El texto:',data,'-> es tipo:',lenguaje
		print '/********** FIN Detectar Lenguaje **********/\n'

		return lenguaje