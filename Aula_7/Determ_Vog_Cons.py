letra = str(input('Digite uma letra: '))
letraL = letra.lower()
if letraL == 'a' or letraL == 'e' or letraL == 'i' or letraL == 'o' or letraL == 'u': 
    print(letra, 'e uma vogal')
else:
    print(letra, 'e uma consoante')