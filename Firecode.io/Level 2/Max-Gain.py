# Given an list of integers, write a method - max_gain - that returns the maximum gain.
# Maximum Gain is defined as the maximum difference between 2 elements in a list such that the larger element appears after the smaller element.
# If no gain is possible, return 0.
#
# Example:
# max_gain([100,40,20,10]) ==> 0
# max_gain([0,50,10,100,30]) ==> 100

# My notes:
#   - We could do this pretty simply by starting at the first number, going through the whole list
#       - Then we compare to the previous best gain (which starts at 0)
#       - Do this for all numbers until the end
#       - This would take awhile for a large list
#   - You can't sort the list. That would ruin things...
#   - You could go through the whole list. Keep track of the index of the largest and smallest numbers
#       - You need to make sure smallest comes before the largest...stop tracking the smallest if its index is larger than the largest?
#   Instantiate variables for smallest and largest indices. Set smallest at 0 and largest at 1
#   Loop through the whole enumerated list
#       If number is less than list[smallest] and i <= largest, it becomes the new smallest
#       If number is greater than list[largest], it becomes the new largest
#   If smallest < largest, return the difference. Else, return 0

test_inputs = [
    [100,40,20,10],     # 0
    [0,50,10,100,30],   # 100
    [50, 5, 100, 400, 0]# 395
]

def max_gain(input_list):
    # Instantiate variables for smallest and largest indices. Set smallest at 0 and largest at 1
    smallest = 0
    largest = 1
    # Loop through the whole enumerated list
    for i, num in enumerate(input_list):
        # If number is less than list[smallest] and i <= largest, it becomes the new smallest
        if num < input_list[smallest] and i <= largest:
            smallest = i
        # If number is greater than list[largest], it becomes the new largest
        elif num > input_list[largest]:
            largest = i
    # If smallest < largest, return the difference. Else, return 0
    if smallest < largest:
        return input_list[largest] - input_list[smallest]
    else:
        return 0

for test in test_inputs:
    print(max_gain(test))