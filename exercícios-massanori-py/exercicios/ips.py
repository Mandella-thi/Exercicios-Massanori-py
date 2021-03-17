import ipaddress
ip='192.168.0.100/24'
#endereco= ipaddress.ip_address(ip)
#print(endereco)
rede= ipaddress.ip_network(ip, strict= False)
print(rede)
