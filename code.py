import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("phone.csv")
rating = df["Mobile Brand"].tolist()
brand = df["Avg Rating"].tolist()

figure = ff.create_distplot([brand],["rating of different brand"],show_hist=False)

figure.show()
