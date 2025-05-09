# Cotações

Um sistema que coleta cotações do dólar em relação ao real, euro e iene, exibindo-as em um gráfico. O gráfico mostra dados dos últimos 5 dias baseado na abertura da bolsa NYSE. A API do Vatcomply, conforme requisição no desafio, foi usada para coletar as cotações, e o backend foi feito em Python (Django).

 <img src="https://github.com/arthurantonello/Cotacao/blob/e0a62ba797c37c8ab76d0b9611e054a99e95d8ef/staticfiles/img/pagina.png?raw=true" alt="Tela do formulário pronto" width="1000" height="275" />

Para utilização do código, favor digitar os seguintes códigos no terminal:
> Recomendado uso de máquina virtual para execução.<br>
```
pip install django
pip install requests plotly
pip install pandas-market-calendars
pip install gunicorn
```

-------
<h3>História de usuário:</h3>

Preciso de um sistema que guarde as cotações do dólar versus real, euro e iene(JPY) e que as exibe em um gráfico, respeitando as seguintes especificações:

•	Inicialmente o gráfico deve conter as cotações dos últimos cinco dias úteis.<br>
•	Deve ser possível alterar o período contanto que seja de no máximo 5 dias úteis.<br>
•	Deve ser possível variar as moedas (real, euro e iene).<br>

Existem algumas restrições que devem ser seguidas:<br>
•	Os dados das cotações devem ser coletados utilizando a api do https://www.vatcomply.com/documentation (Você vai precisar usar Dólar como base). <br>
•	O código deve ser desenvolvido utilizando um repositório git no seu perfil do Github, BitBucket ou Gitlab;<br>
•	Backend: deve ser implementado em python utilizando o framework Django, FastAPI ou Flask.<br>
•	Frontend: o único requisito é exibir os gráficos de forma bem apresentada.<br>
•	Não precisa de login, usuário, autenticação ou qualquer coisa. Só a página carregando o gráfico.<br>
<br>
Bônus:<br>
•	Deploy no python anywhere ou em outra hospedagem de sua preferência.<br>
•	Criar uma api para realizar leitura das cotações persistidas no banco de dados.<br>

