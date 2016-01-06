/*
 * r/DailyProgrammer Challenge 248 Easy
 * Solution by whoisrgj
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// definitions

#define FILE_FORMAT_MAGIC_NUM "P3"
#define MAX_COLOR 255
#define BUFF_SZ 64

// structures

struct color {
    unsigned short int R;
    unsigned short int G;
    unsigned short int B;
};
typedef struct color Color;

struct dimension {
    int width;
    int height;
};
typedef struct dimension Dimension;

// functions

Color *initColor(unsigned short R, unsigned short G, unsigned short B) {
    Color *pColor = NULL;
    if((pColor = (Color*) malloc(sizeof(Color))) == NULL) {
        fprintf(stderr, "error allocating memory for color init.");
    } else {
        pColor->R = R;
        pColor->G = G;
        pColor->B = B;
    }
    return pColor;
}

int drawPoint(Color **grid, Dimension d, char *args) {
    unsigned short R, G, B;
    int x1, y1;
    
    // R G B x1 y1
    if(sscanf(args, "%hu %hu %hu %d %d", &R, &G, &B, &x1, &y1) != 5) {
        fprintf(stderr, "error reading arguments for point command.");
        return 0;
    }
    // set color at x,y
    *(grid+(x1*d.width+y1)) = initColor(R, G, B);
    return 1;
}

int drawLine(Color **grid, Dimension d, char *args) {
    unsigned short R, G, B;
    int x1, y1, x2, y2, dx, dy, err, e2, sx, sy;
    Color *pColor;

    // R G B x1 y1 x2 y2
    if(sscanf(args, "%hu %hu %hu %d %d %d %d", &R, &G, &B, &x1, &y1, &x2, &y2) != 7) {
        fprintf(stderr, "error reading arguments for line command.");
        return 0;
    }
    pColor = initColor(R, G, B);
    // using the Bresenham Line Algorithm
    // calculate deltas and error
    dx = abs(x2-x1);
    sx = x1<x2 ? 1 : -1;
    dy = abs(y2-y1);
    sy = y1<y2 ? 1 : -1;
    err = (dx>dy ? dx : -dy)/2;
    // set colors
    for(;;) {
        *(grid+((x1*d.width)+y1)) = pColor;
        if(x1==x2 && y1==y2)
            break;
        e2 = err;
        if(e2 > -dx) {
            err -= dy;
            x1 += sx;
        }
        if(e2 < dy) {
            err += dx;
            y1 += sy;
        }
    }
    return 1;
}

int drawRect(Color **grid, Dimension d, char *args) {
    unsigned short R, G, B;
    int x1, y1, h, w, i, start, end;
    Color *pColor;

    // R G B height width
    if(sscanf(args, "%hu %hu %hu %d %d %d %d", &R, &G, &B, &x1, &y1, &h, &w) != 7) {
        fprintf(stderr, "error reading arguments for rect command.");
        return 0;
    }
    pColor = initColor(R, G, B);
    // top bottom
    start = x1*d.width+y1;
    end = start+w;
    for(i=start; i<end; i++) {
        *(grid+i) = pColor;
        *(grid+(i+(h-1)*d.width)) = pColor;
    }
    // left right
    start = (x1+1)*d.width+y1;
    end = start+((h-2)*d.width);
    for(i=start; i<end; i=i+d.width) {
        *(grid+i) = pColor;
        *(grid+(i+(w-1))) = pColor;
    }
    return 1;
}

void printGrid(Color **grid, Dimension d) {
    int i, j;
    Color *pColor;

    for(i=0; i<d.height; i++) {
        for(j=0; j<d.width; j++) {
            if((pColor = *(grid+(i*d.width+j))) != NULL)
                fprintf(stdout, "%-4d%-4d%-4d%4s", pColor->R, pColor->G, pColor->B, "");
            else
                fprintf(stdout, "%-4d%-4d%-4d%4s", 0, 0, 0, "");
        }
        fprintf(stdout, "\n");
    }
}

// end functions

int main(int argc, char *argv[]) {

    Color **grid = NULL;
    Dimension d;
    int i;
    char buffer[BUFF_SZ], *cmd, *args;

    // get dimensions
    if(fscanf(stdin, "%d %d", &d.width, &d.height) != 2) {
        fprintf(stderr, "error: could not correctly scan dimensions.");
        return EXIT_FAILURE;
    }

    // allocate memory for grid
    if((grid = (Color**) malloc(sizeof(Color*)*d.width*d.height)) == NULL) {
        fprintf(stderr, "error: could not allocate memory for grid.");
        return EXIT_FAILURE;
    }
    // init grid of Color pointers to NULL
    for(i = 0; i<d.width*d.height; i++) {
        *(grid+i) = NULL;
    }

    // read and parse commands from STDIN
    while(fgets(buffer, BUFF_SZ, stdin) != NULL) {
        cmd = strtok(buffer, " "); // command
        args = strtok(NULL, ""); // arguments
        if(strcmp(cmd, "point") == 0) {
            drawPoint(grid, d, args);
        } else if(strcmp(cmd, "line") == 0) {
            drawLine(grid, d, args);
        } else if(strcmp(cmd, "rect") == 0) {
            drawRect(grid, d, args);
        }
    }

    // print output
    fprintf(stdout, "%s\n", FILE_FORMAT_MAGIC_NUM);
    fprintf(stdout, "%d %d\n", d.width, d.height);
    fprintf(stdout, "%d\n", MAX_COLOR);
    printGrid(grid, d);

    return EXIT_SUCCESS;
}