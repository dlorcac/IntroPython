import pandas as pd 

df = pd.read_csv("athlete_events.csv")
#df = pd.read_csv(r'C:\Users\david\ws-desafiolatam\IntroPython\desafio8\athlete_events.csv')

ejercicio_1 = df.shape  # (271116, 15)
ejercicio_2 = df['Games'].nunique()   #51

vSummer = df[df['Season'] == 'Summer'].Year.min()
ejercicio_4=df[df['Year']==vSummer]['City'].unique()

vWinter = df[df['Season'] == 'Winter'].Year.min()
ejercicio_5=df[df['Year']==vWinter]['City'].unique()

ejercicio_6 el equipo, poner ojo

ejercicio_7, funcion de porcentaje

ejercicio_8, usar el min