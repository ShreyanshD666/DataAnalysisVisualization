import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv("level vs attempt.csv")

Mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

fig = px.scatter(Mean, x = "student_id", y = "level", size = "attempt", color = "attempt")
fig.show()

