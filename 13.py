from ipaddress import *
ip='193.18.135.201'
for mask in range(30,0,-1):
    net=ip_network(f'{ip}/{mask}',0)
    k=0
    for x in net:
        if bin(int(x))[2:].count('1')==19:k+=1
    if k==105:
        print(32-mask)
        break