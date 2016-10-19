"""Find the number of trailing zeroes in the factorial of a number."""

from math import factorial


def find_trailing_zeroes(num):
	"""Input any integer. Returns the number of trailing zeroes."""
    num = str(factorial(num))
    return len(num)-len(num.rstrip('0'))

if __name__ == "__main__":
    number = int(raw_input("Enter the number whose count of trailing zeroes"
    						" in the factorial is to be found? \n"))
    print find_trailing_zeroes(number)
