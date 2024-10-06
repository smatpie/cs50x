# import cs50
from cs50 import get_float

# main function defined


def main():

    # taking user input and checking it
    while True:
        change = get_float("Change: ")
        change = int(change * 100)
        if change > 0:
            break

    # calculating all the dimes and quarters
    quarter = calculate_coins(change, 25)
    change -= quarter*25

    ten = calculate_coins(change, 10)
    change -= ten*10

    five = calculate_coins(change, 5)
    change -= five*5

    one = calculate_coins(change, 1)
    change -= one*1

    # printing the final answer
    print(quarter + ten + five + one)


# function to calculate all the coins
def calculate_coins(change, cointype):
    coin = 0
    while change >= cointype:
        coin += 1
        change = change - cointype
    return coin


main()
