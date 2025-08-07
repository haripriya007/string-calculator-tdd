def add(numbers):
    if numbers == "":
        return 0
    numbers = numbers.replace("\n", ",")
    parts = numbers.split(",")
    return sum(map(int, parts))
    