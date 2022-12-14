#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int is_in_circle() {
    float x = ((float) rand()) / (float) RAND_MAX;
    float y = ((float) rand()) / (float) RAND_MAX;

    if (pow(x, 2) + pow(y, 2) < 1) {
        return 1;
    } else {
        return 0;
    }
}

void calculate_pi(unsigned long iterations) {
    unsigned long inside = 0;
    for (int i = 0; i < iterations; i++) {
        if (is_in_circle()) {
            inside++;
        }
    }
    double est_pi = 4 * ((double) inside / iterations);
    printf("%lu iterations: %f (%f)\n", iterations, est_pi, est_pi - M_PI);
}

int main() {
    srand(time(NULL));
    for (int i = 2; i < 9; i++) {
        calculate_pi(pow(10, i));
    }
}
