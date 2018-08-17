# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

# My notes:
# Loop i in range(1, n)
#   Instantiate a blank string
#   If i % 3 = 0, append 'Fizz' to string
#   If i % 5 = 0, append 'Buzz' to string
#   If not string, string = '1'
#   print(string)

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Instantiate a return list
        return_list = []
        # Loop i in range(1, n + 1)
        for i in range(1, n + 1):
            #   Instantiate a blank string
            s = ''
            #   If i % 3 = 0, append 'Fizz' to string
            if i % 3 == 0:
                s += 'Fizz'
            #   If i % 5 = 0, append 'Buzz' to string
            if i % 5 == 0:
                s += 'Buzz'
            #   If not string, string = '1'
            if not s:
                s = i
            #   append to the list
            return_list.append(s)
        return return_list