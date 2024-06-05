dist1 = float(input('Digite o valor do primeiro comprimento: '))
dist2 = float(input('Digite o valor do segundo comprimento: '))
dist3 = float(input('Digite o valor do terceiro comprimento: '))

if dist1 != dist2 and dist1 == dist3:
    print('Triangulo isoceles') 
elif dist1 != dist2 and dist2 == dist3:
    print('Triangulo isoceles')
elif dist1 != dist3 and dist1 == dist2:
    print('Triangulo isoceles')
elif dist1 != dist2 != dist3:
    print('Triangulo escaleno')
else: 
    print('Triangulo equilatero') 