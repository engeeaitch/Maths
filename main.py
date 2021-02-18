# Program to solve maths problem...

# Find all cases where two digit numerator, divided by two digit denominator gives a two digit answer as a %age
# Each digit must be unique, and must use the digits 0, 1, 2, 3, 5, 6

# Let n10 be the tens in the numerator and n1 be the units in numerator
# so e.g. if the number was 23, n10 would be 2 and n1 would be 3
# Let d10 be the tens in the denominator and d1 be the units in the denominator
# Let a10 be the tens in the answer and a1 be the units in the answer

def main():

    allowableDigits = [0, 1, 2, 3, 5, 6]

    # Use to keep track of the number of answers
    answer = 0
    # Check all the allowable digits for each of the six digits
    for n10 in allowableDigits:
        for n1 in allowableDigits:
            for d10 in allowableDigits:
                for d1 in allowableDigits:
                    for a10 in allowableDigits:
                        for a1 in allowableDigits:
                            if isAnswer(n10, n1, d10, d1, a10, a1):
                                answer = answer + 1
                                print(
                                    f"Answer {answer} is {n10}{n1}/{d10}{d1} = {a10}{a1}%")


def isAnswer(n10, n1, d10, d1, a10, a1):
    # First check to see if any digits are repeated
    if not isDuplicated([n10, n1, d10, d1, a10, a1]):
        return False

    # Now check to see if the calculation equals the answer
    numerator = n10 * 10 + n1
    denominator = d10 * 10 + d1
    if denominator == 0:
        # Should never happen because to be zero, the digits would need to be duplicated
        # but need to check against dividing by zero.
        return False
    answer = a10 * 10 + a1
    # Now do the test (answer is a percentage)...
    if numerator / denominator * 100 == answer:
        return True
    return False


# Check to see if any of the digits are duplicated
def isDuplicated(listOfDigits):
    # Store the numbers in a set - this will remove any duplicates
    setOfDigits = set(listOfDigits)
    # Now compare the length (number of digits) of the list with the length of the set
    if len(setOfDigits) != len(listOfDigits):
        # Must be duplicates
        return False
    return True


# Run the program
main()
