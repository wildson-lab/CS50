#include <stdio.h>
#include <cs50.h>

int main(void){
    int tamanho = 0;
    
    // Pergunta o tamanho até que o valor esteja entre 1 e 8
    while (tamanho < 1 || tamanho > 8){
        tamanho = get_int("Altura: ");
    }
    
    // Loops alinhados
    // Imprime ' ' caso o numero da linha seja menor que a diferença
    // entre o tamanho total e o numero da coluna (para alinhar à direita)
    // Imprime '#' caso contrario
    for (int i=0; i < tamanho; i++){
        for (int j = 0; j < tamanho; j++){
            if (i + 1 < tamanho - j){
                printf(" ");
            }
            else{
                printf("#");
            }
        }
        
        printf("  ");
        
        for (int j = 0; j < tamanho; j++){
            if (j <= i){
                printf("#");
            }
        }
        
        printf("\n");
    }
}