import json
from armazenamento import Banco

def atualizar_estoque(arquivos: dict, json_name= '.estoque_atual.json'):
    salvar = {}

    insumo_comprado = Banco(arquivos['insumo_comprado'])
    insumo_comprado = insumo_comprado.ler()
    print(insumo_comprado)

    insumo_consumo  = Banco(arquivos['insumo_consumo'])
    insumo_consumo  = insumo_consumo.ler()

    animal_comprado = Banco(arquivos['animal_comprado'])
    animal_comprado = animal_comprado.ler()

    animal_vendido  = Banco(arquivos['animal_vendido'])
    animal_vendido  = animal_vendido.ler()

    custos_despesas = Banco(arquivos['custos_despesas'])
    custos_despesas = custos_despesas.ler()

    if insumo_comprado:
        insumos = {} # coleta todos os ids únicos
        for linha in insumo_comprado[1:]:
            if not linha[1] in insumos:
                insumos[linha[1]] = linha[3]
            else:
                insumos[linha[1]] += linha[3]
        salvar['insumo'] = insumos

    with open(json_name, 'w') as arq_json:
        json.dump(salvar, arq_json, indent= 4)

if __name__ == '__main__':
    CSV = {
        "insumo_dados": "insumo_dados.csv",
        "insumo_comprado": "insumo_comprado.csv",
        "insumo_consumo": "insumo_consumo.csv",
        "animal_comprado": "animal_comprado.csv",
        "animal_vendido": "animal_vendido.csv",
        "categoria_financeiro": "categoria_financeiro.csv",
        "custos_despesas": "custos_despesas.csv"
    }
    atualizar_estoque(CSV)
