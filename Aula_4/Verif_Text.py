text = str(input('Digite algo: '))
verifVazio = len(text)

if not verifVazio == 0:
    print('Texto não vazio')
else:
    print('Texto vazio')