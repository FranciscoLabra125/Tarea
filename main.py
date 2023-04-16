pr = int(input())
se = int(input())
suma = 0
print('Buscando estrellas brillantes...')
for i in range(pr,se+1):
    if i%2 == 0:
        for k in range(1,i-1):
            if i%k==0:
                suma +=k
            else:
                suma+=0
        if suma > 15:
            print('Encontre una estrella brillante!')
            print('Coordenadas: ',f'{suma}',f'{pr}')
    suma = 0