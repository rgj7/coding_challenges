// codeabbey, problem 33
// solution by whoisrgj

#include <stdio.h>


int main(int arc, char *argv[]) {
	int bits, num;
	
	while(fscanf(stdin, "%d", &num) == 1) {
		bits = __builtin_popcount(num);
		num = num & 127;
		if(bits % 2 == 0)
		    fprintf(stdout, "%c", (char) num);
	}
	
	return 0;
}