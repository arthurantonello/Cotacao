import datetime # Biblioteca para data hora
import requests
import json
import pandas_market_calendars as mcal # Para coletar os dias de bolsa de valores aberta
import plotly.graph_objects as go # Utilizado o Scatter e o Figure
from plotly.utils import PlotlyJSONEncoder # Para serializar objetos de gráfico em JSON


from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    # Obtém o número de dias a partir do parâmetro GET (padrão 1 dia)
    dias = int(request.GET.get('dias', 1))
    # Limita entre 1 e 5 dias
    dias = max(1, min(dias, 5))
    hoje = datetime.date.today()

    datas = []
    cotacao_brl = []
    cotacao_eur = []
    cotacao_jpy = []
    annotations = []

    # Loop para pegar os últimos 5 dias (1 até 5)
    for i in range(0, dias):
        dia = hoje - datetime.timedelta(days=i) # Subtrai i dias da data de hoje
        dia_str = dia.isoformat()  # YYYY-MM-DD
        calendario = mcal.get_calendar("NYSE")
        schedule = calendario.schedule(start_date= dia_str, end_date= dia_str)
        url = f"https://api.vatcomply.com/rates?date={dia_str}&base=USD" # Coleta as datas tendo base o USD
        response = requests.get(url)

        if response.status_code == 200:
            data_json = response.json() # Converte para um dicionário Python
            datas.append(dia_str) # Adiciona a data formatada na lista de datas
            rates = data_json.get("rates", {})

            cotacao_brl.append(rates.get("BRL", 0))
            cotacao_eur.append(rates.get("EUR", 0))
            cotacao_jpy.append(rates.get("JPY", 0))

            if schedule.empty:
                annotations.append(dict(
                    x=dia_str,
                    y= 0,  
                    yref= 'paper',
                    text="CLOSE",
                    showarrow=True,
                    arrowhead=2,
                    ax=0,
                    ay=-30,
                    font=dict(color="red")
                ))
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
    annotations.reverse()

    # Cria uma Figure Plotly vazia e após insere cada uma das moedas respectivamente
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=datas, y=cotacao_brl, mode='lines+markers', name='USD -> BRL'))
    fig.add_trace(go.Scatter(x=datas, y=cotacao_eur, mode='lines+markers', name='USD -> EUR'))
    fig.add_trace(go.Scatter(x=datas, y=cotacao_jpy, mode='lines+markers', name='USD -> JPY'))

    fig.update_layout(
        title="Cotações de USD nos últimos 5 dias",
        xaxis_title="Data",
        yaxis_title="Cotação",
        xaxis=dict(
            title="Data<br><sup>Close = Mercado da bolsa fechado</sup>",
            range=[datas[0], datas[-1]],  # Limita o eixo X ao intervalo definido
            fixedrange= True               # Impede zoom/pan no eixo X
        ),
        yaxis= dict(title="Cotação"),
        annotations = annotations
    )

    # Serializa a figura Plotly para uma string JSON
    grafico_json = json.dumps(fig, cls=PlotlyJSONEncoder)
    
    return render(request, "inicio.html", {"grafico_json": grafico_json, "dias": dias}) # Retorna o gráfico em JSON e o html
