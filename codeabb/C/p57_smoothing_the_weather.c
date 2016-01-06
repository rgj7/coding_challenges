// codeabbey, problem 57
// solution by whoisrgj

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int N, i;
    double result, *data;
    
    fscanf(stdin, "%d", &N); // N of values
    
    data = (double *) malloc(N*sizeof(double));
    for(i=0;i<N;i++) {
        fscanf(stdin, "%lf", data+i);
    }
    
    for(i=0;i<N;i++) {
        if(i==0 || i==N-1)
            result = data[i];
        else
            result = (double) (data[i-1] + data[i] + data[i+1]) / 3;
        fprintf(stdout, "%.8lf ", result);
    }
    fprintf(stdout, "\n");
    
    free(data);
    return 0;
}