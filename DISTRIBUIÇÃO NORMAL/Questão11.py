from scipy.stats import norm
media = 1000  
desvio_padrao = 10  
# (a) 
limite_inferior = 990
prob_menor_990 = norm.cdf(limite_inferior, loc=media, scale=desvio_padrao)
# (b) 
limite_inferior_2dp = media - 2 * desvio_padrao
limite_superior_2dp = media + 2 * desvio_padrao
prob_entre_2dp = norm.cdf(limite_superior_2dp, loc=media, scale=desvio_padrao) - norm.cdf(limite_inferior_2dp, loc=media, scale=desvio_padrao)
print(f"(a) Porcentagem de garrafas com volume menor que 990 cm³: {prob_menor_990 * 100:.2f}%")
print(f"(b) Porcentagem de garrafas com volume dentro de dois desvios padrões: {prob_entre_2dp * 100:.2f}%")