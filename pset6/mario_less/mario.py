from cs50 import get_int

# Inicia a variavel n com valor nulo
n = 0

# Solicita do usuario uma entrada numerica positiva não superior a 8
while(n < 1 or n > 8):
    n = get_int("Height: ")

# Imprime os espaços vazios, em seguida os hashes
for i in range(n):
    print(" " * (n-i-1), end="")
    print("#" * (i + 1))