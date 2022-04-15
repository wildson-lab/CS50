from cs50 import get_float

troco = 0.0

# Solicita o troco ate que uma entrada válida seja inserida
while (troco <= 0.0):
    troco = get_float("Change owned: ")

# Converte o troco em um valor inteiro em centavos
cents = int(troco * 100)
moedas = 0

# Obtem o numero de moedas de cada valor pela divisão inteira entre
# o valor em centavos e o valor de cada moeda, somando ao total de moedas.
# Atualiza o valor com o resto desta divisão.
for moeda in [25, 10, 5, 1]:
    moedas = moedas + cents // moeda
    cents = cents % moeda

print(moedas)