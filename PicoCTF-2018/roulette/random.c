#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <limits.h>

int main(int argc, char *argv[]) {
    int seed = atoi(argv[1]);

    srand(seed);

    for (int i = 0; i < 100; ++i)
        printf("%d,", rand());

    return 0;
}