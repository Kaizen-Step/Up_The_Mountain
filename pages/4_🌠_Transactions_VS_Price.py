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
st.set_page_config(page_title='Transactions - Up The Mountain',
                   page_icon=':bar_chart:', layout='wide')
st.title('🌠Transactions')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Transaction_Price':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ce9955e3-6c79-4e6f-b2fe-98dc73200395/data/latest')
    elif query == 'Daily_TX_Type':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/999b8676-c867-4638-8a0b-6833dbef705c/data/latest')
    elif query == 'Daily_TX_FEE_Type':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7232fce4-57e1-41e9-a356-2a3b857e4687/data/latest')
    elif query == 'Total_Transaction_Comparison':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fb5217ce-4ab7-44ce-83e5-8aa7b9a79e96/data/latest')
    elif query == 'Top10_Platforms':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/934aaafb-dde1-41b4-ad66-eb7a15f30e5c/data/latest')
    elif query == 'Top10_TransactionType':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e54eaa63-ab14-4313-af7a-fdff2d8abecc/data/latest')
    elif query == 'TX_SUCC_Fail':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/a21367b3-6df5-447c-996e-919d2f89b6e7/data/latest')
    return None


Transaction_Price = get_data('Transaction_Price')
Daily_TX_Type = get_data('Daily_TX_Type')
Daily_TX_FEE_Type = get_data('Daily_TX_FEE_Type')
Total_Transaction_Comparison = get_data('Total_Transaction_Comparison')
Top10_Platforms = get_data('Top10_Platforms')
Top10_TransactionType = get_data('Top10_TransactionType')
TX_SUCC_Fail = get_data('TX_SUCC_Fail')


df = Transaction_Price
df2 = Daily_TX_Type
df3 = Daily_TX_FEE_Type
df4 = Total_Transaction_Comparison
df5 = Top10_Platforms
df6 = Top10_TransactionType
df6 = TX_SUCC_Fail
######################################################################################################################


st.write(""" ### Transaction Concept ##  """)

st.write("""
A Simply put, cryptocurrency transaction is a transfer of information made between blockchain addresses. These transfers have to be signed with a private key that corresponds to its address. Signed transactions are broadcast to the network of nodes, active computers that follow a specific set of rules to validate transactions and blocks. Valid transactions need to be confirmed by being included in blocks through the process of mining.[[4]](https://www.bitstamp.net/learn/crypto-101/how-do-cryptocurrency-transactions-work/)   """)


st.info(""" ##### In This Transaction Section you can find: ####

 * Whales Different Type of Transactions Activity 
 * Whales Transactions Compare to other Users  
 * Whales Weekly Transaction Prespective view (Last 12 Month)
 * Whales Daily Transaction Zoom in (Last 3 Month)



""")


#####################################################################################
st.write(""" ## New Comers & Avax price """)

# Avaluanch New Comers & avax price
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["newcomers on Avaluanch"],
                     name="newcomers on Avaluanch"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["AVAX_PRICE"],
                      name="AVAX_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Avalanch New Comers & avax price')
fig.update_yaxes(
    title_text="newcomers on Avaluanch", secondary_y=False)
fig.update_yaxes(title_text="AVAX_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
