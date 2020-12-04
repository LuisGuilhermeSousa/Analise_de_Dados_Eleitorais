# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd


# %%
dados_2012 = pd.read_csv('Dados/perfil_eleitorado_2012.csv', sep=';', encoding='latin-1')
dados_2014 = pd.read_csv('Dados/perfil_eleitorado_2014.csv', sep=';', encoding='utf-8')
dados_2016 = pd.read_csv('Dados/perfil_eleitorado_2016.csv', sep=';', encoding='utf-8')
dados_2018 = pd.read_csv('Dados/perfil_eleitorado_2018.csv', sep=';', encoding='latin-1')
dados_2020 = pd.read_csv('Dados/perfil_eleitorado_2020.csv', sep=';', encoding='latin-1')


# %%
dados_2012.head()


# %%
dados_2014.head()


# %%
dados_2016.head()


# %%
dados_2018.head()


# %%
dados_2020.head()


# %%
dados_2012.columns.values


# %%
dados_2020.columns.values


# %%
colunasSelecionadas = ['HH_GERACAO', 'SG_UF', 'NM_MUNICIPIO', 'CD_MUNICIPIO', 'NR_ZONA',
       'DS_GENERO', 'DS_FAIXA_ETARIA', 'DS_GRAU_ESCOLARIDADE',
       'QT_ELEITORES_PERFIL']


# %%
dados_2012_Selecionados = dados_2012.filter(items=colunasSelecionadas)


# %%
dados_2014_Selecionados = dados_2014.filter(items=colunasSelecionadas)


# %%
dados_2016_Selecionados = dados_2016.filter(items=colunasSelecionadas)


# %%
dados_2018_Selecionados = dados_2018.filter(items=colunasSelecionadas)


# %%
dados_2020_Selecionados = dados_2020.filter(items=colunasSelecionadas)


# %%
dados_2012_Selecionados.columns.values


# %%
dados_2018_Selecionados.columns.values


# %%
dados_2020_Selecionados.columns.values


# %%
dados_2018.columns


# %%
dados_2020_Selecionados


# %%
dados_2016_selecionados


# %%
dados_2016


# %%
dados_2020_Selecionados


# %%
teste = dados_2020_Selecionados.groupby('DS_GRAU_ESCOLARIDADE').size().sort_values()


# %%
teste


# %%
teste2 = dados_2020_Selecionados[dados_2020_Selecionados['DS_GRAU_ESCOLARIDADE'] == 'ENSINO MÉDIO COMPLETO']


# %%
teste2['QT_ELEITORES_PERFIL'].sum()


# %%
dataframes = [dados_2012_Selecionados, dados_2014_Selecionados, dados_2016_Selecionados, dados_2018_Selecionados, dados_2020_Selecionados]


# %%
dataframes


# %%
d2012 = {'NÃO INFORMADO':[],
'SUPERIOR INCOMPLETO':[],
'SUPERIOR COMPLETO':[],
'ENSINO MÉDIO INCOMPLETO':[],
'ANALFABETO':[],
'ENSINO FUNDAMENTAL COMPLETO':[],
'LÊ E ESCREVE':[],
'ENSINO MÉDIO COMPLETO':[],
'ENSINO FUNDAMENTAL INCOMPLETO':[]}


