#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void){
    float valor = 0.0000;
    
    do {
        valor = get_float("Troca devida: ");
    } while (valor < 0.0000);
    
    int centavos = round(valor * 100.00);
    
    int moedas = 0;
    
    while(centavos >= 25){
        centavos-= 25;
        moedas++;
    }    
    
    while(centavos >= 10){
        centavos-= 10;
        moedas++;
    }
    
    while(centavos >= 5){
        centavos-= 5;
        moedas++;
    }
    
    while(centavos >= 1){
        centavos-= 1;
        moedas++;
    }
    
    printf("%i\n", moedas);
}