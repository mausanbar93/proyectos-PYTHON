# - *- coding: utf- 8 - *-

#Se importa clase consultas de modulo APIs
from APIs import consultas

if __name__ == '__main__':
	#Instanciamos clase consultas
	metodo = consultas()

	texto = 'Fast and accurate sentiment classification using an enhanced Naive Bayes model'
	print '/********** TEXTO ANALIZAR **********/'
	print texto
	print '/********** FIN TEXTO ANALIZAR **********/\n'
	
	metodo.text_processing(texto)
	metodo.sentiment(texto)