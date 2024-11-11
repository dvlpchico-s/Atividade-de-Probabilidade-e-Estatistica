from math import comb
total_lampadas = 15
defeituosas = 5
boas = 10
escolhas = 3
# (i) 
nenhuma_defeituosa = comb(boas, escolhas)  
total_escolhas = comb(total_lampadas, escolhas) 
p_nenhuma_defeituosa = nenhuma_defeituosa / total_escolhas
print(f"(i) Probabilidade de que nenhuma seja defeituosa: {p_nenhuma_defeituosa:.4f}")
# (ii) 
uma_defeituosa = comb(defeituosas, 1) * comb(boas, 2)
p_uma_defeituosa = uma_defeituosa / total_escolhas
print(f"(ii) Probabilidade de que exatamente uma seja defeituosa: {p_uma_defeituosa:.4f}")
# (iii) 
p_pelo_menos_uma_defeituosa = 1 - p_nenhuma_defeituosa
print(f"(iii) Probabilidade de que pelo menos uma seja defeituosa: {p_pelo_menos_uma_defeituosa:.4f}")