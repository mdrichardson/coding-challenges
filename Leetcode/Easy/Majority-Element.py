# Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2

# My notes:
#   It would be pretty easy to add everything to a dict and +1 the value each time we see it...if the value is ever > n/2, we return it
#   Maybe there's something we can do with set()
#       If we took set(3,2,3) we get 3,2. Summed, is 5. 5/2 == 2.5. 3>2.5, so maybe that's it
#       set(2,2,1,1,1,2,2) = 2,1. Summed, is 3. 3/2 is 1.5. 2>1.5...but let's try to make the answer the smaller of the two numbers...
#       set(5,5,5,1,1,1,1,1) = 5,1. Summed is 6. 6/2=3 and 1<3. So that doesn't work. Maybe we divide by the length of the list. The one that appears the most frequently would affect the average
#       set(5,5,5,1,1,1,1,1) = 5,1. Set average is 3, but list average is 5+5+5+1+1+1+1/8=2.35. Since the list average is less than the set average, the answer should be the smaller number
#       set(4,4,3,3,3) = 4,3. Set average = 3.5. List average = 4+4+3+3+3/5=3.4. 3.4 < 3.5, so the answer is the smaller again
#       Does this work for >2 unique #s? set(1,1,2,2,2,2,3) = 1,2,3. Average is 2. List average = 1.86. Maybe it's the closest to the average? 2 is, in this case
#       set(-5,3,3,3,9). Set average is 2.333. list average = 2.6. Works there
#       set(1,1,1,1,1,1,1,9,9,9,9,9,9). Set average is 5. List average is 4.7. 9 is closer to the average and list average...
#       I think we have to do the dict method

test = [2,2,1,1,1,2,2]


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Catch edge cases
    if len(nums) < 2:
        return nums[0]
    # Instantiate and empty dict
    appearances = {}
    # Store len(nums) / 2 so we don't calculate every time
    n_length = len(nums) / 2
    # Loop through the numbers
    for n in nums:
        # Try to get dict[n]
        appearance_amt = appearances.get(n, 0)
        # If we've seen n, +1 to its value
        if appearances:
            total = appearance_amt + 1
            # Return if > len(nums)/2
            if total >= n_length:
                return n
            # Otherwise, just set the value to the new total
            appearances[n] = total
        # If we haven't seen it, add it to the dict
        else:
            appearances[n] = 1

print(majorityElement(test))