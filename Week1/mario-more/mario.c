#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Making the compiler know of these functions existence
    void stairs(int n, int a);
    void stairs_reverse(int n, int a);

    int a = 1;
    // To accept only numbers between 1 to 8 inclusively
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1 || n > 8);

    // Main code for the mario problem
    for (int i = 0; i < n; i++)
    {
        stairs(n, a);
        printf("  ");
        stairs_reverse(n, a);
        a++;
        printf("\n");
    }
}
// To make the forward stairs
void stairs(int n, int b)
{
    for (int j = 0; j < n - b; j++)
    {
        printf(" ");
    }
    for (int k = 0; k < b; k++)
    {
        printf("#");
    }
}
// To make the reverse stairs
void stairs_reverse(int n, int c)
{
    for (int k = 0; k < c; k++)
    {
        printf("#");
    }
}
