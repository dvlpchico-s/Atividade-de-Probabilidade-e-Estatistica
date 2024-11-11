P_M = 0.25      
P_Q = 0.15      
P_M_and_Q = 0.10 
# (i) 
P_M_given_Q = P_M_and_Q / P_Q
print(f"(i) Probabilidade de ter sido reprovado em matemática dado que foi reprovado em química: {P_M_given_Q:.4f}")
# (ii) 
P_Q_given_M = P_M_and_Q / P_M
print(f"(ii) Probabilidade de ter sido reprovado em química dado que foi reprovado em matemática: {P_Q_given_M:.4f}")
# (iii)
P_M_or_Q = P_M + P_Q - P_M_and_Q
print(f"(iii) Probabilidade de ter sido reprovado em matemática ou em química: {P_M_or_Q:.4f}")