// codeabbey, problem 8
// solution by whoisrgj

#include <stdio.h>

char *suits[] = {"Clubs", "Spades", "Diamonds", "Hearts"};
char *ranks[] = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};

int main(int argc, char *argv[]) {
    int N, i, val, s_val, r_val;
    
    fscanf(stdin, "%d", &N);
    for(i = 0; i < N; i++) {
        fscanf(stdin, "%d", &val);
        s_val = val / 13;
        r_val = val % 13;
        fprintf(stdout, "%s-of-%s ", ranks[r_val], suits[s_val]);
    }
    return 0;
}