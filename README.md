# Cotacao
<h2>Realização do desafio proposto pela empresta Abess, da implementação de um sistema de cotação monetária, afim de ingressar na vaga de Dev JR.</h2>

<h3>Tu podes olhar o projeto funcionando acessando https://cotacao-production.up.railway.app/ </h3>


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

