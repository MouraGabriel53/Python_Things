def calculadora():
    operacao = str(input("Digite a operação (+, -, *, /): "))
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        resultado = "Operação inválida!"

    print(f"O resultado da operação {operacao} é: {resultado}")

calculadora()