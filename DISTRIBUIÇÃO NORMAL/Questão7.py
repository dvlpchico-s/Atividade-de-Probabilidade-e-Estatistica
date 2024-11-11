from scipy.stats import norm
media = 500  
desvio_padrao = 100  
# (a)
limite_inferior = 450
limite_superior = 650
probabilidade = norm.cdf(limite_superior, loc=media, scale=desvio_padrao) - norm.cdf(limite_inferior, loc=media, scale=desvio_padrao)
# (b) 
valor_x = norm.ppf(0.05, loc=media, scale=desvio_padrao)
# (c) 
a = norm.ppf(0.975, loc=media, scale=desvio_padrao) - media  
print(f"(a) P(450 <= X <= 650): {probabilidade:.4f}")
print(f"(b) O valor x tal que P(X <= x) = 0.05: {valor_x:.2f}")
print(f"(c) O número a tal que P(500 <= X <= 500 + a) = 0.95: {a:.2f}")

