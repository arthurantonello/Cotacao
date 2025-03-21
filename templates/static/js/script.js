// Função para carregar o gráfico pela primeira vez
function carregarGrafico(dias) {
    let graficoDiv = document.getElementById("grafico");

    // Captura a visibilidade atual das moedas antes de atualizar
    let verVisibilidade = {};
    if (graficoDiv.data) {
        graficoDiv.data.forEach((ver, index) => {
            verVisibilidade[ver.name] = ver.visible !== "legendonly";
        });
    }

    // Faz requisição GET para obter novos dados
    fetch('/grafico_data/?dias=' + dias)
    .then(response => response.json())
    .then(data => {
        // Atualiza o gráfico SEM recriá-lo do zero
        Plotly.react('grafico', data.data, data.layout);

        // Restaura a visibilidade das moedas após a atualização
        data.data.forEach((ver, index) => {
            if (verVisibilidade.hasOwnProperty(ver.name)) {
                Plotly.restyle("grafico", { visible: verVisibilidade[ver.name] ? true : "legendonly" }, [index]);
            }
        });

        // Atualiza o valor de dias no input hidden
        document.getElementById('numDias').value = dias;
    })
    .catch(err => console.error(err));
}

// Função para mudar a quantidade de dias dinamicamente
function trocaDias(incremento) {
    let valorAtual = parseInt(document.getElementById('numDias').value);
    let novoValor = valorAtual + incremento;
    // Limita de 1 a 5
    if (novoValor < 1) novoValor = 1;
    if (novoValor > 5) novoValor = 5;
    carregarGrafico(novoValor);
}

// Carrega o gráfico inicialmente com 1 dia (ou outro valor padrão)
window.onload = function() {
    carregarGrafico(5);
};
