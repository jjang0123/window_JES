list1 = [1, 0, 1]
list2 = [1, 1, 2]

total = 0
for i in range(3):
    total += list1[i] * list2[i]

print(f"{list1}*{list2} = {total}")