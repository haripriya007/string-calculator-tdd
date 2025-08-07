import re
DEFAULT_DELIMITERS = [",", "\n"]
def extractDelimiters(input_string):

    delimiters = DEFAULT_DELIMITERS.copy()

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
        print("Input is empty or whitespace, Returning 0")
        return 0
    delimiters = extractDelimiters(numbers)
    print(f"Delimiters used: {delimiters}")
    if numbers.startswith("//"):
        numbers = numbers.split("\n", 1)[1]
        
    pattern = "|".join(map(re.escape, delimiters))
    num_list = [int(n) for n in re.split(pattern, numbers) if n.strip()]
    print(f"Parsed numbers: {num_list}")
    
    negatives = [n for n in num_list if n < 0]
    if negatives:
        raise Exception("negative numbers not allowed " + ", ".join(map(str, negatives)))
    result = sum(n for n in num_list if n <= 1000)
    #ignore number greated than 1000
    print(f"Final sum (ignoring >1000): {result}")
    return result
    