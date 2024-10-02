#include <cs50.h>
#include <string.h>
#include <stdio.h>

typedef struct
{
    string names;
    string numbers;
}
phonebook;

int main(void)
{
    phonebook phonebook[3];

    phonebook[0].names = "Carter";
    phonebook[0].numbers = "+1-617-495-1000";

    phonebook[1].names = "David";
    phonebook[1].numbers = "+1-617-495-1000";

    phonebook[2].names = "John";
    phonebook[2].numbers = "+1-949-468-2750";
    string name = get_string("Name: ");
    for (int i = 0; i < 3; i++)
    {
        if(strcmp(phonebook[i].names, name) == 0)
        {
            printf("Found %s\n", phonebook[i].numbers);
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}
