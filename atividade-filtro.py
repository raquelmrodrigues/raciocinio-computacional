"""
Suponha que você está realizando um experimento científico no qual são necessários o monitoramento e a análise da evolução
da temperatura em um dispositivo eletrônico. Após uma série de análises, você percebeu que o sensor que foi usado captou
muito ruído e este ruído está dificultando a análise da evolução da temperatura no tempo.
Desenvolva um programa em Python que seja capaz de filtrar esse sinal, usando o filtro mediano. Considere que os dados
desse sensor sejam passados por meio de uma lista de valores decimais.
"""

coluna = [29.2, 29.3, 29.4, 29.2, 29.2, 29.2, 29.3, 29.2, 29.1, 29.4, 29.2, 29.1, 29.1, 29.2, 29.1, 29.1, 29.2, 29.2,
          29.0, 29.1, 29.1, 29.1, 29.2, 29.1, 29.0, 29.2, 29.2, 29.0, 29.2, 29.4, 29.3, 29.3, 29.3, 29.5, 29.4, 29.4,
          29.5, 29.5, 29.5, 29.5, 29.5, 29.5, 29.6, 29.5, 29.6, 29.7, 29.7, 29.7, 29.8, 29.8, 29.8, 29.9, 29.8, 29.9,
          29.9, 29.9, 29.9, 29.9, 30.0, 30.0, 30.0, 30.1, 30.2, 30.1, 30.1, 30.3, 30.2, 30.2, 30.3, 30.3, 30.3, 30.3,
          30.3, 30.3, 30.3, 30.3, 30.3, 30.4, 30.4, 30.3, 30.3, 30.3, 30.4, 30.3, 30.3, 30.3, 30.4, 30.3, 30.3, 30.3,
          30.4, 30.3, 30.3, 30.4, 30.3, 30.3, 30.3, 30.3, 30.3, 30.2, 30.3, 30.3, 30.3, 30.2, 30.2, 30.2, 30.2, 30.2,
          30.2, 30.2, 30.2, 30.2, 30.1, 30.1, 30.2, 30.0, 30.0, 30.1, 30.0, 30.0, 30.0, 30.1, 30.0, 29.9, 30.0, 30.0,
          30.0, 30.1, 30.0, 29.9, 30.0, 30.0, 30.0, 29.9, 30.0, 29.9, 29.9, 30.0, 30.0, 30.0, 29.9, 29.9, 30.1, 29.9,
          30.0, 29.9, 30.0, 30.0, 29.9, 30.0, 30.1]
def filtroMediano(coluna):
    novaColuna = []
    novaColuna.append(coluna[0])
    novaColuna.append(coluna[1])
    for idx in range(0, len(coluna) -1):
        novaColuna.append((coluna[idx] + coluna[idx+1]) / 2)

    return novaColuna

novaColuna = filtroMediano(coluna)

for v in novaColuna:
    print(v)