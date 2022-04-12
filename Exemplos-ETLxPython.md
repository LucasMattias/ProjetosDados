# Para esses exemplos importei a biblioteca "pandas" e atribui o apelido de "pd"

## -Realiza a Extração de dados ja transformando em nulo os valores ausentes na minha tabela.

+ ##### A variável 'missing_values' foi criada para armazenar-mos os valores que devem ser nulos na nossa tabela.

+ ##### Foi criada a variável "df" para guardarmos um dataframe com a leitura do arquivo csv.
  
  ## Parâmetros:
  
  * ##### O primeiro é o nome do arquivo que sera consultado (Se o arquivo estiver na mesma pasta da sua aplicação .py não é necessario que você informe o caminho, caso contrario, o caminho é requerido)
  
  * ##### 'sep=' informa o elemento de separação dos campos da tabela, neste caso foi o ';'.
  
  * ##### 'parse_dates' informa os campos que são do formato data.
  
  * ##### 'dayfirst' informa que o primeiro campo da data é o dia do mes.
  
  * ##### 'na_values' aponta os valores nulos, nesse caso temos eles guardados na variavel 'missing_values'.

            `missing_values = ['*****', '****', '###!', '####', '00:00:00']`  
            `df = pd.read_csv('ocorrencia.csv', sep=';', parse_dates=['ocorrencia_dia'], dayfirst= True, na_values=valores_ausentes)` 

## -Criação de uma variavel para filtro, trazendo a cidade e o estado das ocorrências com mais de 5 recomendações .

+ #### A função 'loc' é usada para puxar dados do documento, o primeiro campo dentro dos colchetes informa as linhas que devem ser trazidas, na segunda parte depois da virgula é informado as colunas que devem ser retornadas.

        `filter = df.total_recomendacoes > 5`   
        `print(df.loc[filtro, ['ocorrencia_cidade', 'ocorrencia_uf']])`

## -Conta o total de ocorrências em MANAUS e mostra apenas a cidade.

+ #### A função count conta quantas linhas retornaram na sua query.

        print(df.loc[df.ocorrencia_cidade == 'MANAUS', 'ocorrencia_cidade'].count())

## -Mostra a cidade, o codigo da ocorrência e o total de recomendações de todas ocorrências que aconteceram no município de PARATY.

        `print(df.loc[df.ocorrencia_cidade == 'PARATY', ['ocorrencia_cidade', 'codigo_ocorrencia', 'total_recomendacoes']])`

## -Realiza dois filtros, sendo um deles na cidade do RIO DE JANEIRO e o outro nas classificações ACIDENTES e INCIDENTE usando os operadores lógicos '&' e '|' .

+ #### O operador lógico '&' é equivalente a 'E', obrigando a aplicação a retornar apenas os valores onde a cidade da ocorrência seja 'RIO DE JANEIRO'.

+ #### Ja o '|' é equivalente a 'OU', trazendo as ocorrencias no RIO DE JANEIRO onde a classificação da ocorrência seja 'ACIDENTE' ou 'INCIDENTE'.

        `print(df.loc[(df.ocorrencia_cidade == 'RIO DE JANEIRO') & ((df.ocorrencia_classificacao == 'ACIDENTE') |`         `(df.ocorrencia_classificacao == 'INCIDENTE') ), ['ocorrencia_cidade', 'ocorrencia_classificacao']])`  

## -É realizado dois filtros, sendo um deles em cidade e outro na classificação da ocorrência, utilizando o .isin.

+ #### Semelhante ao exemplo anterior, é utilizado o operador lógico '&' para agregar a query, porém, substituindo o operador lógico '|' temos a função '.isin', para determinar os valores aceitáveis para a coluna 'ocorrencia_classificacao'.

         `print(df.loc[(df.ocorrencia_cidade == 'RIO DE JANEIRO') & (df.ocorrencia_classificacao.isin(['ACIDENTE', 'INCIDENTE'])), ['ocorrencia_cidade', 'ocorrencia_classificacao']])`

## -Filtra todas cidades que começãm com a letra C .

+ #### Na variável 'filter' informamos que devemos retornar apenas cidades onde o indice '0' da string contenha a letra 'C'.
  
     `filter = df.ocorrencia_cidade.str[0] == 'C' ` 
     `print(df.loc[filtro, ['ocorrencia_cidade', 'ocorrencia_uf', 'codigo_ocorrencia']])`

## -Filtra todas cidades que começãm com a letra A .

+ #### Na variável 'filter' informamos que devemos retornar apenas cidades onde o indice '-1' (ou seja, o último) da string contenha a letra 'A'.

        `filter = df.ocorrencia_cidade.str[-1] == 'A'  `
        `print(df.loc[filtro, ['ocorrencia_cidade', 'ocorrencia_uf', 'codigo_ocorrencia']])` 

## -Filtra todas cidades que contém 'MA'.

+ #### A funcão '.str.contains' retorna os campos que possuem em qualquer posição a string entre parênteses, nesse caso a sílaba 'MA'.

        `filtro = df.ocorrencia_cidade.str.contains('MA') ` 
        `print(df.loc[filtro, ['ocorrencia_cidade', 'ocorrencia_uf', 'codigo_ocorrencia']])`

## -Filtra todas cidades que contém 'MA' ou 'AL'.

+ #### Nesse caso é requisitado duas sequencias de caractéres, fazendo um 'OU' com auxílio do '|'.

        `filtro = df.ocorrencia_cidade.str.contains('MA|AL')  `
        `print(df.loc[filtro, ['ocorrencia_cidade', 'ocorrencia_uf', 'codigo_ocorrencia']]) ` 

