numeros = [1, 2, 3, 4, 5, 6]
probabilidades = [n / sum(numeros) for n in numeros] 
A = {2, 4, 6}  
B = {2, 3, 5}  
C = {1, 3, 5}  
def calcular_probabilidade(evento):
    return sum(probabilidades[n-1] for n in evento)
# (i) 
espaco_probabilidade = {n: probabilidades[n-1] for n in numeros}
print("Espaço de probabilidade:", espaco_probabilidade)
# (ii)
P_A = calcular_probabilidade(A)
P_B = calcular_probabilidade(B)
P_C = calcular_probabilidade(C)
print(f"\nP(A): {P_A}")
print(f"P(B): {P_B}")
print(f"P(C): {P_C}")
# (iii)
# (a) 
P_A_union_B = calcular_probabilidade(A.union(B))
print(f"\nP(A ∪ B) (um número par ou primo ocorre): {P_A_union_B}")
# (b) 
P_B_intersect_C = calcular_probabilidade(B.intersection(C))
print(f"P(B ∩ C) (um número ímpar primo ocorre): {P_B_intersect_C}")
# (c) 
P_A_minus_B = calcular_probabilidade(A - B)
print(f"P(A - B) (A ocorre, mas B não ocorre): {P_A_minus_B}")
