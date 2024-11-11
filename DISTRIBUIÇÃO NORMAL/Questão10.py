from scipy.stats import norm
media = 5  
desvio_padrao = 0.9  
# (a) 
limite_inferior_pequenos = norm.ppf(0.15, loc=media, scale=desvio_padrao)
# (b) 
limite_inferior_medios = norm.ppf(0.65, loc=media, scale=desvio_padrao)
# (c) 
limite_superior_grandes = norm.ppf(0.85, loc=media, scale=desvio_padrao)
# (d) 
limite_superior_extras = norm.ppf(1, loc=media, scale=desvio_padrao)
print(f"Limite inferior para os 15% mais leves (pequenos): {limite_inferior_pequenos:.2f} kg")
print(f"Limite inferior para os 50% seguintes (médios): {limite_inferior_medios:.2f} kg")
print(f"Limite superior para os 20% mais pesados (grandes): {limite_superior_grandes:.2f} kg")
print(f"Limite superior para os 15% mais pesados (extras): {limite_superior_extras:.2f} kg")