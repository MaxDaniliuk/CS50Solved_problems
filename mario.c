#include <cs50.h>
#include <stdio.h>

// Declared functions
int get_height(void);
void print_pyramid(int height);


int main(void)
{
    // Prompt the user for a pyramid's height

    int height = get_height();

    // Build the pyramid

    print_pyramid(height);
}


























// Declare the functions
int get_height(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    return height;
}

void print_pyramid(int height)
{
    // Loop to add a line
    for (int lineno = 0; lineno < height; lineno++)
    {
        // Loop to add a 'space'
        for (int space = height - lineno; space > 1; space--)
        {
            printf(" ");
        }
        // Loop to create a left side
        for (int lcolumn = 0; lcolumn <= lineno; lcolumn++)
        {
            printf("#");
        }
        // Separates one pyramid's side from another
        printf("  ");

        // Loop to a right side
        for (int rcolumn = 0; rcolumn <= lineno; rcolumn++)
        {
            printf("#");
        }
        printf("\n");
    }
}