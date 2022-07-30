#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 20:27:27 2022

@author: laune
"""

import pandas as pd
import streamlit as st
import plotly.express as px

# Definindo um Data Frame
df = pd.read_csv('porto-itapoah-00.csv')

tipos = list(df['Circulante'].unique())
ativos = list(df['Ativo'].unique())

# Seletores
tipo = st.sidebar.selectbox('Escolha o tipo',['Todos']+tipos)
ativo = st.sidebar.selectbox('Escolha o ativo',['Todos']+ativos)

st.header('Porto de Itapoá')
st.subheader('Demonstrativo Financeiro')

# Filtra os dados se apenas um pais conforme selecionado
if(tipo != 'Todos'):
    df = df[df['Circulante'] == tipo]
    tipo_txt = tipo
else:
    tipo_txt = ''

# ... além disso, filtra a variante caso seja selecionada uma
if(ativo != 'Todos'):
    df = df[df['Ativo'] == ativo]
    ativo_txt = ativo
else:
    ativo_txt = 'todos os ativos'

fig_txt = 'Filtro: {} - {}'.format(tipo_txt,ativo_txt)

fig = px.line(df, x="Ano", y='Valor',hover_data={"Ano"},color='Ativo')
fig.update_layout(title=fig_txt )

st.plotly_chart(fig,use_container_width=True)
