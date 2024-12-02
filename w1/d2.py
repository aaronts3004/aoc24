
from itertools import combinations


def is_line_safe(line_list):

    # Convert all input strings to integers
    line_list = list(map(int, line_list))

    # Check if the full string line is sorted (in either ascending or descending order, does not matter which)
    if sorted(line_list) != line_list and sorted(line_list, reverse=True) != line_list:
        return False
    
    if(len(line_list) == 1):
        return True 
    
    # Check if the numbers should appear in ascending or descending order
    ascend = False 
    if line_list[0] < line_list[1]:
        ascend = True 

    # Check for all sucessive number pairs if the conditions are met
    for i in range(len(line_list)-1):

        num1 = int(line_list[i])
        num2 = int(line_list[i+1])

        if ascend: 
            if num1 >= num2 or num2 > (num1+3):
                return False 
        else: 
            if num1 <= num2 or num2 < (num1-3):
                return False   
    
    return True

count_safe = 0
index = 1
with open("input_d1.txt", 'r') as file:

    for line in file:
        # Get the current line string and split it into the individual integer elements
        line_list = line.split()

        is_safe = is_line_safe(line_list)
        if (is_safe):
            count_safe += 1 
        else: 
            # If the current line is not safe, then check if it might be by removing exactly one element
            for i in range(len(line_list)):
                # Exclude the element at index `i` and include the rest
                sublist = line_list[:i] + line_list[i+1:]
                if (is_line_safe(sublist)):
                    count_safe += 1 
                    break 

        '''
        for num in line_list:
            sub_list = line_list[:]
            sub_list.remove(num)

            if (is_line_safe(sub_list)):
                diff.write(line)
                count_safe += 1 
                break 
        '''

file.close()
print(count_safe)

