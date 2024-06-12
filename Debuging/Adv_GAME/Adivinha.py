import random

numero_secreto = random.randint(20, 50)
tentativas = 0
max_tentativas = 5

while tentativas < max_tentativas:
    chute = int(input("Digite um número: "))
    tentativas += 1

    if chute == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break
    elif chute > numero_secreto:
        print("O número secreto é menor que o seu chute.")
    else:
        print("O número secreto é maior que o seu chute.")

if chute != numero_secreto:
    print(f"Você não conseguiu adivinhar o número secreto. Era {numero_secreto}.")