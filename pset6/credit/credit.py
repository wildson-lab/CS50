from cs50 import get_string

# Função principal do programa
def main():
    numero_cc = ""

    # Solicita a entrada até que uma entrada numérica seja inserida
    while True:
        numero_cc = get_string("Number: ")
        if(somente_numeros(numero_cc)):
            break

    # Verifica se o tamanho está correto, se a entrada é válida pelo
    # Algoritmo de Luhn e se os numeros correspondem a uma bandeira.
    # Caso alguma condição não seja atendida, o número é inválido.
    if not (tamanho_correto(numero_cc) and luhn_valido(numero_cc) and bandeira_valida(numero_cc)):
        print("INVALID")


# Verifica se uma string é composta apenas por números e retorna True, caso positivo
def somente_numeros(str_cc):
    for char in str_cc:
        if not char.isdigit():
            return False

    return True


# Verifica se o tamanho de uma string é compatível com um cartão de crédito
def tamanho_correto(str_cc):
    tamanho_num = len(str_cc)

    if not tamanho_num in [13, 15, 16]:
        return False

    return True


# Verifica se o número do cartão é valido através do Algoritmo de Luhn
def luhn_valido(str_cc):
    soma = 0
    tamanho_num = len(str_cc)

    # Obtém o produto e a soma dos dígitos de 2 em 2, partindo do penúltimo
    for i in range(tamanho_num-2, -1, -2):
        digito = int(str_cc[i])
        produto = digito * 2
        soma += produto // 10
        soma += produto % 10

    # Soma os demais dígitos ao acumulador
    for i in range (tamanho_num - 1, -1, -2):
        digito = int(str_cc[i])
        soma += digito

    # Verifica se o último dígito da soma é zero
    if(soma % 10 == 0):
        return True
    else:
        return False


def bandeira_valida(cc_num):
    # Obtém os dois primeiros números do cartão
    inicio_num = int(cc_num[0:2])

    # Imprime a bandeira correspondente
    # Ou retorna False se nenhuma corresponder
    if inicio_num in [34, 37]:
        print("AMEX")
    elif  inicio_num in range(50, 56, 1):
        print("MASTERCARD")
    elif  inicio_num in range(39, 50, 1):
        print("VISA")
    else:
        return False

    # Se chegar até aqui, houve uma bandeira correspondente.
    return True

main()
