from app.constants.mapping import MASTER_NUMBERS


def sum_digits(number: int) -> int:
    return sum(int(digit) for digit in str(number))


def reduce_number(number: int) -> int:
    current = number
    while current > 9 and current not in MASTER_NUMBERS:
        current = sum_digits(current)
    return current