import math
lambda_media = 5.4
probabilidade = sum((lambda_media**k * math.exp(-lambda_media)) / math.factorial(k) for k in range(5))
print(f"A probabilidade de que a loja não fique sem estoque em dois dias é aproximadamente {probabilidade:.4f}")