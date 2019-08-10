import base64

def escribirArchivo(nombreArchivo, texto):
	try:
		archivo = open(nombreArchivo,"w",encoding="ISO-8859-1")
	except IOError:
		return ''
	else:
		archivo.write(texto)
		return archivo

def escribirArchivo64(nombreArchivo, texto):
	try:
		archDecode=base64.b64decode(texto)
		archivo = open(nombreArchivo,"w",encoding="ISO-8859-1")
	except ValueError:
		return -1
	except IOError:
		return ''
	else:
		archivo.write(archDecode.decode("ISO-8859-1"))
		return archivo

def escribirAlfabeto(nombreArchivo, texto):
	try:
		archivo = open(nombreArchivo,"a",encoding="ISO-8859-1")
	except IOError:
		return ''
	else:
		archivo.write(texto)
		return archivo
	
def abrirArchivo(nombreArchivo):
	try:
		archivo = open(nombreArchivo,'r',encoding="ISO-8859-1")
	except IOError:
		return ''
	else:
		return archivo

def abrirArchivo64(nombreArchivo):
	try:
		archivo = open(nombreArchivo,'rb')
		arch_read=archivo.read();
		arch64=base64.encodestring(arch_read)
	except IOError:
		return ''
	else:
		return arch64
		
def obtenerNombreArchivo():
	nombreArchivo = ''
	nombreArchivo = raw_input("(ejm: nombreArchivo.txt): ")
	return nombreArchivo
