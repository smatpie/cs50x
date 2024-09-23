#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
// sizeof is not a function taught yet but i got it through the rubber duck

// Declaring the function before hand
int score_calculator(string player, string points[], int len);

// main code
int main(void)
{

    string player1 = get_string("Player1: ");
    string player2 = get_string("Player2: ");
    string points[] = {"AEILNORSTU", "DG", "BCMP", "FHVWY", "K", "JX", "QZ"};
    int len = sizeof(points) / sizeof(points[0]);

    int total_score1 = score_calculator(player1, points, len);
    int total_score2 = score_calculator(player2, points, len);

    if (total_score1 > total_score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (total_score1 < total_score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}
// Function to calculate total points each player has
int score_calculator(string player, string points[], int len)
{
    int total_score = 0;
    for (int i = 0, length = strlen(player); i < length; i++)
    {
        char a = toupper(player[i]);
        for (int j = 0; j < len; j++)
        {
            if (strchr(points[j], a))
            {
                if (j == 0)
                {
                    total_score++;
                }
                else if (j == 1)
                {
                    total_score += 2;
                }
                else if (j == 2)
                {
                    total_score += 3;
                }
                else if (j == 3)
                {
                    total_score += 4;
                }
                else if (j == 4)
                {
                    total_score += 5;
                }
                else if (j == 5)
                {
                    total_score += 8;
                }
                else if (j == 6)
                {
                    total_score += 10;
                }
                else
                {
                    total_score += 0;
                }
            }
        }
    }

    return total_score;
}
