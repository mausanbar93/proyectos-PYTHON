# - *- coding: utf- 8 - *-

#Se importa clase consultas de modulo APIs
from APIs import consultas

if __name__ == '__main__':
	#Instanciamos clase consultas
	metodo = consultas()

	texto = 'love'
	print "Resp1: ",metodo.text_processing(texto)