#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int a = 1;
    // To reject any non positive number
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1);

    // Main code for the mario problem
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - a; j++)
        {
            printf(" ");
        }
        for (int k = 0; k < a; k++)
        {
            printf("#");
        }
        a++;

        printf("\n");
    }
}
