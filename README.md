# Análise sobre o nível de escolaride dos eleitores nas eleições de 2020

* Trabalho realizador por [Luis Guilherme](https://github.com/LuisGuilhermeSousa) e [Matheus Campos](https://github.com/MatheusCampos-450)

Neste trabalho temos como principal objetivo fazer uma análise sobre o perfil do eleitor no ano de 2020, tendo em vista o seu nível de escolaridade. 
Tomamos como base os índices do Brasil como um todo e de algumas das principais cidades do país, como São Paulo, Rio de Janeiro, Fortaleza, Belo Horizonte e Maceió. 
Com relação ao nível de escolaridade, separamos os pelos seguintes níveis:
* Analfabeto
* Lê e Escreve
* Ensino Fundamental Incompleto
* Ensino Fundamental Completo
* Ensino Médio Incompleto
* Ensino Médio Completo
* Superior Incpmpleto
* Superior Completo

### Sobre a Análise
A análise foi feita utilizando os dados fornecidos no portal do [Tribunal Superior ELeitoral](https://www.tse.jus.br/eleicoes/estatisticas/repositorio-de-dados-eleitorais-1/repositorio-de-dados-eleitorais) e foram feitos com base nos dados de 2020.
Com relação ás tecnologias utilizadas, nós usamos o Python 3.8 junto com as biblioteca [Pandas](https://github.com/pandas-dev/pandas), para leitura e limpeza dos dados, e a 
biblioteca [Matplotlib](https://github.com/matplotlib/matplotlib) para a geração dos gráficos que serão apresentados.

### Resultados Obtídos
#### Grau de escolaridade dos eleitores brasileiros
Primeiramente fizemos uma análise sobre o nível de escolaridade do eleitor brasileiro em geral e podemos ver que a maioria dos eleitores completou o Ensino Médio, 
porém uma parcela grande não completou ao menos o Ensino Fundamental. O que surpreende é o fato de a quantidade de pessoas que iniciaram uma Faculdade ser maior que o número de pessoas analfabetas.
![brasileiros](https://user-images.githubusercontent.com/56441318/101294411-ea28f500-37f5-11eb-96c5-96a97f0e4065.png)

#### Municípios com o maior número de eleitores Analfabetos
Neste gráfico podemos ver que este índice acompanha a população da determinada cidade, sendo proporcional a ela, onde a cidade de São Paulo aparece disparada como a que possui a 
maior quantidade de eleitores Analfabetos. Isso se deve ao fato dela ser a cidade mais populosa do país e assim, possuindo o a maior parcela do eleitorado analfabeto.
![analfabetos](https://user-images.githubusercontent.com/56441318/101294473-3bd17f80-37f6-11eb-900a-22d78a6bdfa6.png)

#### Grau de escolaridade na cidade de São Paulo - SP
O perfil do eleitor paulista segue bastante a linha do eleitor brasileiro como um todo, onde a grande maioria completou Ensino Médio Completo e outras duas parcelas não completaram nem o Ensino Médio e nem o Ensino Fundametal.
O que chama atenção é que entre os que tentaram uma faculdade, a grande maioria conseguiu concluir os estudos no terceiro grau.
![sao paulo](https://user-images.githubusercontent.com/56441318/101294554-d5992c80-37f6-11eb-9ea3-d5560cad6f6c.png)


#### Grau de escolaridade na cidade do Rio de Janeiro - RJ
O eleitor carioca se destaca pelo fato do número de pessoas que não completaram o Ensino Médio ser maior que o número de pessoas que se formaram no segundo grau. Já com relação ao
Ensino Fundamental e Superior, esses índices manteram a média nacional.
![rio de janeiro](https://user-images.githubusercontent.com/56441318/101294634-84d60380-37f7-11eb-9eea-5c48ce483a38.png)

#### Grau de escolaridade na cidade de Fortaleza - CE
Os índices de Fortaleza se manteram semelhantes com os de São Paulo e Rio de Janeiro, com destaque ao percentual menor de eleitores que não concluíram o Ensino Médio e mantendo a 
maioria dos eleitores formados no segundo grau.
![fortaleza](https://user-images.githubusercontent.com/56441318/101294738-4856d780-37f8-11eb-9e0c-64ae6fa53cc1.png)

#### Grau de escolaridade na cidade de Belo Horizonte - MG
O destaque do eleitor mineiro é o índice de eleitores formados na fauldade ser ligeiramente maior quando comparado ás demais cidades citadas. Os outros índices se materam na média 
do Brasil.
![belo horizonte](https://user-images.githubusercontent.com/56441318/101294868-ef3b7380-37f8-11eb-8f09-b5c9f0d8fc07.png)

#### Grau de escolaridade na cidade de Maceió - AL
O eleitor de Maceió segue o perfil brasileiro, com leves diferenças nos níveis de Ensino Médio Incompleto ser inferior à média e Superior Incompleto ser levemente maior quando comparado
ao país como um todo.
![maceio](https://user-images.githubusercontent.com/56441318/101294934-3d507700-37f9-11eb-9c52-4369c537607b.png)


#### [Link para a análise feita](https://github.com/LuisGuilhermeSousa/Analise_de_Dados_Eleitorais/blob/main/analise_dados_eleitorais.ipynb)

