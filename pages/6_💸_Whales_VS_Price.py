# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Price - The Whales of Near',
                   page_icon=':bar_chart:', layout='wide')
st.title('💸 Near Price VS Whales ')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Near_From_CX':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/92ebc00f-2384-46b5-918e-c2287d40e2e9/data/latest')
    elif query == 'Near_TO_CX':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/43355071-4ec6-421d-94e6-650879554395/data/latest')
    return None


Near_From_CX = get_data('Near_From_CX')
Near_TO_CX = get_data('Near_TO_CX')


df = Near_From_CX
df2 = Near_TO_CX


############################################################################################################

st.write(""" ### Whale Impact Concept ##  """)

st.write("""
The community and investors watch crypto whales because they can significantly influence price movements.
Whales can also create price volatility increases, especially when they move a large quantity of cryptocurrency in one transaction. For example, if an owner is trying to sell their bitcoin for fiat currency, the lack of liquidity and large transaction size creates downward pressure on Bitcoin's price because other market participants see the transaction. When whales sell, other investors go on high alert, watching for indicators that whales are "dumping" their holdings. [[8]](https://www.investopedia.com/terms/b/bitcoin-whale.asp#:~:text=A%20crypto%20whale%20is%20a,also%20create%20price%20volatility%20increases.)   """)


st.info(""" ##### In This Price VS Whales Section you can find: ####

* Transfer From CEX Impact on NEAR Price
* Transfer to CEX Impact on NEAR Price


""")


############################################################################################################

st.write(""" ## Transfer From CEX Vs Near Price """)

# Transfer from CEX Vs Near Price
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["number of transactions"],
                     name='Transfer From CEX Num TX'), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["PRICE"],
                      name='Near Price'), secondary_y=True)
fig.update_layout(
    title_text='Transfer From CEX Number of Transaction Vs Near Price')
fig.update_yaxes(
    title_text='Number of Transaction', secondary_y=False)
fig.update_yaxes(title_text='Near Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Transfer from CEX Vs Near Price
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["AMOUNT"],
                     name='Transfer From CEX Volume'), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["PRICE"],
                      name='Near Price'), secondary_y=True)
fig.update_layout(
    title_text='Transfer From CEX Volume Vs Near Price')
fig.update_yaxes(
    title_text='Volume [Near]', secondary_y=False)
fig.update_yaxes(title_text='Near Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ## Transfer To CEX Vs Near Price """)

# Transfer To CEX Vs Near Price
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["DATE"], y=df2["number of transactions"],
                     name='Transfer From CEX Num TX'), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["PRICE"],
                      name='Near Price'), secondary_y=True)
fig.update_layout(
    title_text='Transfer To CEX Number of Transaction Vs Near Price')
fig.update_yaxes(
    title_text='Number of Transaction', secondary_y=False)
fig.update_yaxes(title_text='Near Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Transfer To CEX Vs Near Price
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["DATE"], y=df["AMOUNT"],
                     name='Transfer From CEX Volume'), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["PRICE"],
                      name='Near Price'), secondary_y=True)
fig.update_layout(
    title_text='Transfer To CEX Volume Vs Near Price')
fig.update_yaxes(
    title_text='Volume [Near]', secondary_y=False)
fig.update_yaxes(title_text='Near Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
