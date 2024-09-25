#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Declaring functions
bool only_alpha(string s);
void substitute(char c, string k);
bool duplicate(string k);

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
        bool x = only_alpha(argv[1]);
        // Check if argv[] is only digits
        if (x == false)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
        else
        {
            // Check if key has all characters
            if (strlen(argv[1]) != 26)
            {
                printf("Key must contain 26 characters\n");
                return 1;
            }
            else
            {
                // Check if key has duplicates
                if (!duplicate(argv[1]))
                {
                    printf("A key should not contain duplicate characters\n");
                    return 1;
                }
                else
                {
                    // Main Code
                    string k = argv[1];
                    string plaintext = get_string("plaintext: ");
                    int length = strlen(plaintext);
                    printf("ciphertext: ");
                    for (int i = 0; i < length; i++)
                    {
                        substitute(plaintext[i], k);
                    }
                    printf("\n");
                }
            }
        }
    }
}

// To check if is only alpha in argv[]
bool only_alpha(string s)
{
    int l = strlen(s);
    int check = 0;
    for (int i = 0; i < l; i++)
    {
        if (!isalpha(s[i]))
        {
            return false;
        }
    }
    return true;
}

// To substitute the characters
void substitute(char c, string k)
{
    if (isalpha(c))
    {
        if (isupper(c))
        {
            int index = c - 'A';
            printf("%c", toupper(k[index]));
        }
        else if (islower(c))
        {
            int index = c - 'a';
            printf("%c", tolower(k[index]));
        }
    }
    else
    {
        printf("%c", c);
    }
}
// Function for checking duplicate
bool duplicate(string k)
{
    bool seen[26] = {false};

    for (int i = 0; i < 26; i++)
    {
        int index = tolower(k[i]) - 'a';
        if (seen[index])
        {
            return false;
        }
        else
        {
            seen[index] = true;
        }
    }
    return true;
}
