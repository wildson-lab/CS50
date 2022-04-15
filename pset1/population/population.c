#include <stdio.h>
#include <cs50.h>

int main(void){
    int start = 0, end = 0, pop = 0, anos = 0;
    
    do {
        start = get_int("Start size: ");
    } while (start < 9);
    
    do {
        end = get_int("End size: ");
    } while (end < start);
    
    pop = start;
    
    while (pop < end){
        pop += ((pop/3) - (pop/4));
        anos++;
    }
    
    printf("Years: %i\n", anos);
}