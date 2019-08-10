#!/usr/bin/python
# -*- coding: utf8 -*-
import ayuda
import vigenere
import archivo
from time import time


def validacionVigenere(argumentos):
	if(len(argumentos)==6):
		if(argumentos[5]=="-c64"):    #activo la opcion c64
			if(argumentos[2]=="-c"):         #si va a cifrar
				start_time = time()      #toma el tiempo
                                #                      archi_plano   archi clave
				vigenere.cifraVigenere(argumentos[3],argumentos[4],argumentos[3]+".cif", "-c64")
				elapsed_time = time() - start_time
				print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
			elif(argumentos[2]=="-d"):    #si va a descifrar
				sal=argumentos[3].replace("cif","dec")
				start_time = time()
                                #                      archi_cifrado archi clave
				vigenere.descVigenere(argumentos[3],argumentos[4],sal,"-c64")
				elapsed_time = time() - start_time
				print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
			else: 
				print ("\nEl modo ",argumentos[2]," es incorrecto")
				print ("Revisar la ayuda del algoritmo de vigenere: python3 principal.py -sva\n")
		else:
			print("Si deseas codificar o decodificar usa la bandera -c64 en lugar de ",argumentos[5])
	else:
		if(len(argumentos)!=5):	
			print ("\nEl número de parámetros es incorrecto")
			print ("Revisar la ayuda del algoritmo de vigenere: python3 principal.py -sva\n")
		else:
			if(argumentos[2]=="-c"):
				start_time = time()
				vigenere.cifraVigenere(argumentos[3],argumentos[4],argumentos[3]+".cif", "")
				elapsed_time = time() - start_time
				print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
			elif(argumentos[2]=="-d"):
				sal=argumentos[3].replace("cif","dec")
				start_time = time()
				vigenere.descVigenere(argumentos[3],argumentos[4],sal,"")
				elapsed_time = time() - start_time
				print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
			else: 
				print ("\nEl modo ",argumentos[2]," es incorrecto")
				print ("Revisar la ayuda del algoritmo de vigenere: python3 principal.py -sva\n")
