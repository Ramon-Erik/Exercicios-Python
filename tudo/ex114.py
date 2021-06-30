import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br', timeout=5)
except:
    print('\033[31mSite inacessivel\033[m')
else:
    print('\033[32mSite acessivel\033[m')
