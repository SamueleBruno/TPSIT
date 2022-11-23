#include <stdio.h>
#include <stdlib.h>

int main()
{

    int v[5];

    int *a;

    a = v;

    *(a + 3) = 28;

    *(a + 2) = 3;

    *(a + 1) = 5;

    *(a) = 12;

    while( a - v < 4){

        printf("%d\n", *(a ++));

    }

    return 0;

}
