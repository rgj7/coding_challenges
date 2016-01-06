#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	int testCases, i;
	char buffer[4];
	int kcol, krow, qcol, qrow;
	
	fscanf(stdin, "%d\n", &testCases);
	for(i = 0; i < testCases; i++) {
		fscanf(stdin, "%c%c %c%c\n", &buffer[0], &buffer[1], &buffer[2], &buffer[3]);
		
		kcol = (int) buffer[0]-96;
		krow = (int) buffer[1]-48;
		qcol = (int) buffer[2]-96;
		qrow = (int) buffer[3]-48;
		
		//printf("(%c, %c) (%c, %c)\n", buffer[0], buffer[1], buffer[2], buffer[3]);
		//printf("(%d, %d) (%d, %d)\n", kcol, krow, qcol, qrow);
		
		if(kcol == qcol || krow == qrow || abs(krow-qrow) == abs(kcol-qcol))
			fprintf(stdout, "Y ");
		else
			fprintf(stdout, "N ");
	}
	
	return 0;
}