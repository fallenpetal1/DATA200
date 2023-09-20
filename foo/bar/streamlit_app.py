import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 
import numpy as np

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

df = pd.read_csv("https://raw.githubusercontent.com/fallenpetal1/DATA200/main/foo/bar/toy_dataset.csv")
# Extract only rows with Illness TRUE
rows_with_illness_true = df.loc[df['Illness'] == 'Yes']
# Plot showing ill people across cities
fig = rows_with_illness_true.City.value_counts().plot.bar()
a = np.random.normal(1, 1, size=50)
fig,x = plt.subplots()
plt.xticks(rotation=45)
# x.hist(a, bins=10)
st.pyplot(fig, clear_figure=None)
st.write("Test")
# fig = px.density_heatmap(
#    data_frame=df, y="age_new", x="marital"
# )


