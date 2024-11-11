questao = {
    "e5": {
        "descricao": "Conte o número de rebites defeituosos em uma asa de avião",
        "espaco_amostral": "Números inteiros de rebites defeituosos",
        "evento_possivel": "No máximo 5 rebites defeituosos"
    },
    "e9": {
        "descricao": "Observe as três velocidades (v1, v2, v3) de um míssil no instante t",
        "espaco_amostral": "(v1, v2, v3) em números reais",
        "evento_possivel": "Velocidades são positivas"
    },
    "e10": {
        "descricao": "Observe a altura de um míssil acima do solo em vários instantes",
        "espaco_amostral": "Alturas em números reais",
        "evento_possivel": "Altura máxima registrada é 500 metros"
    },
    "e11": {
        "descricao": "A resistência à tração de uma barra metálica é medida",
        "espaco_amostral": "Forças em números reais",
        "evento_possivel": "Resistência superior a 1000 N"
    },
}

for tit, resposta in questao.items():
    print(f"Experimento {tit}: {resposta['descricao']}")
    print(f"Espaço Amostral: {resposta['espaco_amostral']}")
    print(f"Evento Possível: {resposta['evento_possivel']}\n")