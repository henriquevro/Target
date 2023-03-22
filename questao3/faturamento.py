import json

with open('dados.json') as json_file:
    faturamento = json.load(json_file)
    
    faturamento_filtrado = []       #Lista que conterá o faturamento sem o valores quando o ganho foi zero.
    for elem in faturamento:
        if elem['valor'] != 0:
            faturamento_filtrado.append(elem)
    print(faturamento_filtrado)
    
    