import math

x = 0
mu = 1.5
rho = 2.0

term1 = 1 / math.sqrt(2 * math.pi * rho)
term2 = math.exp(-((x - mu) ** 2) / (2 * (rho ** 2)))
answer = term1 * term2

print(f"5번 문제 값: {answer}")