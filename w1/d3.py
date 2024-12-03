import re

# REGEX 1 to find all mul(num1, num2) matches: 'mul\([0,9]*,[0,9]*\)' 
# Add '\' before parentheses to escape the regex grouping character
# Extend this to REGEX 2 in order to find "do()" and "don't()" instances
# that either enable or disable multiplications  

with open("input_d3.txt", 'r') as file:
    file_string = file.read()

    p = re.compile('mul\([0-9]*,[0-9]*\)|do\(\)|don\'t\(\)')
    matches=p.findall(file_string)
    print(matches)

    acc = 0   # accumulator for results
    mul_enabled = True      # multiplication is enabled at program entry
    for match in matches:

        if match == "do()":
            mul_enabled = True 
        elif match == "don't()":
            mul_enabled = False
        else: 
            if mul_enabled:
                split_match = match.split(',')

                num1_str = "".join([ele for ele in split_match[0] if ele.isdigit()]) 
                num2_str = "".join([ele for ele in split_match[1] if ele.isdigit()])

                num1 = int(num1_str)
                num2 = int(num2_str)

                mul_res = num1 * num2 
                acc += mul_res


    print(acc)

file.close()