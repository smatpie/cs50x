# import cs50 library
from cs50 import get_string

# main function


def main():

    # get user input and required values
    text = get_string("Text: ")
    l = L(text)
    s = S(text)

    # apply the formula
    grade = 0.0588 * l - 0.296 * s - 15.8
    grade = round(grade)

    # set conidtions for different grade
    if grade < 0:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


# define both functions for required values
def L(string):
    s = 0
    for i in string:
        if i.isalpha() == True:
            s += 1
    w = string.split(" ")
    l = (s / len(w))*100
    return l


def S(string):
    l = 0
    for i in string:
        if i == "." or i == "!" or i == "?":
            l += 1

    w = string.split(" ")
    s = (l / len(w))*100
    return s


main()
