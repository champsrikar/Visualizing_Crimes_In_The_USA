import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
from wordcloud import WordCloud, STOPWORDS


st.title("Location")
location_2021 = pd.DataFrame(pd.read_excel("../Data/Crimes_Against_Persons_Offenses_Offense_Category_by_Location_2021.xlsx"))



# Sorting the dataframe by Total Offences
final_df = location_2021.sort_values(by=['Total Offenses'], ascending=False)

# Top locations with high total offenses
top20k = final_df.loc[final_df['Total Offenses'] >= 20000]



comment_words = ''
stopwords = set(STOPWORDS)
 
# iterate through the csv file
for val in top20k['Location'].values:
     
    # typecaste each val to string
    val = str(val)
 
    # split the value
    tokens = val.split()
     
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
    comment_words += " ".join(tokens)+" "


st.subheader("Word Cloud of the crime locations")
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)
 
# plot the WordCloud image                      
fig1 = plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
st.pyplot(fig1)