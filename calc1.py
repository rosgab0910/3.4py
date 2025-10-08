print("-----Calculadora-----")
n1 = float(input("informe o primeiro número: "))
n2 = float(input("informe o segundo número: "))
operador = input("informe a operação (+, -, *, /): ")

if operador == "+":
    resultado = n1 + n2
    print("A soma é: ", resultado)
elif operador == "*":
    resultado = n1 * n2
    print("A multiplicação é: ", resultado)
elif operador == "/":
    if n2 != 0:
        resultado = n1 / n2
        print("A divisão é: ", resultado)
    else:
        print("Não é possível dividir por zero.")
elif operador == "-":
    resultado = n1 - n2
    print("A subtração é: ", resultado)
else:
    print("Operação inválida.")