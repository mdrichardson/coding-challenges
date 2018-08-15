# Given a sorted list of integer ranges, merge all overlapping ranges.
#
# Example:
# Input  : [[1,10], [5,8], [8,15]]
# Output : [[1,15]]

# My Notes:
#   - Ranges are ordered by lowest range, which helps
#   - Instantiate a list of Ranges, to return at the end
#   - Return the range if it's the only one
#   - Instantiate a root index at 0 and a comparison index at 1
#   - Use a while loop that stops once both comparison and root reach the end - Just while True and break out right away
#       - If comparison is greater than the length of the list, we just append comparison as a range and break the loop
#       - Set lower as root[0] and upper as root[1]
#       - If comparison[0] > upper:
#           - The comparison range can't merge with lower/upper
#           - append current lower and upper as a range to Ranges
#           - Set root to comparison (so we start at the next possible merge)
#           - Set comparison as root + 1
#       - Else:
#           - This means we can merge the ranges
#           - Set upper to comparison[1], comparison + 1 so we move to the next keep root the same
#   - Return Ranges

class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "[" + str(self.lower_bound) + "," + str(self.upper_bound) + "]"

a = Range(1, 5)
b = Range(5, 10)
c = Range(11, 15)
d = Range(15, 20)
test_input = [a, b, c, d] # [[1,10], [11,20]]

class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "[" + str(self.lower_bound) + "," + str(self.upper_bound) + "]"

def merge_ranges(input_range_list):
    # Instantiate a list of Ranges, to return at the end
    ranges = []
    # Instantiate a root index at 0 and a comparison index at 1
    root = 0
    comparison = 1
    # Set bounds by default
    set_bounds = True
    # Use a while loop that stops once both comparison and root reach the end - Just while True and break out right away
    while True:
        # If comparison is greater than the length of the list, we append root to the list and break
        if comparison >= len(input_range_list):
            ranges.append(Range(input_range_list[root].lower_bound, max(upper, input_range_list[root].upper_bound)))
            break
        # See if we need to set lower and upper based off root
        if set_bounds:
            # Set lower as [root][0] and upper as [root][1]
            lower = input_range_list[root].lower_bound
            upper = input_range_list[root].upper_bound
        # If comparison[0] > upper:
        if input_range_list[comparison].lower_bound > upper:
            # The comparison range can't merge with lower/upper
            # Append current lower and upper as a range to Ranges
            ranges.append(Range(lower, upper))
            # Set root to comparison (so we start at the next possible merge)
            root = comparison
            # Set comparison as root + 1
            comparison = root + 1
            # Ensure we set the bounds next time
            set_bounds = True
        else:
            # This means we can merge the ranges
            # Set upper to max of comparison[1] and upper, comparison + 1 so we move to the next keep root the same
            upper = max(upper, input_range_list[comparison].upper_bound)
            comparison += 1
            # Don't reset the bounds
            set_bounds = False
    # Return Ranges
    return ranges



for x in merge_ranges(test_input):
    print x