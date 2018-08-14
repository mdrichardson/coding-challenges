# Write a function that takes in a string and returns the reversed version of the string.
#
# Examples:
#
# reverse_string("abcde") -> "edcba"
#
# reverse_string("1") -> "1"
#
# reverse_string("") -> ""
#
# reverse_string("madam") -> "madam"

# My Notes:
#   - This one is too similar to FlipIt. Let's just do a [::-1] and make it easy

test = "Orange"


def reverse_string(a_string):
    return a_string[::-1]


print(reverse_string(test))