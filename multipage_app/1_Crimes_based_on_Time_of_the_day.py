import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import altair as alt

st.set_page_config(
    page_title="Multipage App",
    page_icon="@",
)
st.title("Visualization of Crimes in The USA")
st.header("Time of Day")
st.subheader("Crime report of 2021")

time_person_2021 = pd.DataFrame(pd.read_excel("../Data/Crimes_Against_Persons_Incidents_Offense_Category_by_Time_of_Day_2021.xlsx"))



df_per_am = time_person_2021.iloc[2:14,:2]
df_per_pm = time_person_2021.iloc[15:,:2]

#Crimes that happen during A.M.
st.write(" ")
st.write(" ")
st.write("Bar chart for the accidents during A.M.")

st.bar_chart(data=df_per_am, x ='Time of Day', height = 600)

#Crimes that happen during P.M.


st.write("Bar chart for the accidents during P.M.")

st.bar_chart(data=df_per_pm, x ='Time of Day', height = 600)

# Crimes that happen during the entire day
st.write(" ")
st.write(" ")
st.subheader("Line Chart of crimes during the entire day")
df_am_pm = pd.concat([df_per_am, df_per_pm], axis=0)

# st.line_chart(df_am_pm, x = 'Time of Day', height=600)

fig, ax = plt.subplots(figsize=(17, 8))
df_am_pm.plot.line(x = 'Time of Day',ax=ax)
st.pyplot(fig)



st.write("Max criminal incidents reported at time: Midnight - 12:59am \n ")
st.write("Minimum criminal incidents reported at time 5am to 5:59am")



#Pie Chart
st.write(" ")
st.write(" ")
st.subheader("Pie Chart of the types of Crimes")
max_df = time_person_2021.loc[time_person_2021['Time of Day'] == 'Midnight - 12:59 a.m.']

data = max_df.iloc[0, 2:].to_numpy()

max_df = {'Type': ['Assault Offenses', 'Homicide Offenses', 'Human Trafficking Offenses', 'Kidnapping/Abduction', 'Sex Offenses'],
      'Total Incidents': max_df.iloc[0, 2:].to_numpy()}
max_df = pd.DataFrame(data=max_df)


sizes = max_df['Total Incidents']
labels = ['Assault Offenses', 'Homicide Offenses', 'Human Trafficking Offenses', 'Kidnapping/Abduction', 'Sex Offenses']

fig1, ax1 = plt.subplots(figsize=(6, 5))
fig1.subplots_adjust(0.3,0,1,1)

theme = plt.get_cmap('bwr')
ax1.set_prop_cycle("color", [theme(1. * i / len(sizes)) for i in range(len(sizes))])

ax1.pie(sizes, startangle=90)

ax1.axis('equal')

total = sum(sizes)
plt.legend(
    loc='upper left',
    labels=['%s, %1.1f%%' % (
        l, (float(s) / total) * 100) for l, s in zip(labels, sizes)],
    prop={'size': 10},
    bbox_to_anchor=(0.0, 1.2),
    bbox_transform=fig1.transFigure
)

st.pyplot(fig1)