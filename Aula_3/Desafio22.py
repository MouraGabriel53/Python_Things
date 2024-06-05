nome = str(input('Digite seu nome completo:'))

maiusculo = nome.upper()
minusculo = nome.lower()
nomeSpaco = len(nome.replace(' ', ''))
nomeDiv = len(nome.split()[0])

print(maiusculo)
print(minusculo)
print('Seu nome tem:', nomeDiv, 'letras')
print('Seu primeiro nome tem:', nomeSpaco, 'letras')



#ultimonome = nomeDiv[-1] 
#print(ultimonome)