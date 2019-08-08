import pandas as pd 

#df = pd.read_csv("athlete_events.csv")
df = pd.read_csv(r'C:\Users\david\ws-desafiolatam\IntroPython\desafio8\athlete_events.csv')

ejercicio_1 = df.shape  # (271116, 15)

ejercicio_2 = df['Event'].nunique()   #765