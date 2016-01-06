#include <stdio.h>

#define STEPS 100

int main(int argc, char *argv[]) {
    int width, height, length, i;
    int x1, x2, y, dx, dy;
    
    // get values from stdin
    scanf("%d %d %d\n", &width, &height, &length);
    
    // set initial coords and delta
    x1 = 0;
    x2 = length-1;
    y = 0;
    dx = 1;
    dy = 1;
    
    for(i=0; i<=STEPS; i++) {
        // print coords
        printf("%d %d ", x1, y);
        
        // check bounds (for next step) and adjust deltas
        if(x2+1 >= width) { // right
            dx = -1;
        } else if(x1-1 < 0) { // left
            dx = 1;
        }
        if(y+1 >= height) { // bottom
            dy = -1;
        } else if(y-1 < 0) { // top
            dy = 1;
        }
        
        // update coords
        x1 += dx;
        x2 += dx;
        y += dy;
    }
    
    return 0;
}