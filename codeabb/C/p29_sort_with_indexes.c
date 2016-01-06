// codeabbey, problem 29
// solution by whoisrgj

#include <stdio.h>
#include <stdlib.h>

typedef struct number number_t;
struct number {
    int value;
    int index;
};

int bubblesort(number_t *arr, int N) {
    int i, swaps = 0;
    number_t temp;
    
    for(i = 0; i < N-1; i++) {
        if((arr+i)->value > (arr+i+1)->value) {
            temp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = temp;
            swaps++;
        }
    }
    return swaps;
}

int main(int argc, char *argv[]) {
    int N, i;
    number_t *arr;
    
    fscanf(stdin, "%d", &N); // get array size
    arr = (number_t*) malloc(sizeof(number_t)*N);
    for(i = 0; i < N; i++) { // get array values
        fscanf(stdin, "%d", &(arr+i)->value);
        (arr+i)->index = i+1;
    }
    
    while(bubblesort(arr, N) > 0);
    
    for(i = 0; i < N; i++) {
        fprintf(stdout, "%d ", (arr+i)->index);
    }
    fprintf(stdout, "\n");

    free(arr);
    
    return 0;
}