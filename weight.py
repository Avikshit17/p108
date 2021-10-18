import pandas as pd
import plotly.figure_factory as pf
df=pd.read_csv("data108.csv")
weight=df["Weight(Pounds)"].tolist()
graph=pf.create_distplot([weight],["Weight"],show_hist=False)
graph.show()