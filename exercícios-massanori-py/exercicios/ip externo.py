import re, json
from urllib.request import urlopen

url='https://ipinfo.io/json'

resposta= urlopen(url)
dados=json.load(resposta)

ip=dados['ip']
org=dados['org']
cid=dados['city']
pais=dados['country']
regiao=dados['region']
print('Detalhes do Ip externo\n')
print('IP: {4}\n Região {1}\nPais:{2}\nCidade: {3}\n Org.: {0}'.format(org,regiao,pais,cid,ip))