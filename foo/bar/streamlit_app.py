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
# df.hist(column = 'Income')

gen_med = df.groupby(['City','Gender'])['Income'].mean().reset_index(name='count')
print(gen_med)
# creating the bar plot
plt.bar(gen_med['City'], gen_med['count'])#,width = 0.4)

plt.xlabel("Average Income Per City")
plt.ylabel("Average Income")
plt.title("City")
plt.xticks(rotation=45,horizontalalignment='right' )
#plt.xlabel('x_description', , x=1.0)
st.pyplot(plt)
