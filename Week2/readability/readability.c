#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Describing the function beforehand
float index_calculator(float L, float S);
int words_counter(string text, int length);
float S_calculator(string text, int length, int words);
float L_calculator(string text, int length, int words);

// Main code of the file
int main(void)
{
    string text = get_string("Text: ");
    int length = strlen(text);
    int words = words_counter(text, length);
    float L = L_calculator(text, length, words);

    float S = S_calculator(text, length, words);

    float grade = index_calculator(L, S);
    int int_grade = round(grade);
    if (int_grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (int_grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", int_grade);
    }
}
// Calculating Index
float index_calculator(float L, float S)
{
    float index = 0.0588 * L - 0.296 * S - 15.8;
    return index;
}
// Calculate number of words
int words_counter(string text, int length)
{
    int words = 0;
    for (int i = 0; i < length; i++)
    {
        if (text[i] == ' ')
        {
            words++;
        }
    }
    words++;
    return words;
}
// Calulate S
float S_calculator(string text, int length, int words)
{
    int s = 0;
    for (int i = 0; i < length; i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            s++;
        }
    }
    float S = 100.0 / (float) words * (float) s;
    return S;
}
// Calculate L
float L_calculator(string text, int length, int words)
{
    int l = 0;
    for (int i = 0; i < length; i++)
    {
        if (isalpha(text[i]) != 0)
        {
            l++;
        }
    }
    float L = (100.0 / (float) words) * (float) l;
    return L;
}
