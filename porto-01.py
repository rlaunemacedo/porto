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
# dfcirc = pd.read_csv('porto-itapoah-00.csv').query("Circulante == 'Ativo circulante'")
df = pd.read_csv('porto-itapoah-00.csv')

st.header('Porto de Itapoá')
st.subheader('Demonstrativo Financeiro (em milhares de reais - R$)')
st.sidebar.header('Dicas:')
st.sidebar.subheader('1. Para ver um ativo em particular, na legenda, dê um clique duplo;')
st.sidebar.subheader('2. Para esconder um ativo em particular, na legenda, dê um clique simples;')

dfcirc = df[df['Circulante'] == 'Ativo circulante']
dfncirc = df[df['Circulante'] != 'Ativo circulante']

fig1 = px.line(dfcirc, x="Ano", y='Valor',hover_data={"Ano"}, 
               color='Ativo',line_shape="spline")
fig1.update_xaxes(dtick=1)
fig1.update_layout(title='Circulante')

fig2 = px.line(dfncirc, x="Ano", y='Valor',hover_data={"Ano"},color='Ativo',line_shape="spline")
fig2.update_xaxes(dtick=1)
fig2.update_layout(title='Não circulante')

st.plotly_chart(fig1,use_container_width=True)
st.plotly_chart(fig2,use_container_width=True)
