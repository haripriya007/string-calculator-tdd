import re
def extractDelimiters(input_string):

    delimiters = [",", "\n"]

    if input_string.startswith("//"):
        delimiter_part = input_string.split("\n", 1)[0]

        # Handles multiple delimiters
        custom = re.findall(r"\[(.*?)\]", delimiter_part)
        if custom:
            delimiters = custom
        else:
            #single char delimiter 
            delimiters = [delimiter_part[2:]]

    return delimiters
    
def add(numbers):
    if numbers.strip() == "": #handle whitespace
        return 0
    delimiters = extractDelimiters(numbers)
    
    if numbers.startswith("//"):
        numbers = numbers.split("\n", 1)[1]
        
    pattern = "|".join(map(re.escape, delimiters))
    num_list = [int(n) for n in re.split(pattern, numbers) if n.strip()]

    
    negatives = [n for n in num_list if n < 0]
    if negatives:
        raise Exception("negative numbers not allowed " + ", ".join(map(str, negatives)))
    return sum(n for n in num_list if n <= 1000)#ignore number greated than 1000
    