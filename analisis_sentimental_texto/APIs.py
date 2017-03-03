# - *- coding: utf- 8 - *-
import unirest,json

#Definimos clase consultas, que va a contener las peticiones a las APIs
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

		return respuesta;