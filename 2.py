#Contexto do programa
print("A sequência de Fibonacci se inicia com 0 e 1 e os próximos valores  sempre serão a soma dos 2 valores anteriores, como no exemplo a seguir: \n ")

# Define a função para calcular a sequência de Fibonacci até um certo limite
def fibonacci(limite):
    a, b = 0, 1
    while a <= limite:
        print(a, end=' ')
        a, b = b, a + b

# Chama a função para imprimir a sequência até o número 8 para exemplificar
fibonacci(8)

print("\n")

while True:
    try:
        num = int(input("\nDigite um número qualquer que vamos verificar se ele faz parte da sequência de Fibonacci: "))
        # Verifica se o número faz parte da sequência
        a, b = 0, 1
        while b < num:
            a, b = b, a + b
        if b == num:
            print(f"O número {num} faz parte da sequência de Fibonacci.")
        else:
            print(f"O número {num} Não faz parte da sequência de Fibonacci.")
    except KeyboardInterrupt:
        print("\nEncerrando o programa...")
        break