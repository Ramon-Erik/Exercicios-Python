import urllib.request
from time import sleep

try:
    urllib.request.urlopen('http://pudim.com.br', timeout=5)
except:
    print('\033[31mSite inacessivel\033[m')
else:
    print('\033[32mSite acessivel\033[m')

print('ola mundo')
for c in range(10):
    print('oie')
    sleep(2)