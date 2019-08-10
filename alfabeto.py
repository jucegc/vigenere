#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import archivo

"""Alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x'
,'y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X'
,'Y','Z','0','1','2','3','4','5','6','7','8','9','.',',',' ','\n','_','ü','Ü',':','«','Ï',']','À','Ù']"""
Alfabeto=[]
al=['Ñ']
nomAlfabeto='Alfabeto.txt'

def cargarAlf():
	A=archivo.abrirArchivo(nomAlfabeto)
	if A=='':
		print ('No se encontro el archivo '+nomAlfabeto)
	for letra in A.readlines():
		if(letra[0]!="\xc3" and letra[0]!="\xc2" and letra[0]+letra[1]!="\\n"):
			Alfabeto.append(letra[0])
		elif(letra[0]+letra[1]=="\\n"):
			Alfabeto.append('\n')		
		else:			
			Alfabeto.append(letra[0]+letra[1])
		#Alfabeto.append(letra)
	A.close()

def agregarSimbolo(simbolo):	
	#print '\xc3'
	simb=simbolo+"\n"
	fichero = archivo.escribirAlfabeto(nomAlfabeto,simb)
	if fichero=='':
		print ('Ocurrio un error al intentar escribir en ', n)
	else:
		fichero.close()
	Alfabeto.append(simbolo)
	print ("Se agrego el simbolo ",simbolo," al alfabeto"	)
	#imprimir()

def existe(simbolo):
	if(simbolo in Alfabeto):
		print ("El simbolo que desea agregar ya existe dentro del alfabeto")
		return True
	else:
		print ("El simbolo no se encuentra en el alfabeto")
		return False

def imprimir():
	i=0
	while(i<len(Alfabeto)):
		j=0
		alf=""
		print ('----------------------------------------------------------------------------')
		while(j<20):
			if(Alfabeto[i]=="\n"):
				alf=alf+'|\\n|'	
			else:
				alf=alf+'|'+Alfabeto[i]+'|'
			i=i+1
			if(i==len(Alfabeto)):
				j=20
			j=j+1
		print (alf)

def getAlfabeto():
	return Alfabeto
	
def tamAlfabeto():
	return len(Alfabeto)

def getPosicion(letra):
	try:
		return Alfabeto.index(letra)
	except:
		return -1
	
cargarAlf()
#agregarSimbolo('ñ')
#print (Alfabeto.index('Ñ'))
#imprimir()



#print (chr(91))

#print (map(chr,range(65,91)))



