P_Mais_160_Homem = 0.04
P_Mais_160_Mulher = 0.01
P_Mulher = 0.60
P_Homem = 0.40
P_Mais_160 = (P_Mais_160_Homem * P_Homem) + (P_Mais_160_Mulher * P_Mulher)
P_Mulher_given_Mais_160 = (P_Mais_160_Mulher * P_Mulher) / P_Mais_160
print(f"A probabilidade de o estudante ser uma mulher, dado que tem mais de 1,60 m de altura, é: {P_Mulher_given_Mais_160:.4f}")