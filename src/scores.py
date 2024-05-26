def rank(x):
    if 10 <= x <= 20:
        return f"{x}th"

    digit = x % 10

    if digit == 1:
        return f"{x}st"

    if digit == 2:
        return f"{x}nd"

    if digit == 3:
        return f"{x}rd"

    return f"{x}th"
