# - *- coding: utf- 8 - *-
import unirest,json

#Definimos clase consultas, que va a contener las peticiones a las APIs
class consultas:
	# Función que hace consultas a la API text-processing, análisis en inglés
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
		print 'Respuesta: ',resp
		print 'Porc Min: ',minimo,'',resp[minimo]
		print 'Porc Max: ',maximo,'',resp[maximo]
		if maximo == 'neg':
			respuesta = 'Emocion Negativa'
		elif maximo == 'neutral':
			respuesta = 'Emocion Neutral'
		else:
			respuesta = 'Emocion Positiva'
		#respuesta = json.dumps({maximo:resp[maximo]})

		return respuesta
