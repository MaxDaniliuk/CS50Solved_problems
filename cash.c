#include <cs50.h>
#include <stdio.h>

// Declared functions
int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}




// Promtimg the user for cents
int get_cents(void)
{
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 1);
    return cents;
}
// Counting quarters
int calculate_quarters(int cents)
{
    // Up to one quarter
    int quarters;
    if (cents == 25)
    {
        quarters = 1;
    }
    else if (cents > 25 && cents < 50)
    {
        quarters = 1;
    }
    // Up to two quarters
    else if (cents >= 50 && cents < 75)
    {
        quarters = 2;
    }
    // Up to three quarters
    else if (cents >= 75 && cents < 100)
    {
        quarters = 3;
    }
    //  Up to four quarters
    else if (cents == 100)
    {
        quarters = 4;
    }
    // More than four quarters
    else if (cents > 100)
    {
        quarters = cents / 25;
    }
    else
    {
        return 0;
    }
    return quarters;
}
// Counting dimes
int calculate_dimes(int cents)
{
    // More than two dimes
    int dimes;
    if (cents >= 25 && cents <= 100)
    {
        dimes = cents / 10;
    }
    // Up to two dimes
    else if (cents >= 20 && cents < 25)
    {
        dimes = 2;
    }
    // Up to one dime
    else if (cents >= 10 && cents < 20)
    {
        dimes = 1;
    }
    // Number of coinds less than 10
    else
    {
        return 0;
    }
    return dimes;
}
// Counting dimes
int calculate_nickels(int cents)
{
    // Two or more nickels
    int nickels;
    if (cents >= 10 && cents <= 100)
    {
        nickels = cents / 5;
    }
    // One nickel
    else if (cents >= 5 && cents < 10)
    {
        nickels = 1;
    }
    // Number of coins less than 5
    else
    {
        return 0;
    }
    return nickels;
}
// Counting pennies
int calculate_pennies(int cents)
{
    // Number of coins less than 5
    int pennies;
    if (cents > 0 && cents < 5)
    {
        pennies = cents;
    }
    // Counting coins with pennies
    else if (cents <= 100)
    {
        pennies = cents / 1;
        return pennies;
    }
    return cents;
}
