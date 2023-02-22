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
st.set_page_config(page_title='Avax Price - Up the Mountain',
                   page_icon=':bar_chart:', layout='wide')
st.title('🚀 Avax Price')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Hourly_Price':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e7b2e139-c12d-4652-ad0e-338fdd556a4b/data/latest')
    elif query == 'Price_MovingAverages':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/21267cbc-bcd4-4fb9-8017-914e74a3a40d/data/latest')
    elif query == 'Hourly_MA':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/a7c560da-651a-4eae-99d6-f0250e61c7dc/data/latest')
    elif query == 'Avax_VS_Tokens':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ee55cea0-347d-421c-852a-cbd8741b12ef/data/latest')
    elif query == 'Avax_vs_Daily_Tokens':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/c906624e-f7f8-4f92-9ca9-4889f6c88c68/data/latest')
    elif query == 'Price_Change_Comparison':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/b54dfa53-a913-40dd-ad5d-4fc65f88f820/data/latest')
    elif query == 'Price_Change_Comparison_Hourly':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/b54dfa53-a913-40dd-ad5d-4fc65f88f820/data/latest')
    return None


Hourly_Price = get_data('Hourly_Price')
Price_MovingAverages = get_data('Price_MovingAverages')
Hourly_MA = get_data('Hourly_MA')
Avax_VS_Tokens = get_data('Avax_VS_Tokens')
Avax_vs_Daily_Tokens = get_data('Avax_vs_Daily_Tokens')
Price_Change_Comparison = get_data('Price_Change_Comparison')
Price_Change_Comparison_Hourly = get_data('Price_Change_Comparison_Hourly')

df = Hourly_Price
df2 = Price_MovingAverages
df3 = Hourly_MA
df4 = Avax_VS_Tokens
df5 = Avax_vs_Daily_Tokens
df6 = Price_Change_Comparison
df7 = Price_Change_Comparison_Hourly

#########################################################################################

st.write(""" ### Avax Price Summary ##  """)

st.write("""
The live Avalanche price today is 20.56 USD with a 24-hour trading volume of 692,788,306 USD. Avalanche is up 2.23% in the last 24 hours. The current CoinMarketCap ranking is #15, with a live market cap of 6,479,078,378 USD. It has a circulating supply of 315,125,667 AVAX coins and a max. supply of 720,000,000 AVAX coins.An Avalanche has been building up steam as of late — the price of AVAX rose by nearly 100% from start of 2023 with 11.18 USD. [[6]](https://coinmarketcap.com/currencies/avalanche/ )  """)


st.info(""" ##### In This Avax Price Section you can find: ####


* Avax Price with Standard Moving Averages [H & D]
* Avax Price Compare to Role Models [H & D]
* Avax Price Compare to Rivals [H & D]
* Price Change Rate [H & D]
""")


#########################################################################################


# Avax Price Moving averages
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df2['DATE'], y=df2["AVAX_PRICE"],
                      name="Avax PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA7'],
                      name='Hourly Moving average (MA7))'), secondary_y=True)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA26'],
                      name='Hourly Moving average (MA26)'), secondary_y=True)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA52'],
                      name='Hourly Moving average (MA52))'), secondary_y=True)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA100'],
                      name='Hourly Moving average (MA100)'), secondary_y=True)
fig.update_layout(
    title_text='Avax Daily Price With Standard Moving averages ')
fig.update_yaxes(
    title_text='Price', secondary_y=False)
fig.update_yaxes(title_text='Moving averages', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Hourly Price- AVAX vs ETH
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df3['DATE'], y=df3["AVAX_PRICE"],
                      name="Avax Price"), secondary_y=False)
fig.add_trace(go.Line(x=df3['DATE'], y=df3['MA7'],
                      name='Hourly Moving average (MA7))'), secondary_y=True)
fig.add_trace(go.Line(x=df3['DATE'], y=df3['MA26'],
                      name='Hourly Moving average (MA26)'), secondary_y=True)
fig.add_trace(go.Line(x=df3['DATE'], y=df3['MA52'],
                      name='Hourly Moving average (MA52))'), secondary_y=True)
fig.add_trace(go.Line(x=df3['DATE'], y=df3['MA100'],
                      name='Hourly Moving average (MA100)'), secondary_y=True)
