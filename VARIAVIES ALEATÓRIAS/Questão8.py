import sympy as sp
p = sp.symbols('p')
equacao = sp.Eq(3 * p**2 + 2 * p, 1)
solucoes = sp.solve(equacao, p)
p_valor = [sol for sol in solucoes if 0 <= sol <= 1][0]
print(f"Valor de p: {p_valor}")
probabilidades = [0, p_valor**2, p_valor**2, p_valor, p_valor, p_valor**2]
valores_Y = [0, 1, 2, 3, 4, 5]
esperanca = sum(y * prob for y, prob in zip(valores_Y, probabilidades))
print(f"Esperança E(Y): {esperanca}")
esperanca_Y2 = sum((y**2) * prob for y, prob in zip(valores_Y, probabilidades))
variancia = esperanca_Y2 - (esperanca ** 2)
print(f"Variância Var(Y): {variancia}")