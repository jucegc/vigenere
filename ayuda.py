#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys

def ayudaPrincipal():
	print (" ----------------------------------------------------------------------------")
	print ("| \tALGORITMOS CRIPTOGRAFICOS                                               |")
	print ("| sintaxis: python3 principal.py <algoritmo>					|")
	print ("| <algoritmo>:									|")
	print ("|\t-sva   Algoritmo de sustitución polialfabética Vigenere Autoclave       |")
	print ("| consultar ayuda de un algoritmo en específico: 				|")
	print ("|                                   sintaxis: python3 principal.py <algoritmo>	|")
	print ("|										|")
	print ("| Ayuda con el alfabeto:  			    				|")
	print ("|\tsintaxis: python3 principal.py Alfabeto <tipoAyuda>  	 	        |")
	print ("| <tipoAyuda>:									|")
	print ("|\t-m    Mostrar alfabeto		     				        |")
	print ("|\t-a <simbolo>    agregar	simbolo al alfabeto    			        |")
	print ("|\t-t    Tamaño del alfabeto	  				        |")
	print ("|___________________________________________________________________________|")
	print ("| Adaptado por: Julio Cesar Gomez C. jgomez@umanizales.edu.co                   |")
	print ("| 		 Camilo Gayon ing.camilo.gayon@gmail.com                        |")
	print ("| Creado por: Tania Canizares y Jonathan Ibarra                                 |")
	print ("| Electiva:      Criptografía                         	      ")
	print ("| Docente:       Siler Amador Donado samador@unicauca.edu.co                    |")
	print ("|                      UNIVERSIDAD DEL MANIZALES                                |")
	print (" ----------------------------------------------------------------------------")

def ayudaVigenere():
	print (" -------------------------------------------------------------------------------")
	print ("|                                                                                           |")
	print ("| \tALGORITMO VIGENERE AUTOCLAVE           			                            |")
	print ("|	           								            |")
	print ("| sintaxis: python3 principal.py -sva <modo> <archivoEntrada> <Archivoclave>                |")
	print ("|								   		            |")
	print ("| <modo>:									            |")
	print ("|\t-c    para cifrar el archivo				                            |")
	print ("|\t-d    para descifrar el archivo     						    |")
	print ("| 									                    |")
	print ("| <archivoEntrada>: Nombre del archivo de entrada a cifrar o descifrar ej: quijote.txt	    |")
	print ("|									                    |")
	print ("| <Archivoclave>: El archivo que contiene la clave para cifrar o descifrar el mensaje 	    |")
	print ("|										     	    |")
	print ("| NOTA: El archivo de salida tendra el mismo nombre que el archivo de entrada 	 	    |")
	print ("|	agregando al final la extencion '.cif'(cifrar) o '.dec'(descifrar)  		    |")
	print ("|	ej: quijote.txt.cif o quijote.txt.dec  					            |")
	print ("|										     	    |")
	print ("| Codificación y decodificación (opcional):   	    	 				    |")
	print ("|\tsintaxis: python3 principal.py -sva <modo><archivoEntrada><Archivoclave> -c64 	    |")
	print ("|										            |")
	print ("| Ejemplos:    			  						            |")
	print ("|										            |")
	print ("| Los archivos de prueba los puedes encontrar en:            				    |")
	print ("| http://seguridad.unicauca.edu.co/criptografia/MobyDick.txt            		    |")
	print ("| http://seguridad.unicauca.edu.co/criptografia/quijote.txt            			    |")
	print ("|										            |")
	print ("|\tcifrar: python3 principal.py -sva -c quijote.txt Archivo_Clave.txt          	    |")
	print ("|\tdescifrar: python3 principal.py -sva -d quijote.txt.cif Archivo_Clave.txt           |")
	print ("|										      	    |")
	print (" --------------------------------------------------------------------------------------------")
