import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt


busy_hour_df = pd.read_csv('dashboard/busy_hour.csv')
cnt_bytemp_df = pd.read_csv('dashboard/cnt_bytemp.csv')
user_monthly_df = pd.read_csv('dashboard/user_monthly.csv')

st.title('Analysis Data Project')
st.write('''Addin Hadi Rizal - m312b4ky0071@bangkit.academy''')

''''''
st.subheader('Question 1')
st.write(
    '''
        When is the busiest time of people rode bicycle on workingday?
    '''
)

busy_hour_df['hr'] = busy_hour_df['hr'].astype(str)
chart = alt.Chart(busy_hour_df).mark_bar().encode(
    x=alt.X('hr', title='Hour of the Day', sort=None),
    y=alt.Y('cnt', title='Count')
).properties(
    title='Average Usage of the Bicycle by Hour'
)

st.altair_chart(chart, use_container_width=True)

st.write(
    '''
        From the graph, we can see that most of people rode bicycle on workingday at 5 PM.
    '''
)

''''''
st.subheader('Question 2')
st.write(
    '''
        Does temperature affect the amount of user that used bicycle?
    '''
)

chart = alt.Chart(cnt_bytemp_df).mark_bar().encode(
    x=alt.X('Category', sort=None),
    y=alt.Y('Count')
).properties(
    title='Rate of Bicycle Usage Based on Heat Index'
)
st.altair_chart(chart, use_container_width=True)

st.write(
    '''
        From the graph, we can see that the number of people who rode bicycles decreased as the temperature increased. Therefore, we can conclude that the heat index affects the usage rate of bicycles.
    '''
)

''''''
st.subheader('Question 3')
st.write(
    '''
        When is the busiest time of people rode bicycle on workingday?
    '''
)

user_monthly_long = user_monthly_df.melt(id_vars='month', value_vars=['registered', 'casual'], var_name='user_type', value_name='count')

chart = alt.Chart(user_monthly_long).mark_line().encode(
    x=alt.X('month', title="Month in a Year", sort=None),
    y=alt.Y('count', title="User Count"),
    color='user_type:N'
).properties(
    title='Growth Rate of Registered and Casual Users'
)

st.altair_chart(chart, use_container_width=True)

st.write(
    '''
        From the graph, we can see that bicycle usage, both by casual and registered users, increased from January to June. For the next two months, the usage remained relatively stable. However, starting in September, there was a decline until December. The growth between registered and casual user was growing linear, so both of them was not affect each other.
    '''
)
