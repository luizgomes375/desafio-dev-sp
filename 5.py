string = input("Digite uma string: ")
inverted_string = ""

for i in range(len(string)-1, -1, -1):
    inverted_string += string[i]

print("A string invertida é:", inverted_string)