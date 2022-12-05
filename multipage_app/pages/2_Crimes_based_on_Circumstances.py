import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import altair as alt

st.title("Circumstances of the different Crimes")

circumstance_2021 = pd.DataFrame(pd.read_excel("../Data/Murder_and_Nonnegligent_Manslaughter_and_Aggravated_Assault_Victims_Off_Type_by_Circumst_2021.xlsx"))


circumstance_2021.fillna(0)



# Bar Chart for Aggravted assaults and Murder and Manslaughter
st.write(" ")
st.write(" ")
st.write("Bar chart comparing Aggravated assaults with Murder and Manslaughter")
fig, ax = plt.subplots()
circumstance_2021.plot.bar(x = 'Circumstance', y=['Murder and\nNonnegligent\nManslaughter','Aggravated\nAssault'],ax=ax)
st.pyplot(fig)
st.write("Aggravated assault is the most common type of offence in all circumstance")
# Pie chart
st.write(" ")
st.write(" ")
st.write("Pie Chart for the types of Crimes committed")
sizes = circumstance_2021['Total\nVictims'].iloc[:9]
labels = circumstance_2021['Circumstance'].iloc[:9].to_numpy()

fig1, ax1 = plt.subplots(figsize=(6, 5))
fig1.subplots_adjust(0.3,0,1,1)

theme = plt.get_cmap('jet')
ax1.set_prop_cycle("color", [theme(1. * i / len(sizes)) for i in range(len(sizes))])

_, _ = ax1.pie(sizes, startangle=90)

ax1.axis('equal')

total = sum(sizes)
plt.legend(
    loc='upper left',
    labels=['%s, %1.1f%%' % (
        l, (float(s) / total) * 100) for l, s in zip(labels, sizes)],
    prop={'size': 10},
    bbox_to_anchor=(0.0, 1.3),
    bbox_transform=fig1.transFigure
)

st.pyplot(fig1)
st.write("51.9% of times arguments has led to Murder or Aggravated assault")

