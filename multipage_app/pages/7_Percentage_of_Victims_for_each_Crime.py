import altair as alt
import pandas as pd
from vega_datasets import data
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.subheader("Percentage of Victims of each Crime")
df2=pd.read_csv('../Data/CSV/Incidents_Offenses_Victims_and_Known Offenders_by Offense_Category_2021.csv')
fig_target = go.Figure(data=[go.Pie(labels=df2['Offense_Category'],
                            values=df2['Victims'],
                            hole=.3)])
fig_target.update_layout(showlegend=True,
                    height=400,
                    margin={'l': 20, 'r': 60, 't': 20, 'b': 0})
fig_target.update_traces(textposition='inside', textinfo='percent')
st.plotly_chart(fig_target)
