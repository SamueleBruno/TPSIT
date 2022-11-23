#include <stdio.h>
#include <stdlib.h>

#define DIM 5

int main()
{
    int *v;
    v = (int *)malloc(sizeof(int) * DIM);

    for (int i = 0; i < DIM; i++)
    {

        printf("%d: ", i + 1);
        scanf("%d", (v + i));

    }

    printf("\n");
    int temp = 0;

    for (int i = 1; i < DIM; i++)
    {

        for (int j = 0; j < i; j++)
        {

            if (*(v + i) < *(v + j))
            {

                temp = *(v + i);
                *(v + i) = *(v + j);
                *(v + j) = temp;

            }

        }

    }

    for (int i = 0; i < DIM; i++)
    {

        printf("%d ", *(v + i));
        
    }

    printf("\n");
    free(v);

    return 0;
}