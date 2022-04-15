from cs50 import get_string


# Funcao principal
def main():
    # Recebe um texto do usuario e calcula seu indice
    texto = get_string("Texto: ")
    indice_cl = calcula_indice_cl(texto)
    
    # Mostra o indice correspondente
    if indice_cl < 1:
        print("Before Grade 1")
    elif indice_cl > 16:
        print("Grade 16+")
    else:
        print(f"Grade {indice_cl}")
        
        
# Retorna um inteiro correspondente ao indice de Coleman-Liau de um texto    
def calcula_indice_cl(texto):
    letras = 0
    palavras = 1
    sentencas = 0
    
    # Calcula a quantidade de letras, palavras e sentencas no texto
    for char in texto:
        if(char.isalpha()):
            letras += 1
        elif char in [".", "!", "?"]:
            sentencas += 1
        elif (char == ' '):
            palavras += 1
    
    # Calcula a media de letras  e de sentencas por 100 palavras    
    media_l = 100.0 * (letras/palavras) 
    media_s = 100.0 * (sentencas/palavras)
    
    # Calcula o Indice de Coleman-Liau
    indice = round(0.0588 * media_l - 0.296 * media_s - 15.8)
    
    return indice
    
    
main()