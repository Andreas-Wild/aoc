# https://adventofcode.com/2025/day/1
import time

with open("test_input.txt", "r") as f:
    test_input = f.read().splitlines()
with open("input.txt", "r") as f:
    input = f.read().splitlines()


def get_move(move: str) -> tuple[str, int]:
    direction = move[0]
    distance = int(move[1:])

    return direction, distance


start_time = time.time()

current_point = 50
password_count = 0

for move in input:
    direction, distance = get_move(move)
    for i in range(distance):
        # Update the dial
        if direction == "L":
            current_point -= 1
        else:
            current_point += 1
        # STAGE 2
        # Check whether we pass 0 at any point
        if current_point % 100 == 0:
            password_count += 1
    # Stage 1
    # Check whether we end at 0
    # if current_point % 100 == 0:
    #     password_count += 1


end_time = time.time()
duration = end_time - start_time
print("=" * 15)
print(f"Time: {duration:.7f}s")
print(f"Password: {password_count}")
print("=" * 15)
