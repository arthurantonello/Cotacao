from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.utils import PlotlyJSONEncoder
import json

def inicio(request):
    # xticks = 5
    # x = [1, 2, 3, 4]
    # y = [2, 3, 4, 3]
    # plt.plot(x, y)
    # plt.title('Cotação monetária')
    # plt.ylabel('Moedas')
    # plt.xlabel('Tempo') #Incluir o tamanho da moeda mais cara + 1 para visualização
    # plt.xticks(range(-(xticks), xticks, 1)) #Função de dias alterará aqui
    # plt.show()

     # Criando um gráfico interativo
     # Crie uma figura simples
    fig = go.Figure()
    # Adicione dados ao gráfico
    fig.add_trace(go.Scatter(
        x=[-5, 1, 2, 3, 4, 5],
        y=[-5, 10, 15, 7, 12, 22],
        mode='lines',
        name='Dados'
    ))

    grafico_json = json.dumps(fig, cls=PlotlyJSONEncoder)
    context = {"grafico_json": grafico_json}
    
    return render(request, "inicio.html", context)
