#!/usr/bin/python3
import cgi

prueba = cgi.FieldStorage()
arg = prueba.getvalue('pagina')
print('Content-Type:text/html\r\n')
print('Prueba: '+ arg)
