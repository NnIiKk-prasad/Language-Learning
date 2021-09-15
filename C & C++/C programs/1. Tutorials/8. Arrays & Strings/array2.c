// -----Two dimensional arrays in C-----
#include <stdio.h>

void main()
{
    // Addition of two matrices
    int A[3][3], B[3][3], C[3][3], i, j;
    
    printf("\nEnter 9 values for first matrix\n");
    for (i = 0; i <= 2; i++)
        for (j = 0; j <= 2; j++)
            scanf("%d", &A[i][j]);

    printf("\nEnter 9 values for second matrix\n");
    for (i = 0; i <= 2; i++)
        for (j = 0; j <= 2; j++)
            scanf("%d", &B[i][j]);

    printf("\nResultant matrix is\n");
    for (i = 0; i <= 2; i++)
    {
        for (j = 0; j <= 2; j++)
        {
            C[i][j] = A[i][j] + B[i][j];
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }
}
