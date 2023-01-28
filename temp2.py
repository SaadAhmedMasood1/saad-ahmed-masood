# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:48:13 2023

@author: HP
"""

import pandas as pd
import streamlit as st

file = r'C:\Users\HP\Desktop\Karachi AI\Karachi AI (office PC)\Class\2nd day\Data Manipulation and Summary Analytics\Billionaire.csv'

st.header('Billionaires datasets')



df = pd.read_csv(file)
#df = pd.read_csv('Billionair')


# find count of billionaire by countries
#df.groupby('Country')['Name'].count().sort_values()

# find the most popular source of income

#df.groupby('Source')['Name'].count().sort_values(ascending=False).head(1)
# Get the cumulative wealth of billionaire belonging to US

#import pandas as pd

# Assuming your data is in a DataFrame called 'billionaires'
#df['NetWorth'] = df['NetWorth'].apply(lambda x: float(x.replace('$', '').replace(' B', '')))
#us_billionaires = df[df['Country'] == 'United States']
#us_cumulative_wealth = us_billionaires['NetWorth'].cumsum()
#print("Cumulative wealth of billionaires belonging to US: ", us_cumulative_wealth)





#===========================================================
#all_countries = df['Country'].unique()

#selection = st.selectbox('Select Country',all_countries)

#subset = df[df['Country'] == selection]

#st.dataframe(subset)


df['NetWorth'] = df['NetWorth'].apply(lambda x: float(x.replace('$', '').replace(' B', '')))
all_countries = sorted(df['Country'].unique())
col1 , col2 = st.columns(2)

#display on streamlit

selected_country= col1.selectbox('Select Your Country', all_countries)
#subset on selected country
subset_country = df[df['Country'] == selected_country]

#get unique source from the selected country
source = sorted(subset_country['Source'].unique())
#display multi select option on source
selected_source = col1.multiselect('Select source of income', source)
#subset on selected source
selected_source = subset_country[subset_country['Source'].isin(selected_source)]
#
subset_source = subset_country[subset_country['Source'] == selected_source]

#column 2
main_string = '{} - Billionaires'.format(selected_country)
#main_string = selected_country + ' - Billionaires'
col2.header(main_string)
col2.table(subset_country)
col2.header('source wise info')
col2.dataframe(subset_source)
