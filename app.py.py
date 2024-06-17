<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CENTRO DE DISTRIBUIÇÃO JOANIN</title>
</head>
<body>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            color: #333;
        }

        .header {
            background-color: #008000;
            text-align: center;
            padding: 20px 0;
            color: #fff;
            font-weight: bold;
            font-size: 24px;
            margin-bottom: 20px;
        }

        .container {
            width: 90%;
            margin: 0 auto;
            background-color: #F7519; /* Laranja */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            color: #333;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th {
            padding: 10px;
            text-align: left;
            background-color: #FFA500; /* Laranja */
            color: #fff;
        }

        td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        tr:nth-child(even) {
            background-color: #fff; /* Branco */
        }

        tr:hover {
            background-color: #ddd;
        }
    </style>

    <div class="header">
        BEM VINDO AO CENTRO DE DISTRIBUIÇÃO JOANIN ANCHIETA
    </div>

    <div class="container">
        <table id="data-table">
            <!-- O conteúdo da tabela será preenchido dinamicamente -->
        </table>
    </div>

    <!-- Adicione o código JavaScript para carregar e atualizar os dados do arquivo -->
    <script>
        // Função para carregar e atualizar os dados do arquivo
        function loadData() {
            var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function() {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        updateTable(xhr.responseText);
                    } else {
                        console.error('Erro ao carregar o arquivo:', xhr.status);
                    }
                }
            };
            // Adicione um parâmetro de data e hora aleatório à URL para evitar o cache
            var url = 'temp/painel.csv?' + new Date().getTime();
            xhr.open('GET', url, true);
            xhr.send();
        }

        // Função para atualizar a tabela com os dados do arquivo
        function updateTable(data) {
            var table = document.getElementById('data-table');
            table.innerHTML = ''; // Limpa o conteúdo atual da tabela
            var lines = data.split('\n'); // Divide o texto em linhas
            var headerRow = '<tr>'; // Inicializa a linha de cabeçalho
            lines[0].split(';').forEach(function(column) {
                headerRow += '<th>' + column.trim() + '</th>'; // Adiciona o cabeçalho das colunas com estilo laranja
            });
            headerRow += '</tr>';
            table.innerHTML += headerRow; // Adiciona a linha de cabeçalho à tabela
            for (var i = 1; i < lines.length; i++) {
                var newRow = '<tr>';
                lines[i].split(';').forEach(function(column) {
                    newRow += '<td>' + column.trim() + '</td>'; // Adiciona cada coluna como uma célula da linha
                });
                newRow += '</tr>';
                table.innerHTML += newRow; // Adiciona a linha à tabela
            }
        }

        // Chamar a função de carregar dados
        loadData();

        // Atualiza os dados a cada 30 segundos
        setInterval(loadData, 30000); // 30 segundos em milissegundos
    </script>
</body>
</html>
