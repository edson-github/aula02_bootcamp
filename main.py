import math

# calcular a area a partir do raio com 2 casas decimais
raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio ** 2
print(f"A área do círculo é {area:.2f}")

# versao com try except
raio = input("Digite o raio do círculo: ")
try:
    raio = float(raio)
except ValueError:
    print("O valor digitado não é um número válido")
else:
    area = math.pi * raio ** 2
    print(f"A área do círculo é {area:.2f}")

# nome = input("Digite seu nome: ")


# try:
#     nome = str(nome)
# except ValueError:
#     print("O valor digitado não é um nome válido")



# # validr se numero inteiro com isinstance
# numero = input("Digite um número inteiro: ")

# if isinstance(numero, int):
#     print("O valor digitado é um número inteiro")
# else:
#     print("O valor digitado não é um número inteiro")


# 21: Conversor de Temperatura com try-except
numero = float(input("Digite a temperatura em Celsius: "))
try:
    numero = float(numero)
except ValueError:
    print("O valor digitado não é um número válido")
else:
    print((numero * 9/5) + 32)

