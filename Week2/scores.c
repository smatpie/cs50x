#include <stdio.h>
#include <cs50.h>

const int N = 3;

float average(int length, int array[]);

int main(void)
{

    int scores[N];
    for(int i = 0; i < N; i++)
    {
        scores[i] = get_int("Score: ");
    }

    printf("Average: %f\n", average(N, scores));
}

float average(int length, int array[])
{
    int total_score = 0;
    for(int j = 0; j < length; j++)
    {
        total_score += array[j];
    }
    return total_score/(float)length;
}

