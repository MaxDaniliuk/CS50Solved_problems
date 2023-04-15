#include <cs50.h>
#include <stdio.h>

// Functions that are responsible for their corresponding tasks below
int get_startsize(void);
int get_endsize(int startsize);
int get_years(int start, int end);

int main(void)
{
    // TODO: Prompt for start size
    int start_size = get_startsize();

    // TODO: Prompt for end size
    int end_size = get_endsize(start_size);

    // TODO: Calculate number of years until your reach threshold
    int yrs = get_years(start_size, end_size);

    // TODO: Print number of years
    printf("Years: %i\n", yrs);
}

































int get_startsize(void)
{
    int start_size;
    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9);
    return start_size;
}

int get_endsize(int startsize)
{

    int end_size;
    do
    {
        end_size = get_int("End size: ");
    }
    while (end_size < 9 || end_size < startsize);
    return end_size;
}

int get_years(int start, int end)
{
    int yrs = 0;
    for (int size = start; size < end; yrs++)
    {
        size = size + size / 3 - size / 4;
    }
    return yrs;
}