import json
import numpy as np

with open('dados.json') as json_file:
    faturamento = json.load(json_file)
    
    faturamento_filtrado = []       #Lista que conterá o faturamento sem o valores quando o ganho foi zero.
    for elem in faturamento:
        if elem['valor'] != 0:
            faturamento_filtrado.append(elem)
    ## Cálculo do dia de menor valor registrado
    dia_menor_valor = min(faturamento_filtrado, key=lambda elem: elem['valor'])
    print("O dia que obteve menor valor é o dia",dia_menor_valor["dia"], "com R$", dia_menor_valor["valor"], "faturados.")

    ## Cálculo do dia de maior valor registrado
    dia_maior_valor = max(faturamento_filtrado, key=lambda elem: elem['valor'])
    print("O dia que obteve maior valor é o dia",dia_maior_valor["dia"], "com R$", dia_maior_valor["valor"], "faturados.")
    
    ## Cálculo da média entre os valores registrados
    media_valores = np.mean([elem['valor'] for elem in faturamento_filtrado])
    print("A média de valores diários alcançados excluindo os valores zerados é de: R$", round(media_valores, 3))
    
    ## Cálculo da quantidade de dias em que o valor adquirido foi maior que a média entre os valores registrados
    contador_dias_maior_que_media = 0
    for elem in faturamento_filtrado:
        if elem['valor'] > media_valores:
            contador_dias_maior_que_media += 1
    print("O valor diário é maior que a média de R$", media_valores, "em", contador_dias_maior_que_media, "dias.")