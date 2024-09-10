import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./taxa-cdi.csv')

grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
grafico.set_xticklabels(labels=df['hora'], rotation=90)

grafico.get_figure().savefig("grafico_cdi.png")