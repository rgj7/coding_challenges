// codeabbey, problem 10
// solution by whoisrgj

#include <stdio.h>

int main(int argc, char *argv[]) {
    int i, N, x1, y1, x2, y2, a, b;

    fscanf(stdin, "%d", &N); // get number of test cases
    for(i = 0; i < N; i++) {
        fscanf(stdin, "%d %d %d %d", &x1, &y1, &x2, &y2); // get values
        
        a = (y2-y1) / (x2-x1);
        b = y1 - (a*x1);
        
        fprintf(stdout, "(%d %d) ", a, b);
    }
    fprintf(stdout, "\n");

    return 0;
}