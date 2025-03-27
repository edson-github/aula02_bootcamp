# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
print(numero1 + numero2)


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero = int(input("Digite um número: "))
print(numero % 5)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
print(numero1 * numero2)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
print(numero1 // numero2)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero = int(input("Digite um número: "))
print(numero ** 2)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
print(numero1 + numero2)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
print((numero1 + numero2) / 2)
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero1 = float(input("Digite o número base: "))
numero2 = float(input("Digite o número expoente: "))
print(numero1 ** numero2)
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
numero = float(input("Digite a temperatura em Celsius: "))
print((numero * 9/5) + 32)
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
numero = float(input("Digite o raio do círculo: "))
print(3.14 * numero ** 2)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
nome = input("Digite seu nome: ")
print(nome.upper())
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Digite seu nome completo: ")
print(nome.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
print(frase.strip())
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ")
print(data.split("/"))

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print(nome + " " + sobrenome)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao1 = input("Digite a primeira expressão booleana: ")
expressao2 = input("Digite a segunda expressão booleana: ")
print(expressao1 and expressao2)
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
expressao1 = input("Digite a primeira expressão booleana: ")
expressao2 = input("Digite a segunda expressão booleana: ")
print(expressao1 or expressao2)
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
expressao = input("Digite uma expressão booleana: ")    
print(not expressao)
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
print(numero1 == numero2)
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
print(numero1 != numero2)

# #### try-except e if

# 21: Conversor de Temperatura com try-except
numero = float(input("Digite a temperatura em Celsius: "))
try:
    numero = float(numero)
except ValueError:
    print("O valor digitado não é um número válido")


# 22: Verificador de Palíndromo
palavra = input("Digite uma palavra: ")
print(palavra == palavra[::-1])
# 23: Calculadora Simples
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
print(numero1 + numero2)
# 24: Classificador de Números
numero = float(input("Digite um número: "))
if numero > 0:
    print("O número é positivo")
else:
    print("O número é negativo")
# 25: Conversão de Tipo com Validação
numero = input("Digite um número: ")
try:
    numero = float(numero)
except ValueError:
    print("O valor digitado não é um número válido")
else:
    print(numero)
