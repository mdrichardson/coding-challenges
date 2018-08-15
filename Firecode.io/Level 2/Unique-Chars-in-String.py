# Write a function that takes in an input string and returns True if all the characters in the string are unique,
# False if there is even a single repeated character.

# Examples:
#
# unique_chars_in_string("abcde") -> True
#
# unique_chars_in_string("aa") -> False
#
# unique_chars_in_string("") -> True

# My notes:
#   - Seems like a good one for a hash table
#   - Loop through the string
#   - Check to see if it's in our hash table. If so, return False
#   - If not, add it to the hash table
#   - Hindsight, I could have used set() instead of a dict. Same complexity, but maybe a little less storage?
#   - A really nice one-liner: return len(set(input_string)) == len(input_string)

def unique_chars_in_string(input_string):
    # Instantiate our hash table
    found = {}
    for char in input_string:
        # Check to see if it exists in our found dict
        if found.get(char, None):
            # If it does, return false
           return False
        else:
            # If it doesn't, add it
            found[char] = True
    # If we've made it this far, there's no duplicates, so return True
    return True