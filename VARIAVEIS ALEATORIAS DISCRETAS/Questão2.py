import math
lambda_diaria = 30 / 7
probabilidade_ate_3 = sum((lambda_diaria**k * math.exp(-lambda_diaria)) / math.factorial(k) for k in range(4))
probabilidade_5_dias = probabilidade_ate_3 ** 5
print(f"A probabilidade de seguir a regra por 5 dias consecutivos é aproximadamente {probabilidade_5_dias:.4f}")