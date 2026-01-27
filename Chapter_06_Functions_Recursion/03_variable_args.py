def sum_all_numbers(*args):
    """Function that can take ANY number of inputs."""
    total = sum(args)
    return f"Total Sum: {total}."

# Calling with a different number of arguments
print(sum_all_numbers(10, 20))
print(sum_all_numbers(5, 15, 25, 35, 50))
