'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2
valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que
desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando
se o número informado pertence ou não a sequência.
'''

sequencia = [0, 1]

while sequencia[-1] < 1000:
    sequencia.append(sequencia[-1] + sequencia[-2])

numero = int(input("Digite um Número: "))

if numero in sequencia:
    print(f"O Numero {numero} Pertence á Sequencia de Fibonacci.")

else:
    print(f"O Numero {numero} Não Pertence á Sequencia de Fibonacci.")
    