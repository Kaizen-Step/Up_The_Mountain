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
st.set_page_config(page_title='Bridge - Up the Mountain',
                   page_icon=':bar_chart:', layout='wide')
st.title('🌉Bridge')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Daily_Bridge_BTC':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/59035870-fb5b-4af7-9c89-edaec818908a/data/latest')
    elif query == 'Bridge_BTC_Heatmap':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/6c503da1-f096-4a76-aa0e-502e13891fc0/data/latest')
    elif query == 'Brdige_to_Avax':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/b8e60286-8ac8-45c7-83d7-a3133febd67e/data/latest')
    elif query == 'Swaps_to_Near':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/8f3d6f0f-fdb5-4304-8adb-3a35ea945cf5/data/latest')
    return None


Daily_Bridge_BTC = get_data('Daily_Bridge_BTC')
Bridge_BTC_Heatmap = get_data('Bridge_BTC_Heatmap')
Brdige_to_Avax = get_data('Brdige_to_Avax')
Swaps_to_Near = get_data('Swaps_to_Near')

df = Daily_Bridge_BTC
df2 = Bridge_BTC_Heatmap
df3 = Brdige_to_Avax
df4 = Swaps_to_Near

#################################################################################################
st.write(""" ### Bridge Concept ##  """)

st.write("""
A blockchain bridge is a tool that lets you port assets from one blockchain to another, solving one of the main pain points within blockchains – a lack of interoperability.
Since blockchain assets are often not compatible with one another, bridges create synthetic derivatives that represent an asset from another blockchain.Some bridges, known as unidirectional or one-way bridges, allow you to port assets only to the target blockchain and not the other way around.Other bridges like Wormhole and Multichain are bidirectional, or two-way, meaning you can freely convert assets to and from blockchains. [[5]](https://www.coindesk.com/learn/what-are-blockchain-bridges-and-how-do-they-work/)   """)


st.info(""" ##### In This Bridge Section you can find: ####

* One and Only Whale Swap List  
* Platforms Whale Used for Swapping 
* Top 20 Swaps from Near (Not Whale List)
* Top 20 Swaps to Near (Not Whale List)


""")


#################################################################################################
st.write(""" ## Daily Bridge Transactions to BTC""")

# Daily Bridge Transactions
fig = px.bar(df.sort_values(["DATE", "Daily Transactions"], ascending=[
    True, False]), x="DATE", y="Daily Transactions", title='Daily Bridge Number of Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily Bridge BTC
fig = px.area(df.sort_values(["DATE", "AMOUNT"], ascending=[
    True, False]), x="DATE", y="AMOUNT", title='Daily Bridge Volume [BTC] ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Volume [BTC]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# avg Bridge amount per Transaction
fig = px.area(df.sort_values(["DATE", "avg amount per Transaction"], ascending=[
    True, False]), x="DATE", y="avg amount per Transaction", title='Average Bridge amount per Transaction [BTC] ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Volume [BTC]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


###############################################################

st.write(""" ## Bridge Heatmap""")


# Average Amount per Transaction on hour of day (UTC)
fig = px.density_heatmap(df2, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Volume on hour of day (UTC)",
                         histfunc='avg', title='Volume on hour of day (UTC)', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Transactions on hour of day (UTC)
fig = px.density_heatmap(df2, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Transactions on hour of day (UTC)",
                         histfunc='avg', title='Transactions on hour of day (UTC)', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Average Amount per Transaction on hour of day (UTC)
fig = px.density_heatmap(df2, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="avg amount per Transaction on hour of day (UTC)",
                         histfunc='avg', title='Average Amount per Transaction on hour of day (UTC)', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
###############################################################################

st.write(""" ## Daily Bridge Transactions to Avax""")

# Daily Bridge Transactions
fig = px.bar(df3.sort_values(["DATE", "Daily Transactions"], ascending=[
    True, False]), x="DATE", y="Daily Transactions", title='Daily Bridgers BTC to AVAX')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
