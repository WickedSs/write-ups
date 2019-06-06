#include <stdio.h>
#include <inttypes.h>

uint32_t value[0x18e28] ;
int exists[0x18e28];

uint32_t calc(uint32_t var_24) {
    //Check if we've already done this calculation
    if(exists[var_24]){
    //If we have, just return the precomputed value
      return value[var_24];
    }
    //If not, just continue the calculation
    uint32_t var_14;

    if (var_24 > 0x4) {
        var_14 = calc(var_24 - 0x5) * 0x1234 + (calc(var_24 - 0x1) - calc(var_24 - 0x2)) + (calc(var_24 - 0x3) - calc(var_24 - 0x4));
        return var_14;
    } else {
        var_14 = var_24 * var_24 + 0x2345;
        return var_14;
    }
    //Store the current result into the memo table
    value[var_24] = var_14;
    exists[var_24] = 1;
}

int main(void) {
  printf("%" PRIu32 "\n", calc(0x18e28));
  return 0;
}