# Write your solution here
import random
def lottery_numbers(amount: int, lower: int, upper: int):
    draw = []
    if amount == 1:
        num = random.randint(lower,upper)
        draw.append(num)
        return draw

    pool = list(range(lower, upper + 1))
    lot = random.sample(pool, amount)
    lot.sort()
    return lot

if __name__ == "__main__":
    print(lottery_numbers(7, 1, 10))