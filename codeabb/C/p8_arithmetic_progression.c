 // codeabbey, problem 8
 // solution by whoisrgj

#include <stdio.h>

int main(int argc, char *argv[]) {
    int N, i, j, a, b, c, sum;
    
    fscanf(stdin, "%d", &N);
    for(i = 0; i < N; i++) {
        sum = 0;
        fscanf(stdin, "%d %d %d", &a, &b, &c);
        for(j = 0; j < c; j++)
            sum += (a + j*b);
        fprintf(stdout, "%d ", sum);
    }
    return 0;
}