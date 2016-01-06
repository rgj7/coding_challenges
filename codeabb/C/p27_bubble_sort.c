// codeabbey, problem 27
// solution by whoisrgj
 
#include <stdio.h>
#include <stdlib.h>

int bubblesort(int *arr, int N) {
    int i, temp;
    int swaps = 0;
    for(i = 0; i < N-1; i++) {
        if(arr[i] > arr[i+1]) {
            temp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = temp;
            swaps++;
        }
    }
    return swaps;
}

int main(int argc, char *argv[]) {
    int N, i, swaps, *arr;
    int total_swaps = 0;
    int total_passes = 0;
    
    fscanf(stdin, "%d", &N); // get array size
    arr = (int*) malloc(sizeof(int)*N);
    for(i = 0; i < N; i++) { // get array values
        fscanf(stdin, "%d", arr+i);
    }
    
    while((swaps = bubblesort(arr, N)) > 0) {
        total_swaps += swaps;
        total_passes++;
    }
    total_passes++;
    
    fprintf(stdout, "%d %d\n", total_passes, total_swaps);

    free(arr);
    
    return 0;
}