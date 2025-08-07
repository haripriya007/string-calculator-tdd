def add(numbers):
    if numbers == "":
        return 0
    numbers = numbers.replace("\n", ",") #newline delimit
    parts = numbers.split(",")
    return sum(map(int, parts))
    