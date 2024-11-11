from scipy.stats import poisson
taxa_por_50000 = 2
habitantes_a = 200000
habitantes_b = 112500

lambda_a = (habitantes_a / 50000) * taxa_por_50000
lambda_b = (habitantes_b / 50000) * taxa_por_50000
# (a)
prob_5_afogamentos = poisson.pmf(5, lambda_a) * 100
# (b) 
prob_pelo_menos_3_afogamentos = (1 - poisson.cdf(2, lambda_b)) * 100
print(f"(a) Probabilidade de ocorrer exatamente 5 afogamentos em 200.000 habitantes: {prob_5_afogamentos:.2f}%")
print(f"(b) Probabilidade de ocorrer pelo menos 3 afogamentos em 112.500 habitantes: {prob_pelo_menos_3_afogamentos:.2f}%")