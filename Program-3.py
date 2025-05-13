def generate_modified_odd_series(a: int):
    if a % 2 == 0:
        count = a - 1  # even input → one less
    else:
        count = a      # odd input → full

    series = [2 * i + 1 for i in range(count)]
    return series

# Example usage:
a = int(input("Enter a positive integer: "))
result = generate_modified_odd_series(a)
print("Output:", ", ".join(map(str, result)))
