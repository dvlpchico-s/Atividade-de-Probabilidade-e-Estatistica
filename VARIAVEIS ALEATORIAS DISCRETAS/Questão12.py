from scipy.stats import binom
n = 100       
p = 0.02       
k = 3          
prob_3_defeituosos = binom.pmf(k, n, p)
print(f"Probabilidade de existirem exatamente 3 defeituosos em uma amostra de 100: {prob_3_defeituosos * 100:.2f}%")