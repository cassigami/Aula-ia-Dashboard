import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("BancodeDadosA3_2023.csv", sep=",", decimal=",")

header_style = """
    <style>
        .header {
            background-color: #87CEEB;
            padding: 10px;
            color: white;
            text-align: center;
            font-size: 24px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
    </style>
"""

st.markdown(header_style, unsafe_allow_html=True)
st.markdown('<div class="header">Análise de Diagnósticos com os Dados Fornecidos pela Turma de Veterinária</div>', unsafe_allow_html=True)

counts = df['Diagnóstico'].value_counts()
df_counts = pd.DataFrame({'Diagnóstico': counts.index, 'Quantidade': counts.values})
fig_bar = px.bar(df_counts, x='Diagnóstico', y='Quantidade', labels={'Diagnóstico': 'Diagnóstico', 'Quantidade': 'Quantidade'})
fig_bar.update_layout(title='Quantidade de pacientes por diagnóstico')
st.plotly_chart(fig_bar)

col_parameter = st.selectbox("Escolha a coluna para análise:", df.columns)
line_parameter = st.checkbox("Mostrar Linha de Diagnóstico?", value=True)

fig_scatter = px.scatter(df, x=col_parameter, y='Diagnóstico', color='Diagnóstico' if line_parameter else None)
fig_scatter.update_layout(title=f"{col_parameter} vs Diagnóstico", xaxis_title=col_parameter, yaxis_title='Diagnóstico')

fig_scatter.update_layout(showlegend=False)

st.plotly_chart(fig_scatter)

fig_hist = px.histogram(df, x=col_parameter, title=f'Distribuição de {col_parameter}', nbins=15)
st.plotly_chart(fig_hist)

x_variable = st.selectbox("Escolha a variável para o eixo X:", df.columns, key='x_variable')
y_variable = st.selectbox("Escolha a variável para o eixo Y:", df.columns, key='y_variable')

fig_scatter_2 = px.scatter(data_frame=df, x=x_variable, y=y_variable)
fig_scatter_2.update_layout(title='Relação entre Covariáveis (Gráfico de dispersão)')
st.plotly_chart(fig_scatter_2)


diagnosis_options = df['Diagnóstico'].unique()
filter_table = st.selectbox("Escolha o diagnóstico para análise:", diagnosis_options)

st.markdown("### Tabela de Dados")
filtered_df = df.loc[df['Diagnóstico'] == filter_table]
st.dataframe(filtered_df.head(5), height=150)

if len(filtered_df) > 5:
    st.markdown(f"*Mostrando apenas 5 de {len(filtered_df)} linhas. Utilize a barra de rolagem para ver mais.*")