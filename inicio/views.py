import datetime
import requests
import json
import plotly.graph_objects as go
from plotly.utils import PlotlyJSONEncoder

from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    # Data de hoje
    hoje = datetime.date.today()
    
    # Listas para armazenar as datas e cotações
    datas = []
    cotacao_brl = []
    cotacao_eur = []
    cotacao_jpy = []
    
    # Obter os últimos 5 dias (do mais antigo para o mais recente)
    # Se quiser inverter a ordem no gráfico, basta inverter a lógica abaixo.
    for i in reversed(range(5)):
        dia = hoje - datetime.timedelta(days=i)
        dia_str = dia.isoformat()  # Formato YYYY-MM-DD

        # Monta a URL da API. Exemplo de endpoint histórico:
        # https://api.vatcomply.com/2023-03-01?base=USD
        url = f"https://api.vatcomply.com/rates?{dia_str}&base=USD"
        
        try:
            response = requests.get(url)
            data_json = response.json()

            # Guardar as datas e as cotações
            datas.append(dia_str)
            # "rates" é um dicionário com as chaves das moedas
            cotacao_brl.append(data_json["rates"].get("BRL", 0))
            cotacao_eur.append(data_json["rates"].get("EUR", 0))
            cotacao_jpy.append(data_json["rates"].get("JPY", 0))
        except Exception as e:
            # Em caso de erro, preenche com zero ou trate como desejar
            datas.append(dia_str)
            cotacao_brl.append(0)
            cotacao_eur.append(0)
            cotacao_jpy.append(0)
            print("Erro ao acessar API:", e)

    # Criar o gráfico com Plotly
    fig = go.Figure()

    # Trace para BRL
    fig.add_trace(go.Scatter(
        x=datas,
        y=cotacao_brl,
        mode='lines+markers',
        name='USD -> BRL',
        line=dict(color='green')
    ))

    # Trace para EUR
    fig.add_trace(go.Scatter(
        x=datas,
        y=cotacao_eur,
        mode='lines+markers',
        name='USD -> EUR',
        line=dict(color='blue')
    ))

    # Trace para JPY
    fig.add_trace(go.Scatter(
        x=datas,
        y=cotacao_jpy,
        mode='lines+markers',
        name='USD -> JPY',
        line=dict(color='red')
    ))

    # Personalizar layout (opcional)
    fig.update_layout(
        title="Cotações de USD nos últimos 5 dias",
        xaxis_title="Data",
        yaxis_title="Cotação",
        hovermode="x unified"
    )

    # Converter a figura para JSON
    grafico_json = json.dumps(fig, cls=PlotlyJSONEncoder)
    
    return render(request, "inicio.html", {"grafico_json": grafico_json})
