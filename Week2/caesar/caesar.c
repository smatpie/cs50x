#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Declaring functions
bool only_digits(string s);
char rotate(char c, int k);

// Main code for caesar
int main(int argc, string argv[])
{
    // Check if argv[] has only one input
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        bool x = only_digits(argv[1]);
        // Check if argv[] is only digits
        if (x == false)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
        else
        {

            int k = atoi(argv[1]);
            string plaintext = get_string("plaintext: ");
            int length = strlen(plaintext);
            printf("ciphertext: ");
            for (int i = 0; i < length; i++)
            {
                char c = rotate(plaintext[i], k);
                printf("%c", c);
            }
            printf("\n");
        }
    }
}

// To check if is only digits in argv[]
bool only_digits(string s)
{
    int l = strlen(s);
    int check = 0;
    for (int i = 0; i < l; i++)
    {
        if (isdigit(s[i]))
        {
            check++;
        }
        else
        {
            check--;
        }
    }
    if (check == l)
    {
        return true;
    }
    else
    {
        return false;
    }
}

// To rotate the characters
char rotate(char c, int k)
{
    if (islower(c))
    {
        char p = (c - 'a' + k) % 26 + 'a';
        return p;
    }
    else if (isupper(c))
    {
        char p = (c - 'A' + k) % 26 + 'A';
        return p;
    }
    else
    {
        return c;
    }
}
