import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df, x="student_id", y="level",color="attempt",
                    size_max=60)
fig.show()

print(df.groupby('level')['attempt'].mean())

fig = go.Figure(go.Scatter(x=df.groupby('level')['attempt'].mean(),
                           y=['Level 1','Level 2','Level 3','Level 4'],
                           orientation='h'))
fig.show()