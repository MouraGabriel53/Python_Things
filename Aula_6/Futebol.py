time1 = float(input('Digite o placar do time 1: '))
time2 = float(input('Digite o placar do time 2: '))

if time1 == time2:
    print('O resultado e: empate!')
elif time1 > time2:
     print('O resultado e: vitoria do time 1!')
else:
     print('O resultado e: vitoria do time 2!')