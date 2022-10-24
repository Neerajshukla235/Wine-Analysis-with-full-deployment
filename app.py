import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

import helper
import preprocessor,helper

df=preprocessor.preprocess()


st.sidebar.image('https://img.freepik.com/free-vector/realistic-set-with-bottle-red-wine-four-drinking-glasses'
                 '-filled-with-drink_1284-32449.jpg?w=360')

st.sidebar.title("Global Wine Analysis")
user_menu=st.sidebar.radio(
    'Select an Option',
    ('Overall Analysis','Production Tally','Price Tally' )

)
#st.dataframe(df)


if user_menu== 'Production Tally':
    st.sidebar.header("Production Tally")
    years,country =helper.country_year_list(df)

    selected_Year= st.sidebar.selectbox("Select Years",years)
    selected_country = st.sidebar.selectbox("Select Country",country)
    production_tally=helper.fetch_production_tally(df,selected_Year,selected_country)
    if selected_Year=='Overall' and selected_country=='Overall':
        st.title("Overall Production ")
    if selected_Year != 'Overall' and selected_country == 'Overall':
        st.title("Production  of wine in - " + str(selected_Year))
    if selected_Year == 'Overall' and selected_country != 'Overall':
        st.title("Production of wine in - " + str(selected_country))
    if selected_Year != 'Overall' and selected_country != 'Overall':
        st.title("Production of wine of - "  + selected_country + " in " +  str(selected_Year) )

    hide_dataframe_row_index = """
                <style>
                .row_heading.level0 {display:none}
                .blank {display:none}
                </style>
                """
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)


    st.table(production_tally)

if user_menu == 'Overall Analysis':
    harvesting = int(df['HarvestedAcres'].max())
    Yield  = int(df['Yield(Unit/Acre)'].mean())
    production= int(df['Production'].mean())
    price= df['Price(Dollars/Unit)'].max()
    value= int(df['Value(Dollars)'].mean())


    st.title("TOP STATTISTICS")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Maximum Harvesting")
        st.title(harvesting)

    with col2:
        st.header ("Average Yield per Acre")
        st. title (Yield )
    with col3:
        st.header("Average Production")
        st.title(production)

    col1, col2 = st.columns(2)
    with col1:
        st.header("Max Price")
        st.title(price)
    with col2:
        st.header("Average Value of Production")
        st.title(value)


    min_value1=helper.cheepest_price(df)
    st.header ("Cheepest wine ever")
    hide_dataframe_row_index = """
                    <style>
                    .row_heading.level0 {display:none}
                    .blank {display:none}
                    </style>
                    """
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
    st.table(min_value1)

    max_value1=helper.costliest_price(df)
    st.header("Costliest Wine Ever")
    hide_dataframe_row_index = """
                    <style>
                    .row_heading.level0 {display:none}
                    .blank {display:none}
                    </style>
                    """
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
    st.table(max_value1)

    top10 = helper.top_10_producer(df)
    fig = px.line(top10, x='County', y='Production')
    st.title('Top 10 Producer')
    st.plotly_chart(fig)

    year =helper.over_all_production(df)
    fig = px.line(year, x='Year', y='Production')
    st.title("Production as per Year")
    st.plotly_chart(fig)

    year = helper.over_all_production(df)
    fig= px.line(year, x= 'Year', y= 'Price(Dollars/Unit)')
    st.title("Price as per Year")
    st.plotly_chart(fig)

    st.title (" Country Year-wise Yield")
    fig,ax =plt.subplots(figsize=(20,20))
    ax= sns.heatmap(df.pivot_table(index='County', columns='Year', values='Yield(Unit/Acre)').fillna(0).astype('int'),
                  annot=True)
    st.pyplot(fig)

if user_menu== 'Price Tally':
    st.sidebar.header("Price Tally")
    years,country =helper.country_year_list(df)

    selected_Year= st.sidebar.selectbox("Select Years",years)
    selected_country = st.sidebar.selectbox("Select Country",country)
    price_tally=helper.fetch_price_tally(df,selected_Year,selected_country)
    if selected_Year=='Overall' and selected_country=='Overall':
        st.title("Overall Price ")
    if selected_Year != 'Overall' and selected_country == 'Overall':
        st.title("Price  of wine in - " + str(selected_Year))
    if selected_Year == 'Overall' and selected_country != 'Overall':
        st.title("Price of wine in - " + str(selected_country))
    if selected_Year != 'Overall' and selected_country != 'Overall':
        st.title("Price of wine of - "  + selected_country + " in " +  str(selected_Year) )

    hide_dataframe_row_index = """
                <style>
                .row_heading.level0 {display:none}
                .blank {display:none}
                </style>
                """
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)


    st.table(price_tally)
