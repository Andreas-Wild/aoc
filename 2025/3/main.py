# https://adventofcode.com/2025/day/3
import time

with open("test_input.txt", "r") as f:
    test_input = f.read().splitlines()
with open("input.txt", "r") as f:
    input = f.read().splitlines()

# Code Start
answer = 0
# So we need to check where the greatest two are. Easy step one solution is to sort and use [-2].
for bank in input:
    first, second = ("1", "1")
    index = [-1, -1]
    for i, digit in enumerate(bank):
        # If digit is greater than current first place update and we still have digits left
        if digit > first and i != len(bank) - 1:
            index[0] = i
            first = digit
            # When we jump a ten, set second back to 1
            second = "1"
        # Else if digit is greater than the second place update
        elif digit >= second:
            index[1] = i
            second = digit
    if index[0] > index[1]:
        best_batteries = second + first
    else:
        best_batteries = first + second
    print(best_batteries)
    answer += int(best_batteries)
# Code End
start_time = time.time()


end_time = time.time()
duration = end_time - start_time
print("=" * 15)
print(f"Time: {duration:.7f}s")
print(f"Answer: {answer}")
print("=" * 15)
