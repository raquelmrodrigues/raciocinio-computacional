entrada = [6, 20, 26, 22, 22, 50, 10, 4, 20, 40]
janela = 5
media_movel = []
i = 0

while i < len(entrada) - janela:
    janela_entrada = entrada[i: i + janela]
    media = sum(janela_entrada) / janela
    media_movel.append(media)
    i = i + 1

print(media_movel)