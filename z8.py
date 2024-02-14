x = -2/3
coefficients = [5, 70, 14]

result = coefficients[0]
for i in range(1, len(coefficients)):
    result = result * x + coefficients[i]

print(result)
