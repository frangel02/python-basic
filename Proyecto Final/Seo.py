#Auditoria SEO

#imports
import urllib.request as request

print('Auditoria a python.org')
#**************Verificar https***********#
req = request.Request('http://python.org')
resultado = request.urlopen(req)
print(resultado.geturl())

