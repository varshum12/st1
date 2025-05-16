import requests
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from client import StockApi




## add page title 

st.set_page_config(page_title= "Stock Market App"  , layout= "wide")


## add title for page

st.title("Stock Market App")


## Add subheading
st.subheader("By Varsha Mhetre")



# Add box for company
company = st.text_input("Company  Name")




# make connection between class and app

@st.cache_resource(ttl= 3600)
def Fetch_Data():
    return StockApi(api_key  = st.secrets["API_KEY"])



stock_api = Fetch_Data()




# search symbol

@st.cache_data(ttl = 3600)
def get_symbol(compnay):
    symbol = stock_api.search_symbol(company)
    return symbol



@st.cache_data(ttl =  3600)
def plot_chart(symbol):
    df = stock_api.time_series_daily_data(symbol)
    fig  = stock_api.plot_graph(df)
    return fig


if compnay:

    company_data  = get_symbol(company)

    symbols  =  st.selectbox(company_data)