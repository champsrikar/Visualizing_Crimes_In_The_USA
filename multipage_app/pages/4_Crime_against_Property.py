import altair as alt
import pandas as pd
from vega_datasets import data
import streamlit as st

state = alt.topo_feature(data.us_10m.url, feature='states')
click=alt.selection_single(empty='all', fields=['State_Abv'])

df=pd.read_csv('../Data/CSV/Crime_Against_Property.csv')
st.subheader('Crime_Against_Property')

      
df_group=df.groupby(['State_Code','State_Abv'])['Total_Offenses'].sum().reset_index()
ch_map=alt.Chart(state).mark_geoshape().encode(
    color=alt.condition(
    click,'Total_Offenses:Q',alt.value('lightgray')),
    tooltip=['State_Abv:O', 'Total_Offenses:Q']
).add_selection(
click).transform_lookup(lookup='id',from_=alt.LookupData(
    df_group, 'State_Code',['Total_Offenses', 'State_Abv'])
).project(
type='albersUsa'
).properties(height = 700, width = 500)

bar_chart = alt.Chart(df).mark_bar().encode(
y=alt.Y('Total_Offenses:Q',title='Total Offenses'),
x=alt.X('Offense_Type:N',sort='-y',title='Offense Type')).transform_filter(click
).transform_aggregate(Total_Offenses='sum(Total_Offenses)',groupby=["Offense_Type"]
).properties(height=400, width = 400)
st.write(alt.hconcat(ch_map, bar_chart))