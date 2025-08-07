import re

def add(numbers):
    if numbers.strip() == "": #handle whitespace
        return 0
        
    delimiters = [",", "\n"]   
    if numbers.startswith("//"):
        delimiter_part, numbers = numbers.split("\n", 1)
        custom_delimiters =  re.findall(r"\[(.*?)\]", delimiter_part)#multi length delimiters in formatt
        if custom_delimiters:
            delimiters = custom_delimiters
        else:
            delimiters = [delimiter_part[2:]]

    pattern = "|".join(map(re.escape, delimiters))
    num_list = [int(n) for n in re.split(pattern, numbers) if n.strip()]

    
    negatives = [n for n in num_list if n < 0]
    if negatives:
        raise Exception("negative numbers not allowed " + ", ".join(map(str, negatives)))
    return sum(n for n in num_list if n <= 1000)#ignore number greated than 1000
    