# Write a function to compute the binary representation of a positive decimal integer. The method should return a string.
#
# Example:
# dec_to_bin(6) ==> "110"
#
# dec_to_bin(5) ==> "101"
# Note : Do not use in-built bin() function.

# My Notes:
#     - Algorithm is basically taking the number and dividing by two until you get to 1
#         - Remainder at each division is the number in binary, from right to left
#     - Oooh...let's do this recursively

test_inputs = [1, 2, 5, 15]  # 1, 10, 101, 111


def dec_to_bin(number, binary=''):
    # While loop on number until number = 1
    # Add number % 2 to left side of string
    binary = '{}{}'.format(number % 2, binary)
    # End if number = 1
    if number == 1:
        return binary
    # Divide number by two, rounding down
    return dec_to_bin(number/2, binary)


for test in test_inputs:
    print(dec_to_bin(test))