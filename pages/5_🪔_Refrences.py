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
st.set_page_config(page_title='Aknowledgement - Terra Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🪔 Refrences')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Aknowledgement
st.write(""" ##     Aknowledgement 
We are grateful to all who helped us develop this project specially [**Mr. Ali Taslimi**](https://twitter.com/AliTslm) with comprehensive streamlit open source project [Cross chain Monitoring](https://github.com/alitslm/cross_chain_monitoring) that provides streamlit functions and tools.
And also ****Flipside Crypto**** with massive database and last but not least ****MetricsDao**** that is the reason behind this project.
""")


# SQL Codes
st.write(""" ## SQL Codes ## """)

st.write("""
At the following links, you can find the SQL codes that are used in this dashboard: 

""")


c1, c2 = st.columns(2)

with c1:
    st.write("""
    1. [AVAX-Daily Price Change Comprison](https://flipsidecrypto.xyz/edit/queries/b54dfa53-a913-40dd-ad5d-4fc65f88f820/visualizations/72dba76e-4dfa-4255-8d4a-25f0039334c9)
    2. [Avax- transactions metrc](https://flipsidecrypto.xyz/edit/queries/2aa6e8c8-7ed6-4eac-9185-bd6690792275/visualizations/4e83b7a4-59dc-40e9-86d6-784d1457f2db)
    3. [AVAX DAILY PRICE vs BTC/Matic/SOL/ETH/OP](https://flipsidecrypto.xyz/edit/queries/a3f14d61-47e8-4f22-aaa6-2fd6aca9e130/visualizations/e642b7a6-35c3-427d-b3a5-597f2ca2beba)
    4. [Avax-Hourly Price Change Comprison](https://flipsidecrypto.xyz/edit/queries/3c94f782-d336-47a9-a22d-e1f13c816dc0/visualizations/af278899-b02e-4e84-9ab8-d7e2e197ef71)
    5. [Avax-  Daily Bridge BTC](https://flipsidecrypto.xyz/edit/queries/59035870-fb5b-4af7-9c89-edaec818908a/visualizations/a4e36491-31a8-4cfe-90b2-d5c9b0b76ae7)
    6. [Avax-  Daily Bridge BTC heatmap](https://flipsidecrypto.xyz/edit/queries/6c503da1-f096-4a76-aa0e-502e13891fc0/visualizations/ab4b264e-dc8c-46be-bde8-bf73099b18b2)
    7. [Avax- Daily Average Transactions per block](https://flipsidecrypto.xyz/edit/queries/90e4ae8e-6e67-40de-87bc-0f36ac7c2939/visualizations/e5896679-203d-4ab3-81b8-ef149d9e386f)
    8. [Avax- transactions metrc](https://flipsidecrypto.xyz/edit/queries/2aa6e8c8-7ed6-4eac-9185-bd6690792275/visualizations/4e83b7a4-59dc-40e9-86d6-784d1457f2db)
    9. [Daily TX_FEE Type_Platform](https://flipsidecrypto.xyz/edit/queries/8a5efd9a-2075-4d42-b4ae-01240827c9e1/visualizations/184637fc-6c70-44eb-bf24-bcbde37334c9)
    
    """)

with c2:

    st.write("""
    
    10. [Avax- min/max/avg price](https://flipsidecrypto.xyz/edit/queries/e7b2e139-c12d-4652-ad0e-338fdd556a4b/visualizations/b01c6e2d-b746-4d60-b59e-3eb0c1955d3b)
    11. [AVAX Daily PRICE Moving Averages ](https://flipsidecrypto.xyz/edit/queries/21267cbc-bcd4-4fb9-8017-914e74a3a40d/visualizations/996c896b-4e8f-43fc-b8fd-d07a38aec6fa)
    12. [AVAX DAILY PRICE vs BTC/Matic/SOL/ETH/OP ](https://flipsidecrypto.xyz/edit/queries/ee55cea0-347d-421c-852a-cbd8741b12ef/visualizations/744e9ad2-427e-4b85-b77e-d31f60455ebe)  
    13. [AVAX DAILY PRICE vs BTC/Matic/SOL/ETH/OP](https://flipsidecrypto.xyz/edit/queries/c906624e-f7f8-4f92-9ca9-4889f6c88c68/visualizations/a5c5de72-3a78-4db6-9970-a57cc11be583)
    14. [Avax - Daily bridge user to avax](https://flipsidecrypto.xyz/edit/queries/b8e60286-8ac8-45c7-83d7-a3133febd67e/visualizations/c668bed7-5807-42bf-af20-2828206d6362)
    15. [Avax-  Average TPS](https://flipsidecrypto.xyz/edit/queries/f0e4aac7-763c-4d29-a5b9-19167bbefef6/visualizations/cbabc4cf-eb60-4d5e-bef8-807f117b89d2)
    16. [Avax- Daily HEAT Map 1](https://flipsidecrypto.xyz/edit/queries/e86b9a6e-a735-480c-94e1-42c25f0883a3/visualizations/c356da74-65c4-48e0-97af-bb20fcd439ae)
    17. [Avax- Daily HEAT Map 2](https://flipsidecrypto.xyz/edit/queries/927c0e10-ccee-44f3-bb8a-e1083a0496dd/visualizations/a31114e3-5557-4477-9b7b-c8da7f158138)  
    18. [Avax- transactions metrc](https://flipsidecrypto.xyz/edit/queries/2aa6e8c8-7ed6-4eac-9185-bd6690792275/visualizations/4e83b7a4-59dc-40e9-86d6-784d1457f2db)    

    """)

# Sources
st.write(""" ## Sources ## """)

st.write("""
1.https://www.investopedia.com/avalanche-avax-definition-5217374         
2.https://www.coindesk.com/markets/2023/01/19/bitcoin-bridged-to-avalanche-surpasses-btc-locked-in-lightning-network/      
3.https://www.youtube.com/watch?v=mWBzFmzzBAg    
4.https://bitcoinist.com/key-metrics-to-measure-blockchain-network-performance/  
5.https://www.coindesk.com/learn/what-are-blockchain-bridges-and-how-do-they-work/     
6.https://coinmarketcap.com/currencies/avalanche/     
7.https://www.bitstamp.net/learn/crypto-101/how-do-cryptocurrency-transactions-work/  

""")
