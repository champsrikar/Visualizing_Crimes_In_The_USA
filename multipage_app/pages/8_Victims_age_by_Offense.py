import altair as alt
import pandas as pd
from vega_datasets import data
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.subheader("Victims Age by Offense Category")
cols = ['Assault Offenses','Homicide Offenses','Human Trafficking Offenses','Kidnapping/Abduction','Sex Offenses',
        'Arson','Bribery','Burglary/Breaking & Entering','Counterfeiting/Forgery','Destruction/Damage/Vandalism',
        'Embezzlement','Extortion/Blackmail','Fraud Offenses','Larceny/Theft Offenses','Motor Vehicle Theft','Robbery',
        'Stolen Property Offenses']
      
op = st.multiselect('Which Offenses do you want to display?', cols,cols[12])

df3=pd.read_csv('../Data/CSV/Victims_Age_by_Offense_Category_2021.csv')
multi_line = alt.Chart(df3).transform_fold(op).mark_line().encode(
    x=alt.X('Age:O', title="Age"),
    y=alt.Y('value:Q', title="Number of Victims"),
    color='key:N').properties(
    title='Victims of Crimes by Age',
    width=700,
    height=450).interactive()
st.write(multi_line)
