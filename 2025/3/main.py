# https://adventofcode.com/2025/day/3
import time

with open("test_input.txt", "r") as f:
    test_input = f.read().splitlines()
with open("input.txt", "r") as f:
    input = f.read().splitlines()


def find_start(digit_idx_pairs: list[tuple[int, str]], n: int) -> (int, str):
    for digit_idx_pair in digit_idx_pairs:
        idx = digit_idx_pair[0]
        digit = digit_idx_pair[1]

        if idx < n:
            return idx, digit


# Code Start
answer = 0
# We need to sort the banks but remember their original positions
for bank in test_input:
    # n is the maximum index our starting point can to have
    n = len(bank) - 11
    values = sorted(enumerate(list(bank)), key=lambda x: x[1], reverse=True)
    # Now we need to select our starting point
    base = ""
    for i in range(12):
        idx, digit = find_start(values, n)
        base += digit
        n += 1
        values.remove((idx, digit))
    print(base)
    answer += int(base)
# Code End
start_time = time.time()


end_time = time.time()
duration = end_time - start_time
print("=" * 15)
print(f"Time: {duration:.7f}s")
print(f"Answer: {answer}")
print("=" * 15)
