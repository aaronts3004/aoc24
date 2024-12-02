
from collections import Counter

left = []
right = []

with open("input_d1.txt", "r") as f: 
    for line in f:
        # print(line)
        l = line.split()
        left.append(l[0])
        right.append(l[1])
f.close()    

print(len(left))
print(len(right))

counts = Counter(right)
# print(counts)

res = 0
for i in range(0,len(left)):

    ith_string = left[i]
    mul = int(ith_string) * counts[ith_string]

    res += mul

print(res)
