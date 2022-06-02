import pandas as pd 


df1 = pd.read_csv ('dataset/agris_1.csv', sep=';')
df2 = pd.read_csv ('dataset/agris_2.csv', sep=';')
df3 = pd.read_csv ('dataset/agris_3.csv', sep=';')
df4 = pd.read_csv ('dataset/agris_4.csv', sep=';')
df5 = pd.read_csv ('dataset/agris_5.csv', sep=';')
df6 = pd.read_csv ('dataset/agris_6.csv', sep=';')
df7 = pd.read_csv ('dataset/agris_7.csv', sep=';')
df8 = pd.read_csv ('dataset/agris_8.csv', sep=';')
df9 = pd.read_csv ('dataset/faodocrep_1.csv', sep=';')
df10 = pd.read_csv ('dataset/faodocrep_2.csv', sep=';')
df11 = pd.read_csv ('dataset/faodocrep_3.csv', sep=';')
df9 = df9[['Abstract/Description','Themes']]
df10 = df10[['Abstract/Description','Themes']]
df11 = df11[['Abstract/Description','Themes']]


df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8,df9,df10,df11], ignore_index=True, sort=False)

df = df[['Abstract/Description', 'Themes']]

df[['Themes0', 'Themes_1','Themes_2','Themes_3']] = df['Themes'].str.split(';', expand=True)

dataset = df[['Themes0', 'Abstract/Description']].dropna()
dataset['Themes0'] = dataset['Themes0'].str.replace(' ','_')
dataset['Themes0'] = '__label__' + dataset['Themes0'].astype(str)

print(dataset)


stat_themes = df.groupby(['Themes0']).size().reset_index(name='counts')

print(stat_themes)
dataset.to_csv('stat_themes.txt',sep = ' ',  index=False, encoding="utf-8")