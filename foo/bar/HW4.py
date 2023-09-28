import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("toy_dataset.csv")

st.write(df.head())
#1. Representation of Incomes based on gender in the cities
fig, x = plt.subplots()
df_income = df.groupby(["City", "Gender"]).Income.mean().unstack(0)
df_t = df_income.transpose() #.reset_index()
st.write(df_t)
#st.write(df_t.iloc[:,0])
#st.write(df_t.index.names)
st.write("############## -----")
st.write(type(list(df_t.index)))
#x.bar(df_t['City'], df_income.iloc[0])
#st.write(df_t.iloc[0], df_t.iloc[:,0])
#st.write(df_income['City'])
#x = df_t.plot.bar('City', ['Female','Male'])

#plt.bar(df_t['City'], df_t['Female'])
##plt.xlabel("City")
#plt.ylabel("Average Income")
#plt.title("Cities and respective avg incomes")
#plt.xticks(rotation=45, horizontalalignment='right' )
#st.pyplot(fig)

fig = plt.figure() # Create matplotlib figure

ax1 = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax1.twinx() # Create another axes that shares the same x-axis as ax.

width = 0.4

df_t.Female.plot(kind='bar', color='red', ax=ax1, width=width, position=1)
df_t.Male.plot(kind='bar', color='blue', ax=ax2, width=width, position=0)

ax1.set_ylabel('Female')
ax2.set_ylabel('Male')

st.pyplot(fig)
