
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

NOME_ARQUIVO_FONTE = 'gasolina.csv'
df = pd.read_csv(NOME_ARQUIVO_FONTE)

altura = 15 / 2.54
largura = 15 / 2.54

with sns.axes_style('whitegrid'):
    plt.figure(figsize=(largura, altura))
    graph = sns.lineplot(data=df, x="dia", y="venda", palette="pastel")
    graph.set(title="Preço / dia", xlabel='Dia', ylabel='Preço')

plt.gcf().set_size_inches(w=largura, h=altura)
plt.gcf().savefig(fname='gasolina.png', bbox_inches='tight')
plt.close()
