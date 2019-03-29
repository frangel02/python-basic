#Auditoria SEO

#imports
import os
import urllib.request as request

print('Auditoria a python.org')
#**************Verificar https***********#
req = request.Request('http://python.org')
resultado = request.urlopen(req)
print(resultado.geturl())

#*****************************************#
url = "http://python.org"
print("url ", url)
site = request.urlopen(url)
meta = site.info()

print("Content-Length ", site.headers['content-length'])

f = open('out.txt', 'r')
print('File onDisk: ', len(f.read()))
f.close()

f = open('out.txt', 'wb')
f.write(site.read())
site.close()
f.close()

f = open('out.txt', 'r')
print('File on disk after download: ', len(f.read()))
f.close()

print('os.stat().st_size returns:', os.stat('out.txt').st_size)
