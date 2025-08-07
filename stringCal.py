def add(numbers):
    if numbers.strip() == "": #handle whitespace
        return 0
    delimiter = ","
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]
    numbers = numbers.replace("\n", delimiter)
    parts = numbers.split(delimiter)
    
    nums = list(map(int, parts))
    negatives = [str(n) for n in nums if n < 0]
    if negatives:
        raise Exception("negative numbers not allowed " +, "."join(negatives))
    return sum(nums)
    