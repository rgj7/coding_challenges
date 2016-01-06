// codeabbey, problem 12
// solution by whoisrgj

#include <stdio.h>

#define SECMIN 60
#define SECHOUR 3600
#define SECDAY 86400

struct timedata {
    int day;
    int hour;
    int min;
    int sec;
};

int convertToSec(struct timedata data) {
    int sum;
    sum = data.sec;
    sum += data.min*SECMIN;
    sum += data.hour*SECHOUR;
    sum += data.day*SECDAY;
    return sum;
}

void printTimeDiff(struct timedata start, struct timedata end) {
    int timediff, day, hour, min, sec;
    timediff = convertToSec(end) - convertToSec(start);
    day = timediff/SECDAY;
    timediff %= SECDAY;
    hour = timediff/SECHOUR;
    timediff %= SECHOUR;
    min = timediff/SECMIN;
    timediff %= SECMIN;
    sec = timediff;
    fprintf(stdout, "(%d %d %d %d) ", day, hour, min, sec);
}

int main(int argc, char *argv[]) {
    int N, i, j;
    struct timedata data[2];
    
    fscanf(stdin, "%d", &N);
    for(i = 0; i < N; i++) {
        for(j = 0; j < 2; j++) {
            fscanf(stdin, "%d %d %d %d", &data[j].day, &data[j].hour, &data[j].min, &data[j].sec);
        }
        printTimeDiff(data[0], data[1]);
    }
    fprintf(stdout, "\n");
    return 0;
}