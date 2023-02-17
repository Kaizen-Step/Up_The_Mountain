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

# Sources
st.write(""" ## Sources ## """)

st.write("""
1.https://www.coindesk.com/learn/what-is-near-protocol-and-how-does-it-work/    
2.https://worldcoin.org/articles/what-is-a-crypto-whale    
3.https://www.youtube.com/watch?v=1cozsZP8yd4&t=30s  
4.https://www.bitstamp.net/learn/crypto-101/how-do-cryptocurrency-transactions-work/  
5.https://academy.binance.com/en/articles/what-s-the-difference-between-a-cex-and-a-dex   
6.https://www.forbes.com/advisor/in/investing/cryptocurrency/what-is-staking-in-crypto/#:~:text=Staking%20is%20when%20you%20lock,proof%20of%20stake%20consensus%20mechanism.   
7.https://bitpay.com/blog/what-is-a-crypto-swap/#:~:text=Crypto%20swapping%20allows%20you%20to,reason%20users%20participate%20in%20swapping.  
8.https://www.investopedia.com/terms/b/bitcoin-whale.asp#:~:text=A%20crypto%20whale%20is%20a,also%20create%20price%20volatility%20increases.  

""")

# SQL Codes
st.write(""" ## SQL Codes ## """)

st.write("""
At the following links, you can find the SQL codes that are used in this dashboard: 

""")


c1, c2 = st.columns(2)

with c1:
    st.write("""
    1. [Daily Transaction Fee Based on Users](https://flipsidecrypto.xyz/edit/queries/efb927d0-41bd-4762-a2f2-b463b8cfb01e/visualizations/02c54c89-d55f-4611-8cc6-bcfe7e6d386a)
    2. [Daily Transaction Success and Fails](https://flipsidecrypto.xyz/edit/queries/a21367b3-6df5-447c-996e-919d2f89b6e7/visualizations/d8836273-aed8-42db-9805-a9e0ec90f271)
    3. [Top 10 Transaction Type](https://flipsidecrypto.xyz/edit/queries/e54eaa63-ab14-4313-af7a-fdff2d8abecc/visualizations/221f849d-3463-4e65-9431-1b2b86224322)
    4. [Top 10 Platforms](https://flipsidecrypto.xyz/edit/queries/934aaafb-dde1-41b4-ad66-eb7a15f30e5c/visualizations/ade73bfa-1eee-4a64-8ae5-46c21de94da4)
    5. [Total Transaction Comparison](https://flipsidecrypto.xyz/edit/queries/fb5217ce-4ab7-44ce-83e5-8aa7b9a79e96/visualizations/c0f44e09-b01b-4f3d-890e-76777479faa1)
    6. [Daily Transaction Fee Based on Action Type](https://flipsidecrypto.xyz/edit/queries/7232fce4-57e1-41e9-a356-2a3b857e4687/visualizations/9d09c7b4-b6c8-445b-8ff7-668ccae7bc7a)
    7. [Daily TX Type](https://flipsidecrypto.xyz/edit/queries/7232fce4-57e1-41e9-a356-2a3b857e4687/visualizations/9d09c7b4-b6c8-445b-8ff7-668ccae7bc7a)
    8. [Transaction Type in each wallet](https://flipsidecrypto.xyz/edit/queries/a89edfff-1085-4954-a859-6f2abd0b639f/visualizations/79de6764-7c8f-4d00-86ed-d9fe4b159a8f)
    9. [Daily TX_FEE Type_Platform](https://flipsidecrypto.xyz/edit/queries/8a5efd9a-2075-4d42-b4ae-01240827c9e1/visualizations/184637fc-6c70-44eb-bf24-bcbde37334c9)
    10. [Whale number of Swaps](https://flipsidecrypto.xyz/edit/queries/ac3115a1-889a-42c2-a24c-6bca000fac66)
    11. [Whale swaps in details](https://flipsidecrypto.xyz/edit/queries/4d83f6d7-8e36-4a83-bcbe-1a6932d5aaff/visualizations/d6254f2c-6a57-4d6e-8562-5220614faac0)
    12. [Whale Unstake in last 12 Month](https://flipsidecrypto.xyz/edit/queries/233d8efc-a071-46f7-bacc-42317a39c663/visualizations/42d33378-7db2-46f7-9b39-37aa2bf6b96c)  
    13. [Whale stake in last 12 month](https://flipsidecrypto.xyz/edit/queries/7d23a8c4-64de-484c-9d8d-045d17c40657/visualizations/5f796f21-def9-4973-8d38-ceb275673738)
    """)

with c2:

    st.write("""
    
    14. [NEAR Top20 Whales Excluded](https://flipsidecrypto.xyz/edit/queries/e352c3a7-bd07-45c0-8ef9-4aa30ffe51b3/visualizations/f1f9cf6c-7bb2-4ed9-afa4-a78874c0827e)
    15. [NEAR Top20 Whales](https://flipsidecrypto.xyz/edit/queries/53e0d38b-0c1c-4022-8c86-bc158cbdee2d/visualizations/409aa71a-bea2-4547-80f3-56e4ec9b8136)
    16. [NFT Mint whales Number of MIn in 3 month](https://flipsidecrypto.xyz/edit/queries/23eb21da-8cdb-48f5-bd8a-0e2c1cff7a2c/visualizations/2962ed88-809c-4828-9ebc-046872a36c1f)
    17. [Number of Transactions & Total TX fee](https://flipsidecrypto.xyz/edit/queries/f53a3354-3ce1-4491-b21c-21ad97420666/visualizations/66b04805-c49e-418d-8b0b-34536f4dc2a3)  
    18. [price - transfer to CEX-DAILY vs NEAR Price](https://flipsidecrypto.xyz/edit/queries/43355071-4ec6-421d-94e6-650879554395/visualizations/00c073be-2b8f-4316-b578-f1f170c6922c)    
    19. [price-transfer from CEX Vs Near Price](https://flipsidecrypto.xyz/edit/queries/92ebc00f-2384-46b5-918e-c2287d40e2e9)    
    20. [transfer to CEX](https://flipsidecrypto.xyz/edit/queries/a815a314-6f66-4377-9376-c121cdefc77b/visualizations/06e73e3a-5234-49de-93d7-ed34563b827c)    
    21. [Transfer From CEX](https://flipsidecrypto.xyz/edit/queries/0c772bd7-5e93-48da-adb8-a2a8e3188fad/visualizations/fdb86178-ca18-4e5a-ae7a-9319e4af58d2)    
    22. [Daily Transfer to CEX ](https://flipsidecrypto.xyz/edit/queries/edd737e4-1b0a-404e-842b-3a78d8a87ab6/visualizations/2d2b0ecb-0b78-4ef1-b879-34e12150ecfc)    
    23. [Daily Transfer from CEX](https://flipsidecrypto.xyz/edit/queries/fc17e948-2ddf-4169-a6fe-07cffda76777/visualizations/a7c1fc82-3a16-4fcc-babc-31e2ecc9873e)    
    24. [Weekly Transfer to CEX](https://flipsidecrypto.xyz/edit/queries/1cce9de6-602c-4fc3-aafb-1ad288d80af5/visualizations/8a6e9f6c-804b-40e3-85b6-663535284c61)    
    25. [Weekly Transfer from CEX](https://flipsidecrypto.xyz/edit/queries/389c01aa-bdd4-4f1c-b623-4237cc5e731c/visualizations/262c424a-f864-4862-9c80-f5d9598418f9)    
    26. [Whale Stake Transactions](https://flipsidecrypto.xyz/edit/queries/3ec8472a-7923-4996-97c7-6c27a06a36b7)    

    """)