fig.add_trace(go.Line(x=df3['DATE'], y=df3['MA200'],
                      name='Hourly Moving average (MA200)'), secondary_y=True)
fig.update_layout(
    title_text='Avax Hourly Price With Standard Moving Averages')
fig.update_yaxes(
    title_text='Price', secondary_y=False)
fig.update_yaxes(title_text='Moving averages', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Hourly Price- AVAX vs ETH
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df["DATE"], y=df["AVAX_AVG_PRICE"],
                      name="Avax Houlrly Average Price"), secondary_y=False)
fig.add_trace(go.Line(x=df['DATE'], y=df["AVAX_MA_PRICE"],
                      name='Avax Hourly Max Price'), secondary_y=True)
fig.add_trace(go.Line(x=df['DATE'], y=df["AVAX_MIN_PRICE"],
                      name='Avax Hourly Min Price'), secondary_y=True)
fig.update_layout(
    title_text='Avax Hourly Max Min Average Price')
fig.update_yaxes(
    title_text='Price', secondary_y=False)
fig.update_yaxes(
    title_text='Avax Hourly Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

################################################################################
st.write(""" ## Avax Price Compare to Role Models """)

# AVAX vs Bitcoin Price [Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df5['DATE'], y=df5["AVAX_PRICE"],
                      name="Avax Price"), secondary_y=False)
fig.add_trace(go.Line(x=df5['DATE'], y=df5["BTC_PRICE"],
                      name='Bitcoin Price'), secondary_y=True)
fig.update_layout(
    title_text='AVAX vs Bitcoin Price [Daily]')
fig.update_yaxes(
    title_text=' Daily Avax Price', secondary_y=False)
fig.update_yaxes(title_text=' Daily Bitcoin Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# AVAX vs Bitcoin Price [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df4['DATE'], y=df4["AVAX_PRICE"],
                      name="Avax Price"), secondary_y=False)
fig.add_trace(go.Line(x=df4['DATE'], y=df4["BTC_PRICE"],
                      name='Bitcoin Price'), secondary_y=True)
fig.update_layout(
    title_text='AVAX vs Bitcoin Price [Hourly]')
fig.update_yaxes(
    title_text=' Hourly Avax Price', secondary_y=False)
fig.update_yaxes(title_text=' Hourly Bitcoin Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# AVAX vs ETH Price [Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df5['DATE'], y=df5["AVAX_PRICE"],
                      name="Avax Price"), secondary_y=False)
fig.add_trace(go.Line(x=df5['DATE'], y=df5["ETH_PRICE"],
                      name='Etherum Price'), secondary_y=True)
fig.update_layout(
    title_text='AVAX vs Etherum Price [Daily]')
fig.update_yaxes(
    title_text=' Daily Avax Price', secondary_y=False)
fig.update_yaxes(title_text=' Daily Etherum Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# AVAX vs ETH Price [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df4['DATE'], y=df4["AVAX_PRICE"],
                      name="Avax Price"), secondary_y=False)
fig.add_trace(go.Line(x=df4['DATE'], y=df4["ETH_PRICE"],
                      name='Etherum Price'), secondary_y=True)
fig.update_layout(
    title_text='AVAX vs Etherum Price [Hourly]')
fig.update_yaxes(
    title_text=' Hourly Avax Price', secondary_y=False)
fig.update_yaxes(title_text=' Hourly Etherum Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ## Avax Price Compare to Rivals""")

# AVAX vs MATIC Price [Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df5['DATE'], y=df5["AVAX_PRICE"],
                      name="Avax Price"), secondary_y=False)
fig.add_trace(go.Line(x=df5['DATE'], y=df5["MATIC_PRICE"],
                      name='Matic Price'), secondary_y=True)
fig.update_layout(
    title_text='AVAX vs MATIC Price [Daily]')
fig.update_yaxes(
    title_text=' Daily Avax Price', secondary_y=False)
fig.update_yaxes(title_text=' Daily Matic Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# AVAX vs MATIC Price [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df4['DATE'], y=df4["AVAX_PRICE"],
                      name="Avax Price"), secondary_y=False)
fig.add_trace(go.Line(x=df4['DATE'], y=df4["MATIC_PRICE"],
                      name='Matic Price'), secondary_y=True)
fig.update_layout(
    title_text='AVAX vs MATIC Price [Hourly]')
