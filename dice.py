import random
import plotly.figure_factory as pf
num=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    sum=dice1+dice2
    num.append(sum)
graph=pf.create_distplot([num],["dice number"],show_hist=False)
graph.show()
