# Pega uma string de entrada do usuário
string = input("Digite uma string: ")
#Seta variável inverted_string como vazio
inverted_string = ""
#Cria um laço que percorre toda a sting que o usuário inputou de trás pra frente e inverte os campos
for i in range(len(string)-1, -1, -1):
    inverted_string += string[i]
#imprime a string invertida
print("A string invertida é:", inverted_string)