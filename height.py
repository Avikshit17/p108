import pandas as pd
import random
import plotly.figure_factory as pf
df=pd.read_csv("data108.csv")
height=df["Height(Inches)"].tolist()
graph=pf.create_distplot([height],["Height"],show_hist=False)
graph.show()
