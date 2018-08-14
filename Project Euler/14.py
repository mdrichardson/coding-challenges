"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

#Optimized, not mine
def find(current_iteration, map):
    rounds = 0
    while current_iteration != 1:
        if current_iteration in map:
            return map[current_iteration] + rounds
        rounds += 1
        if current_iteration % 2 == 0:
            current_iteration //= 2
        else:
            current_iteration = (current_iteration * 3) + 1
    return rounds + 1


def main():
    map = {}
    best_chain = 0
    best_number = 0
    for number in range(1, 1000000, 2):
        answer = find(number, map)
        map[number] = answer
        if answer > best_chain:
            best_chain = answer
            best_number = number
    print ("result of %d with %d chains" % (best_number, best_chain))

main()
"""
# TOO SLOW
longest_sequence = 0
best = 0

for x in range(2, 1000000):
    test = x
    length = 1
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        length += 1
    if length > longest_sequence:
        longest_sequence = length
        best = test

print(longest_sequence, 524)
print(best, 837799)
"""
