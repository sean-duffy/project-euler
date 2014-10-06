#include <stdio.h>

int main(void) {
    int n = 0;
    int fib1 = 1;
    int fib2 = 2;
    int sum = fib2;

    while (n < 4000000) {
        n = fib1 + fib2;
        fib1 = fib2;
        fib2 = n;
        if (n % 2 == 0) {
            sum += n;
        }
    }
    printf("%d\n", sum);
}
