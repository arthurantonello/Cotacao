import datetime # Biblioteca para data hora
import requests
import json
import plotly.graph_objects as go # Utilizado o Scatter e o Figure
from plotly.utils import PlotlyJSONEncoder # Para serializar objetos de gráfico em JSON

from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    hoje = datetime.date.today()

    datas = []
    cotacao_brl = []
    cotacao_eur = []
    cotacao_jpy = []

    # Loop para pegar os últimos 5 dias (1 até 5)
    for i in range(1, 6):
        dia = hoje - datetime.timedelta(days=i) # Subtrai i dias da data de hoje
        dia_str = dia.isoformat()  # YYYY-MM-DD

        url = f"https://api.vatcomply.com/rates?date={dia_str}&base=USD" # Coleta as datas tendo base o USD
        response = requests.get(url)

        if response.status_code == 200:
            data_json = response.json() # Converte para um dicionário Python
            datas.append(dia_str) # Adiciona a data formatada na lista de datas
            rates = data_json.get("rates", {})

            cotacao_brl.append(rates.get("BRL", 0))
            cotacao_eur.append(rates.get("EUR", 0))
            cotacao_jpy.append(rates.get("JPY", 0))
        else:
            # Se não retornar 200 (sucesso) retorna 0 em todos, caso a API dê problema
            datas.append(dia_str)
            cotacao_brl.append(0)
            cotacao_eur.append(0)
            cotacao_jpy.append(0)

    # Inverte a lista se quiser do mais antigo para o mais recente
    datas.reverse()
    cotacao_brl.reverse()
    cotacao_eur.reverse()
    cotacao_jpy.reverse()

    # Cria uma Figure Plotly vazia e após insere cada uma das moedas respectivamente
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=datas, y=cotacao_brl, mode='lines+markers', name='USD -> BRL'))
    fig.add_trace(go.Scatter(x=datas, y=cotacao_eur, mode='lines+markers', name='USD -> EUR'))
    fig.add_trace(go.Scatter(x=datas, y=cotacao_jpy, mode='lines+markers', name='USD -> JPY'))

    fig.update_layout(
        title="Cotações de USD nos últimos 5 dias",
        xaxis_title="Data",
        yaxis_title="Cotação"
    )

    # Serializa a figura Plotly para uma string JSON
    grafico_json = json.dumps(fig, cls=PlotlyJSONEncoder)
    
    return render(request, "inicio.html", {"grafico_json": grafico_json}) # Retorna o gráfico em JSON e o html
