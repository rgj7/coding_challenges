#include <stdio.h>
#include <string.h>

#define PAIR 0
#define TWO_PAIR 1
#define THREE 2
#define FOUR 3
#define YACHT 4
#define FULL_HOUSE 5
#define SMALL_STRAIGHT 6
#define BIG_STRAIGHT 7
#define NONE 8

const char *outcomes[] = {"pair", "two-pairs", "three", "four", "yacht", 
		"full-house", "small-straight", "big-straight", "none"};

int main(int argc, char *argv[]) {
	int testCases, i, j, dieValue, dieCount[6], outcomeIndex, pairs, triples;
	
	fscanf(stdin, "%d\n", &testCases);
	for(i = 0; i < testCases; i++) {
		memset(dieCount, 0, sizeof(dieCount));
		
		for(j = 0; j < 5; j++) {
			fscanf(stdin, "%d", &dieValue);
			dieCount[dieValue-1]++;
		}
		
		outcomeIndex = -1;
		pairs = 0;
		triples = 0;
		for(j = 0; j < 6; j++) {
			if(dieCount[j] == 0 || dieCount[j] == 1)
				continue;
			else if(dieCount[j] == 2)
				pairs++;
			else if(dieCount[j] == 3)
				triples++;
			else if(dieCount[j] == 4) {
				outcomeIndex = FOUR;
				break;
			} else if(dieCount[j] == 5) {
				outcomeIndex = YACHT;
				break;
			}
		}
		
		if(outcomeIndex < 0) {
			if(triples == 1) {
				if(pairs == 1)
					outcomeIndex = FULL_HOUSE;
				else
					outcomeIndex = THREE;
			} else if(pairs == 2) {
				outcomeIndex = TWO_PAIR;
			} else if(pairs == 1) {
				outcomeIndex = PAIR;
			} else {
				if(dieCount[0] == 0) {
					outcomeIndex = BIG_STRAIGHT;
				} else if(dieCount[5] == 0) {
					outcomeIndex = SMALL_STRAIGHT;
				} else {
					outcomeIndex = NONE;
				}
			}
		}
		
		fprintf(stdout, "%s ", outcomes[outcomeIndex]);
	}
	
	return 0;
}