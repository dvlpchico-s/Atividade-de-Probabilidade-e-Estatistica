from scipy.stats import binom
p_nao_atacada = 0.98  
p_atacada_recuperavel = 0.02 * 0.5  
p_atacada_nao_recuperavel = 0.02 * 0.5 
lucro_nao_atacada = 3.5 - 1.2
lucro_atacada_recuperavel = 3.5 - (1.2 + 0.5)
lucro_atacada_nao_recuperavel = 0
lucro_medio_por_muda = (p_nao_atacada * lucro_nao_atacada +
                        p_atacada_recuperavel * lucro_atacada_recuperavel +
                        p_atacada_nao_recuperavel * lucro_atacada_nao_recuperavel)
print(f"(a) Lucro médio por muda produzida: R$ {lucro_medio_por_muda:.2f}")
lucro_esperado_10000_mudas = 10000 * lucro_medio_por_muda
print(f"(b) Lucro esperado para uma plantação de 10.000 mudas: R$ {lucro_esperado_10000_mudas:.2f}")
n = 50  
k = 45 
p_aproveitavel = p_nao_atacada + p_atacada_recuperavel  
probabilidade_aproveitaveis = 1 - binom.cdf(k - 1, n, p_aproveitavel)
print(f"(c) Probabilidade de que pelo menos 45 mudas sejam aproveitáveis em um lote de 50: {probabilidade_aproveitaveis * 100:.2f}%")