fig.update_yaxes(
    title_text=' Hourly Avax Price', secondary_y=False)
fig.update_yaxes(title_text=' Hourly Matic Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# AVAX vs OP Price [Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df5['DATE'], y=df5["AVAX_PRICE"],
                      name="Avax Price"), secondary_y=False)
fig.add_trace(go.Line(x=df5['DATE'], y=df5["OP_PRICE"],
                      name='Optimism Price'), secondary_y=True)
fig.update_layout(
    title_text='AVAX vs Optimism Price [Daily]')
fig.update_yaxes(
    title_text=' Daily Avax Price', secondary_y=False)
fig.update_yaxes(title_text=' Daily Optimism Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# AVAX vs OP Price [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df4['DATE'], y=df4["AVAX_PRICE"],
                      name="Avax Price"), secondary_y=False)
fig.add_trace(go.Line(x=df4['DATE'], y=df4["OP_PRICE"],
                      name='Optimism Price'), secondary_y=True)
fig.update_layout(
    title_text='AVAX vs Optimism Price [Hourly]')
fig.update_yaxes(
    title_text=' Hourly Avax Price', secondary_y=False)
fig.update_yaxes(title_text=' Hourly Optimism Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# AVAX vs Solana Price [Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df5['DATE'], y=df5["AVAX_PRICE"],
                      name="Avax Price"), secondary_y=False)
fig.add_trace(go.Line(x=df5['DATE'], y=df5["SOL_PRICE"],
                      name='Solana Price'), secondary_y=True)
fig.update_layout(
    title_text='AVAX vs Solana Price [Daily]')
fig.update_yaxes(
    title_text=' Daily Avax Price', secondary_y=False)
fig.update_yaxes(title_text=' Daily Solana Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# AVAX vs Solana Price [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df4['DATE'], y=df4["AVAX_PRICE"],
                      name="Avax Price"), secondary_y=False)
fig.add_trace(go.Line(x=df4['DATE'], y=df4["SOL_PRICE"],
                      name='Solana Price'), secondary_y=True)
fig.update_layout(
    title_text='AVAX vs Solana Price [Hourly]')
fig.update_yaxes(
    title_text=' Hourly Avax Price', secondary_y=False)
fig.update_yaxes(title_text=' Hourly Solana Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#####################################################################


#####################################################################

st.write(""" ##  Price Change Rate [Daily] """)

# Daily Price Change Comprison
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df6['DATE'], y=df6["AVAX_CHANGE"],
                      name="AVAX CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df6['DATE'], y=df6["SOL_CHANGE"],
                      name='"Solana CHANGE"'), secondary_y=False)
fig.add_trace(go.Line(x=df6['DATE'], y=df6["BTC_CHANGE"],
                      name='"Bitcoin CHANGE"'), secondary_y=False)
fig.add_trace(go.Line(x=df6['DATE'], y=df6["ETH_CHANGE"],
                      name="Etherum CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df6['DATE'], y=df6["MATIC_CHANGE"],
                      name="MATIC CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df6['DATE'], y=df6["OP_CHANGE"],
                      name="Optimism CHANGE"), secondary_y=False)
fig.update_layout(
    title_text='Daily Price Change Comprison')
fig.update_yaxes(
    title_text=' Price Change', secondary_y=False)
fig.update_yaxes(title_text='Price Change', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(""" ##  Price Change Rate Comparison [Hourly] """)

# Hourly Price Change Comprison
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df7['DATE'], y=df7["AVAX_CHANGE"],
                      name="AVAX CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df7['DATE'], y=df7["SOL_CHANGE"],
                      name='"Solana CHANGE"'), secondary_y=False)
fig.add_trace(go.Line(x=df7['DATE'], y=df7["BTC_CHANGE"],
                      name='"Bitcoin CHANGE"'), secondary_y=False)
fig.add_trace(go.Line(x=df7['DATE'], y=df7["ETH_CHANGE"],
                      name="Etherum CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df7['DATE'], y=df7["MATIC_CHANGE"],
                      name="MATIC CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df7['DATE'], y=df7["OP_CHANGE"],
                      name="Optimism CHANGE"), secondary_y=False)
fig.update_layout(
    title_text='Hourly Price Change Comprison')
fig.update_yaxes(
    title_text=' Price Change', secondary_y=False)
fig.update_yaxes(title_text='Price Change', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
