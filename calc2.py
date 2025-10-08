def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

print("-----Calculadora-----")
n1 = float(input("informe o primeiro número: "))
n2 = float(input("informe o segundo número: "))
operador = input("informe a operação (+, -, *, /): ")

if operador == "+":
    resultado = soma(n1, n2)
    print("A soma é: ", resultado)
elif operador == "*":
    resultado = multiplicacao(n1, n2)
    print("A multiplicação é: ", resultado)
elif operador == "/":
    resultado = divisao(n1, n2)
    print("A divisão é: ", resultado)
elif operador == "-":
    resultado = subtracao(n1, n2)
    print("A subtração é: ", resultado)
else:
    print("Operação inválida.")