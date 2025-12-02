# https://adventofcode.com/2025/day/9
import time

with open("test_input.txt", "r") as f:
    test_input = f.read()
with open("input.txt", "r") as f:
    input = f.read()

# Code Start
answer = 0

# Code End
start_time = time.time()


end_time = time.time()
duration = end_time - start_time
print("=" * 15)
print(f"Time: {duration:.7f}s")
print(f"Answer: {answer}")
print("=" * 15)
