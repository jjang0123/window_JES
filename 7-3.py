numbers = [1, 2, 2, 5, 3, 4, 3, 5, 1, 6]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print(result)