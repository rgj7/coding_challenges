#include <stdio.h>
#include <stdlib.h>

int getMaxIndex(int *A, int N) {
	int i, max_idx = 0;
	for(i=1; i<=N; i++)
		if(A[i] > A[max_idx])
			max_idx = i;
	return max_idx;
}

void swap(int *a, int *b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

int main(int argc, char *argv[]) {
	int N, i, *A, max_idx;
	
	fscanf(stdin, "%d\n", &N);
	A = (int*) malloc(N*sizeof(int));
	for(i=0; i<N; i++)
		fscanf(stdin, "%d", A+i);
	
	for(i=N-1; i>0; i--) {
		max_idx = getMaxIndex(A, i);
		swap(A+i, A+max_idx);
		fprintf(stdout, "%d ", max_idx);
	}

	return 0;
}