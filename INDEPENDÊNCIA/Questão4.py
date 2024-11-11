
espaco_amostral = {
    ("C", "C", "C"), ("C", "C", "K"), ("C", "K", "C"), ("K", "C", "C"),
    ("K", "K", "C"), ("K", "C", "K"), ("C", "K", "K"), ("K", "K", "K")
}


evento1 = {("K", "K", "K")}  
evento2 = {("C", "K", "K"), ("K", "C", "K"), ("K", "K", "C"), ("K", "K", "K")}  
evento3 = {
    ("C", "C", "C"), ("C", "C", "K"), ("C", "K", "C"), ("K", "C", "C"),
    ("C", "K", "K"), ("K", "C", "K"), ("K", "K", "C")
} 


def probabilidade(evento, espaco_amostral):
    return len(evento) / len(espaco_amostral)


P_A = probabilidade(evento1, espaco_amostral)
P_B = probabilidade(evento2, espaco_amostral)
P_C = probabilidade(evento3, espaco_amostral)


P_A_and_B = probabilidade(evento1.intersection(evento2), espaco_amostral)
P_A_and_C = probabilidade(evento1.intersection(evento3), espaco_amostral)
P_B_and_C = probabilidade(evento2.intersection(evento3), espaco_amostral)


indep_A_B = P_A_and_B == P_A * P_B
indep_A_C = P_A_and_C == P_A * P_C
indep_B_C = P_B_and_C == P_B * P_C

print(f"Probabilidade de A: {P_A}")
print(f"Probabilidade de B: {P_B}")
print(f"Probabilidade de C: {P_C}")
print(f"Probabilidade de A ∩ B: {P_A_and_B}")
print(f"Probabilidade de A ∩ C: {P_A_and_C}")
print(f"Probabilidade de B ∩ C: {P_B_and_C}")

print(f"(A, B) são {'independentes' if indep_A_B else 'dependentes'}")
print(f"(A, C) são {'independentes' if indep_A_C else 'dependentes'}")
print(f"(B, C) são {'independentes' if indep_B_C else 'dependentes'}")