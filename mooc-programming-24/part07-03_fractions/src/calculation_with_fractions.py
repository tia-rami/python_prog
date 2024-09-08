# Write your solution here
import fractions
def fractionate(amount: int):
    result_list = []
    for i in range(amount):
        result_list.append(fractions.Fraction(1,amount))

    return result_list

if __name__ == "__main__":
    result_fraction = fractionate(5)
    print(result_fraction)

