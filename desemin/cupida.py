import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'category': ['A', 'A', 'A', 'A', 'B', 'B', 'B'],
    'value': [1, 2, 3, 100, 4, 5, 6]  // Outlier in category A
})

fig = px.box(df, x='category', y='value')
fig.show()
