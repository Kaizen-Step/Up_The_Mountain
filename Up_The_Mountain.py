# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Up_The_Mountain',
                   page_icon=':bar_chart:', layout='wide')
st.title(' Up the Mountain')


# Content
c1, c2, c3 = st.columns(3)


with c1:
    st.text(" \n")
    st.text(" \n")
    st.video('https://www.youtube.com/watch?v=mWBzFmzzBAg')

with c3:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/avalanche-logo.png'), width=350)


st.write("""
### What Is Avalanche (AVAX)? ###
Avalanche (AVAX) is a cryptocurrency and blockchain platform that rivals Ethereum. AVAX is the native token of the Avalanche blockchain, which—like Ethereum—uses smart contracts to support a variety of blockchain projects. 
The Avalanche blockchain can provide near-instant transaction finality. AVAX is used to pay transaction processing fees, secure the Avalanche network, and act as a basic unit of account among blockchains in the Avalanche network.The Avalanche blockchain reportedly can process 4,500 transactions per second. Launched in 2020, Avalanche aims to be fast, versatile, secure, affordable, and accessible.  
In addition, Avalanche is an open-source project, meaning anyone can view and contribute to the platform's code.Avalanche's smart contracts platform supports both decentralized applications (dApps) and autonomous blockchains. Avalanche is generally governed by the proof-of-stake mechanism. AVAX holders are required to stake—agree not to trade or sell—AVAX in exchange for the right to validate AVAX transactions. AVAX holders with the most staked, and who actively participate as validators, are the most likely to be chosen as validators for new Avalanche blocks. Holding AVAX tokens is also required to vote on Avalanche governance proposals. [[1]](https://www.investopedia.com/avalanche-avax-definition-5217374)

### Bitcoin Bridged to Avalanche Surpasses BTC Locked in Lightning Network  ###

he number of bitcoin (BTC) bridged or ported from the Bitcoin blockchain to the Avalanche smart contract blockchain has surpassed the tally of coins held in the Lightning Network, a second-layer solution for Bitcoin's scalability problems.
On Tuesday, the total circulating supply of bridged BTC, or BTC.b, on Avalanche rose to a record 5,700 BTC (118.6 million), according to data sourced from Dune Analytics. Meanwhile, the number of bitcoin locked in the Lightening Network stood at 4,929 BTC (100 million).  
The flippening has brought cheer to the Avalanche community and developers behind the project.
"Yesterday marked a pretty awesome milestone for the asset as it exceeded 5,700 in total circulating supply on Avalanche and, in only a handful of months, surpassed the current capacity of the Lightning network," Morgan Krupetsky, director of BD for institutions and capital markets at Avalanche's creator Ava Labs wrote in a blog post on Wednesday.
Avalanche added support for BTC in its cross-chain bridge in June 2022, opening the doors for bitcoin holders to transfer coins to Avalanche and access the Avalanche-based decentralized finance (DeFi) ecosystem.
To initiate BTC to Avalanche, a user sends a user sends a transaction on Bitcoin from the new Core Wallet that transfers BTC to the bridge address controlled by the SGX enclave, a trusted execution environment embedded in a process.  
The SGX enclave then creates or mints an equivalent amount of BTC.b to the user wallet that sent the initiating Bitcoin transaction.
When moving BTC.B back to the Bitcoin Blockchain, the user sends a transaction on Avalanche, calling the "unwrap" method, which burns the BTC.b tokens.[[2]](https://www.coindesk.com/markets/2023/01/19/bitcoin-bridged-to-avalanche-surpasses-btc-locked-in-lightning-network/)


## Methodology ##  
An Avalanche has been building up steam as of late — the price of AVAX rose by nearly 100% in the month of January and BTC hodlers have been moving holdings to the Avalanche chain. 
What’s been fueling this growth over the past month — and what does the future hold for Avalanche?   
Will this growth continue into the new year? Or will growth stagnate as 2023 continues to progress?  
To answer these questions, we use "avalanche.core.fact_token_transfers" and "avalanche.core.fact_transactions" to calculate bridge transactions to Avalanche from Bitcoin Holders from October 1st, 2022, to February 15th, 2023. Then we discussed  Avax price using "ethereum.core.fact_hourly_token_prices" table and tried to find patterns in Avax price. Also, recent activities on Avalanche were investigated. Finally, features that might influence the Avax price are discussed. 


""")

st.write("""   
#### Sources ####  """)
st.write("""    
1.https://www.investopedia.com/avalanche-avax-definition-5217374       
2.https://www.coindesk.com/markets/2023/01/19/bitcoin-bridged-to-avalanche-surpasses-btc-locked-in-lightning-network/    
3.https://www.youtube.com/watch?v=mWBzFmzzBAg   
      
              """)
c1, c2 = st.columns(2)
with c2:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
    st.info(
        '**Project Github:  [Up The Mountain](https://github.com/Kaizen-Step/Up_The_Mountain)**', icon="💻")

with c1:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
    st.info(
        '**Twitter:  [Ludwig.1989](https://flipsidecrypto.xyz/)**', icon="🕊️")
