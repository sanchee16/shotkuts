"""Check if a number if positive or negative. 0 is also considered positive."""


def positive_or_negative_number_by_bit(num):
    """Input a number. Return Positive or negative."""
    return "Negative" if num >> 32 else "Positive"


def positive_or_negative_number_by_zero(num):
    """Input a number. Return Positive or negative."""
    return "Negative" if num < 0 else "Positive"

if __name__ == "__main__":
    number = int(raw_input("Enter the number\n"))
    print positive_or_negative_number_by_bit(number)
    print positive_or_negative_number_by_zero(number)
