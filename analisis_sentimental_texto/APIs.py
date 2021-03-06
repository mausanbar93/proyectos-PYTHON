#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unirest,json,requests
from repustate import Client

# Se define clase consultas, que va a contener las peticiones a las APIs
class consultas:

	# Función que hace consultas a la API text_processing, análisis en inglés
	def text_processing(self,data):
		response = unirest.post("http://text-processing.com/api/sentiment/",
			headers={
				"X-Mashape-Key": "DN4Pvj9aQvmshoeibOcMLVzHMb6yp19PYoqjsnTwnkoVOF5jzD",
				"Content-Type": "application/x-www-form-urlencoded",
				"Accept": "application/json"
			},
			params={
				"language": "english",
				"text": data
			}
		)
		resp = response.body['probability']
		minimo = min(resp)
		maximo = max(resp)
		print '/********** API text_processing **********/'
		print 'Respuesta JSON: ',resp
		print 'Porc Min: ',minimo,'',resp[minimo]
		print 'Porc Max: ',maximo,'',resp[maximo]
		if maximo == 'neg':
			respuesta = 'Emocion Negativa'
		elif maximo == 'neutral':
			respuesta = 'Emocion Neutral'
		else:
			respuesta = 'Emocion Positiva'
		print 'Respuesta Analisis: ',respuesta
		print '/********** FIN API text_processing **********/\n'
		#respuesta = json.dumps({maximo:resp[maximo]})

		return respuesta

	# Función que hace consultas a la API sentiment, análisis en inglés
	def sentiment(self,data):
		response = unirest.post("http://sentiment.vivekn.com/api/text/",
			params={
				"language": "auto",
				"txt":data
			}
		)
		resp = response.body['result']
		emocion = resp['sentiment']
		porcentaje = resp['confidence']
		print '/********** API sentiment **********/'
		print resp
		print 'Porc: ',emocion,'',porcentaje
		if emocion == 'Negative':
			respuesta = 'Emocion Negativa'
		elif emocion == 'Neutral':
			respuesta = 'Emocion Neutral'
		else:
			respuesta = 'Emocion Positiva'
		print 'Respuesta Analisis: ',respuesta
		print '/********** FIN API sentiment **********/\n'

		return respuesta

	# Función que hace consultas a la API sentiment140, análisis en español e inglés
	def sentiment140(self,data):
		data = {"data": [{"text":data}]}		
		response = requests.post("http://www.sentiment140.com/api/bulkClassifyJson",
			data=json.dumps(data),
			headers = {
				'Content-type': 'Application/json',
				'Accept': 'application/json'
			}
		)
		resp = response.json()['data'][0]
		polaridad = resp['polarity']
		print '/********** API sentiment140 **********/'
		print resp		
		if polaridad == 0:
			respuesta = 'Emocion Negativa'
		elif polaridad == 2:
			respuesta = 'Emocion Neutral'
		else:
			respuesta = 'Emocion Positiva'			
		print 'Respuesta Analisis: ',respuesta
		print '/********** FIN API sentiment140 **********/\n'

		return respuesta
	
	# Función que hace consultas a la API repustate sentiment, análisis en español e inglés, otros
	def repustate(self,data):
		client = Client(api_key='58007d78a943329b75a778c3a2e55d22e83bf8ec', version='v3')
		response = client.sentiment({'data':data,'lang':'es','emoji':0})
		resp = response['score']
		print '/********** API repustate sentiment **********/'
		print resp		
		if resp < 0:
			respuesta = 'Emocion Negativa'
		elif resp == 0:
			respuesta = 'Emocion Neutral'
		else:
			respuesta = 'Emocion Positiva'			
		print 'Respuesta Analisis: ',respuesta
		print '/********** FIN API repustate sentiment **********/\n'

		return respuesta
		