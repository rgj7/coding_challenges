// codeabbey, problem 9
// solution by whoisrgj

#include <stdio.h>

int main(int argc, char *argv[]) {
    int N, i, a, b, c, is_tri;
    
    fscanf(stdin, "%d", &N);
    for(i = 0; i < N; i++) {
        is_tri = 0;
        fscanf(stdin, "%d %d %d", &a, &b, &c);
        if(((a+b) >= c) && ((a+c) >= b) && ((b+c) >= a))
            is_tri = 1;
        fprintf(stdout, "%d ", is_tri);
    }
    return 0;
}