## -Filtra todas ocorrencias que aconteceram no ano da ocorrencia de menor periodo.

+ #### A variável 'filter' traz o ano que seja igual ao menor ano de ocorrência na tabela, logo após ele é usado para trazer na tabela apenas as ocorrencias que aconteceram naquele ano.

        `filter = df.ocorrencia_dia.dt.year == df.ocorrencia_dia.dt.year.min() ` 
        `print(df.loc[filtro, ['ocorrencia_dia', 'ocorrencia_cidade']])`

## -Filtra todas ocorrencias que aconteceram no ano de 2015.

+ #### A variável 'filter' traz todas ocorrencias que aconteceram noa no de 2015.

        `filter = df.ocorrencia_dia.dt.year == 2015  `
        `print(df.loc[filtro, ['ocorrencia_dia', 'ocorrencia_cidade']])`

### -Filtra todas ocorrencias que aconteceram no ano de 2015 e no mês 12.

+ #### Os filtros aplicados aqui trazem apenas as ocorrências que aconteceram no mes 12 do ano de 2015.

       `filtro = df.ocorrencia_dia.dt.year == 2015`  

       `filtro1 = df.ocorrencia_dia.dt.month == 12 ` 
       `print(df.loc[filtro & filtro1, ['ocorrencia_dia', 'ocorrencia_cidade']])`

### -Filtra todas ocorrencias que aconteceram em um período.

+ #### Nessa query é aplicado dois filtro fixos para ano e mes, os filtros de dia trazem todas as ocorrencias dentro de um periodo, nesse caso entre os dias 3 e 15.

        `filtro = df.ocorrencia_dia.dt.year == 2015`  
        `filtro1 = df.ocorrencia_dia.dt.month == 12`  
        `filtro_dia_inicio = df.ocorrencia_dia.dt.day > 3`  
        `filtro_dia_fim = df.ocorrencia_dia.dt.day < 15 ` 
        `print(df.loc[filtro & filtro1 & filtro_dia_inicio & filtro_dia_fim, ['ocorrencia_dia', 'ocorrencia_cidade']]) `

### -Une dois campos DIA e HORA, transformando em DateTime.

+ #### É inserido uma nova coluna 'ocorrencia_dia_hora' na tabela, contendo a junção dos de data e de hora.

        `df['ocorrencia_dia_hora'] = pd.to_datetime(df.ocorrencia_dia.astype(str) + ' ' + df.ocorrencia_hora)  
        print(df.loc[:, 'ocorrencia_dia_hora'])`

### -Filtra um período de tempo em formato DateTime.

+ #### Além de unir os campos dia e hora, é criado dois filtros para definir um periodo para a análise.

        `df['ocorrencia_dia_hora'] = pd.to_datetime(df.ocorrencia_dia.astype(str) + ' ' + df.ocorrencia_hora)`  
        `filtro_inicio = df.ocorrencia_dia_hora >= '2012-01-05 21:00:00'`  
        `filtro_fim = df.ocorrencia_dia_hora <= '2012-01-08 21:00:00'`  
        `print(df.loc[filtro_inicio & filtro_fim, 'ocorrencia_dia_hora'])`

## -Filtro é guardado dentro de uma variável.

+ #### Foi salvo dentro de um novo DataFrame os filtros de ano e de mes (2015 e 12 respectivamente), logo após foi agrupado os codigos de occorencia por classificação.

        `filtro = df.ocorrencia_dia.dt.year == 2015`  
        `filtro1 = df.ocorrencia_dia.dt.month == 12`  
        `df201512 = df.loc[filtro & filtro1]`  
        `print(df201512.groupby('ocorrencia_classificacao').codigo_ocorrencia.count())`

## -Filtra uma região em um período de tempo.

+ #### São feitos dois filtros, um para selecionar os estados que compõem a região sudeste e outro para apenas considerar as ocorrências que aconteceram no ano de 2015, apresentando-os de forma agrupada por cidade, fazendo um ranking decrescente, da cidade com mais ocorrência para a com cidade menos ocorrências.

        `filtro1 = df.ocorrencia_uf.isin(['RJ', 'SP', 'ES', 'MG'])`  
        `filtro2 = df.ocorrencia_dia.dt.year == 2015`  
        `dfSudeste2015 = df.loc[filtro1 & filtro2]`  
        `print(dfSudeste2015.groupby('ocorrencia_cidade').codigo_ocorrencia.count().sort_values(ascending=False))`

## - Filtra uma região e um periodo de tempo, realizando após um agrupamento duplo.

+ #### Da mesma forma do exemplo anterior, são feitos dois filtros, mas agora ocorre um agrupamento duplo, informando uma lista dentro do groupby, para que possamos informar duas colunas.

    `filtro1 = df.ocorrencia_uf.isin(['RJ', 'SP', 'ES', 'MG'])`  
    `filtro2 = df.ocorrencia_dia.dt.year == 2015`  
    `dfSudeste2015 = df.loc[filtro1 & filtro2]`  
    `print(dfSudeste2015.groupby(['ocorrencia_classificacao', 'ocorrencia_uf']).codigo_ocorrencia.count())`



<u>**Espero ter te ajudado de alguma forma com esses exemplos, aceito qualquer sugestão de melhoria!**</u>

escrito por *Lucas* **Mattias**


