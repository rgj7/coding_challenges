// codeabbey, problem 104
// solution by whoisrgj

#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]) {
    int N, i;
    double a, b, c, s, area;
    
    struct point {
        int x;
        int y;
    };
    struct point v[3];
    
    fscanf(stdin, "%d", &N);
    for(i = 0; i < N; i++) {
        fscanf(stdin, "%d %d %d %d %d %d", &v[0].x, &v[0].y, &v[1].x, &v[1].y, &v[2].x, &v[2].y);
        a = sqrt(pow(v[1].x-v[0].x, 2)+pow(v[1].y-v[0].y, 2));
        b = sqrt(pow(v[2].x-v[1].x, 2)+pow(v[2].y-v[1].y, 2));
        c = sqrt(pow(v[0].x-v[2].x, 2)+pow(v[0].y-v[2].y, 2));
        s = (a+b+c)/2;
        area = sqrt(s*(s-a)*(s-b)*(s-c));
        fprintf(stdout, "%.8g ", area);
    }
    return 0;
}