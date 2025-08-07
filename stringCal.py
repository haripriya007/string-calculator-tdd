def add(numbers):
    if numbers == "":
        return 0
    parts = numbers.split(",")
    return sum(map(int, parts))
    #Already it will handles multiple numbers via split