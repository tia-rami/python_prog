# Write your solution here
import math

def hypotenuse(leg1: float, leg2: float):
    return math.sqrt(leg1**2 + leg2 **2)

if __name__ == "__main__":
    result = hypotenuse(3,4)
    print(result)