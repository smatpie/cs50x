// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 17576;

int count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int a = hash(word);
    for (node *ptr = table[a]; ptr != NULL; ptr = ptr->next)
    {
        if (strcasecmp(ptr->word, word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Improve this hash function
    int a = toupper(word[0]) - 'A';

    int b;
    if (word[1] == 0)
    {
        b = 0;
    }
    else
    {
        b = toupper(word[1]) - 'A';
    }

    int c;
    if (word[2] == 0)
    {
        c = 0;
    }
    else
    {
        c = toupper(word[2]) - 'A';
    }

    int total = a * (26) * (26) + b * (26) + c;

    return total % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        return false;
    }

    // Read each word in the file
    char word[LENGTH + 1];
    while (fscanf(source, "%s", word) == 1)
    {
        // Add each word to the hash table
        node *h = malloc(sizeof(node));
        if (h == NULL)
        {
            free(h);
            return false;
        }
        strcpy(h->word, word);
        int a = hash(h->word);
        h->next = table[a];
        table[a] = h;

        count++;
    }
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *tmp;
        for (node *ptr = table[i]; ptr != NULL; ptr = tmp)
        {
            tmp = ptr->next;
            free(ptr);
        }
    }
    return true;
}
