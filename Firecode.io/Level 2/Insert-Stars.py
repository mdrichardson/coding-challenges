# Given a string, recursively compute a new string
# where identical, adjacent characters
# get separated with a "*".
#
# Example:
# insert_star_between_pairs("cac") ==> "cac"
#
# insert_star_between_pairs("cc") ==> "c*c"

# My Notes:
#   - To make recursive, we first compare index 0 and 1, then we send the whole string, but with index 0 cut out

test_inputs = [
    'abbba',        # ab*b*ba
    None,           # None
    'abba',         # ab*ba
    'bbb'           # b*b*b
]


def insert_star_between_pairs(a_string):
    # Cover base cases
    if not a_string:
        return None
    if len(a_string) <= 1:
        return a_string
    else:
        # Cover insert case
        if a_string[0] == a_string[1]:
            # Return it with the star included, then search the rest of the string
            return '{}*{}'.format(a_string[0:1], insert_star_between_pairs(a_string[1:]))
        else:
            # It doesn't need a star, so just search the rest
            return a_string[0] + insert_star_between_pairs(a_string[1:])

for s in test_inputs:
    print(insert_star_between_pairs(s))