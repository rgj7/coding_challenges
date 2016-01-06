 // codeabbey, problem 81
 // solution by whoisrgj
 
#include <stdio.h>

#define BITS 32

int main(int argc, char *argv[]) {
    int i, j, N, bit, count;
    long value;

    fscanf(stdin, "%d", &N); // get number of test values
    for(i = 0; i < N; i++) {
        fscanf(stdin, "%ld", &value); // get value
        
        count = 0;
        for(j = BITS-1; j >= 0; j--) {
            bit = value >> j;
            if(bit & 1) {
                count++;
            }
        }
        
        fprintf(stdout, "%d ", count);
    }
    fprintf(stdout, "\n");

    return 0;
}