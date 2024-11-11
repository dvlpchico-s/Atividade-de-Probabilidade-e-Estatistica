from scipy.stats import poisson
total_vazamentos = 30
comprimento_total = 60 
taxa_por_km = total_vazamentos / comprimento_total
comprimento_setor = 3
lambda_setor = taxa_por_km * comprimento_setor
k = 3
prob_pelo_menos_3 = 1 - poisson.cdf(k - 1, lambda_setor)
print(f"Probabilidade de ocorrer pelo menos 3 vazamentos em um setor de 3 km: {prob_pelo_menos_3 * 100:.2f}%")