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

