from itertools import permutations
# (a) 
chaves = ['C1', 'C2', 'C3', 'C4']
espaco_amostral = [chaves[:i+1] for i in range(len(chaves))]
print("(a) Espaço amostral para o experimento:")
for sequencia in espaco_amostral:
    print(sequencia)
# (b) 
valores_X = list(range(1, len(chaves) + 1))
print("\n(b) Valores possíveis de X (número de chaves experimentadas até abrir a porta):", valores_X)