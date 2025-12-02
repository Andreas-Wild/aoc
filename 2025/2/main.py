# https://adventofcode.com/2025/day/2
import time

with open("test_input.txt", "r") as f:
    test_input = f.read()
with open("input.txt", "r") as f:
    input = f.read()

answer = 0
ranges = input.split(",")
print(ranges)
for r in ranges:
    # First let's parse the intervals to check
    ls = r.split("-")
    start = int(ls[0])
    end = int(ls[1])
    # Now check for repititions
    for num in range(start, end + 1):
        # Due to its elegance an explanation of code: Say we have some string s 'jefjef' and we want to check for repitition. Consider the first jef as A and the second jef as B.
        # The below code duplicates the string s to be S i.e. jefjefjefjef (ABAB). Then we remove the first entry S[0] and last entry S[-1] (remember exclusive upper bound)
        # such that now we have efjefjefje or ef-BA-je. Now we use the super fast string method find() to search for AB in our modified string. If we succeed in finding it
        # we see that AB == BA. This is only possible if A==B, hence jef==jef and there exists a repitition inside of our string s.
        s = str(num)
        S = s + s
        is_repitions = S[1:-1].find(s)
        # Stage 1:
        # if is_repitions != -1 and s[: len(s) // 2] == s[len(s) // 2 :]:
        # Stage 2:
        if is_repitions != -1:
            print(num)
            answer += num

start_time = time.time()


end_time = time.time()
duration = end_time - start_time
print("=" * 15)
print(f"Time: {duration:.7f}s")
print(f"Answer: {answer}")
print("=" * 15)
