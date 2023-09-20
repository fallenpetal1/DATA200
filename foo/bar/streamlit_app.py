import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

df = pd.read_csv("toy_dataset.csv")
# Plot showing ill people across cities
st.write(rows_with_illness_true.City.value_counts().plot.bar())
