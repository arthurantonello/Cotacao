# Cotacao
Realização do desafio proposto pela empresta Abess, da implementação de um sistema de cotação monetária, afim de ingressar na vaga de Dev JR.
<<<<<<< Updated upstream
=======

Recomendado uso de máquina virtual para execução
Para utilização do código, favor digitar os seguintes códigos no terminal:

pip install django

pip install requests plotly

pip install pandas-market-calendars


-------
História de usuário:

Preciso de um sistema que guarde as cotações do dólar versus real, euro e iene(JPY) e que as exibe em um gráfico, respeitando as seguintes especificações:

•	Inicialmente o gráfico deve conter as cotações dos últimos cinco dias úteis.
•	Deve ser possível alterar o período contanto que seja de no máximo 5 dias úteis.
•	Deve ser possível variar as moedas (real, euro e iene). 

Existem algumas restrições que devem ser seguidas:
•	Os dados das cotações devem ser coletados utilizando a api do https://www.vatcomply.com/documentation (Você vai precisar usar Dólar como base). 
•	O código deve ser desenvolvido utilizando um repositório git no seu perfil do Github, BitBucket ou Gitlab;
•	Backend: deve ser implementado em python utilizando o framework Django, FastAPI ou Flask.
•	Frontend: o único requisito é exibir os gráficos de forma bem apresentada.
•	Não precisa de login, usuário, autenticação ou qualquer coisa. Só a página carregando o gráfico.

Bônus:
•	Deploy no python anywhere ou em outra hospedagem de sua preferência.
•	Criar uma api para realizar leitura das cotações persistidas no banco de dados.
>>>>>>> Stashed changes
