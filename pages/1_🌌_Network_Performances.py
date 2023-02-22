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
st.set_page_config(page_title='Network Performances - Up the Mountain',
                   page_icon=':bar_chart:', layout='wide')
st.title('🎯Network Performances')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Heat_Map1':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e86b9a6e-a735-480c-94e1-42c25f0883a3/data/latest')
    elif query == 'Heat_Map2':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/927c0e10-ccee-44f3-bb8a-e1083a0496dd/data/latest')
    elif query == 'Daily_Net_per':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/90e4ae8e-6e67-40de-87bc-0f36ac7c2939/data/latest')
    elif query == 'Daily_time_bet_Blocks':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/beeab35b-37cf-448f-815f-045dc3716afe/data/latest')
    elif query == 'Daily_TPS':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/f0e4aac7-763c-4d29-a5b9-19167bbefef6/data/latest')
    elif query == 'Top10_TransactionType':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e54eaa63-ab14-4313-af7a-fdff2d8abecc/data/latest')
    elif query == 'TX_SUCC_Fail':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/a21367b3-6df5-447c-996e-919d2f89b6e7/data/latest')
    return None


Heat_Map1 = get_data('Heat_Map1')
Heat_Map2 = get_data('Heat_Map2')
Daily_Net_per = get_data('Daily_Net_per')
Daily_time_bet_Blocks = get_data('Daily_time_bet_Blocks')
Daily_TPS = get_data('Daily_TPS')
Top10_TransactionType = get_data('Top10_TransactionType')
TX_SUCC_Fail = get_data('TX_SUCC_Fail')


df = Heat_Map1
df2 = Heat_Map2
df3 = Daily_Net_per
df4 = Daily_time_bet_Blocks
df5 = Daily_TPS
df6 = Top10_TransactionType
df6 = TX_SUCC_Fail
######################################################################################################################


st.write(""" ### Key Metrics to Measure Blockchain Network performance ##  """)

st.write("""
Everything out there has a particular set of characteristics against which its performance can be measured. Be it something as simple as a car or as intricately intertwined as the blockchain. These factors also help draw a comparison between two or multiple blockchains in order to find out the one that’s best for developing projects.[[4]](https://bitcoinist.com/key-metrics-to-measure-blockchain-network-performance/)   

* Transactions per Second (TPS)  
* Transaction Latency  
* Block Time  
* Success Rate

For this section we try to evaluate Avalanche with these Metirce.
   """)


st.info(""" ##### In This Network Performance you can find: ####

 * Daily Trnasaction Per Second (TPS)  
 * Daily Average Transactions per block  
 * Daily Time Between Blocks (Average and Max Value)
 * Daily Success Rate
 * Network Performance Heat Maps



""")


#####################################################################################

st.write(""" ## Daily Network Performance  """)


# Average Transaction per second (TPS)
fig = px.bar(df5.sort_values(["DATE", "AVG_TPS"], ascending=[
    True, False]), x="DATE", y="AVG_TPS", title='Daily Average Transaction per second(TPS)')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily TPS')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily Average Transactions per block
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df3["DATE"], y=df3["Daily Blocks"],
                     name="Daily Blocks"), secondary_y=False)
fig.add_trace(go.Line(x=df3["DATE"], y=df3["Daily Average Transactions per block"],
                      name="Daily Average Transactions per block"), secondary_y=True)
fig.update_layout(
    title_text='Daily Average Transactions per block (TPB)')
fig.update_yaxes(
    title_text="Daily Blocks", secondary_y=False)
fig.update_yaxes(
    title_text="Daily Average Transactions per block", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Time Between Blocks
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df4["DATE"], y=df4["MAX_SEC"],
                     name="Maximum Time"), secondary_y=False)
fig.add_trace(go.Bar(x=df4["DATE"], y=df4["AVERAGE_SEC"],
                     name="Average Time"), secondary_y=False)
fig.update_layout(
    title_text=' Daily Time Between Blocks [Second]')
fig.update_yaxes(
    title_text="Time between blocks", secondary_y=False)
fig.update_yaxes(
    title_text="Daily Average Transactions per block", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Success Rate
fig = px.bar(df5.sort_values(["DATE", "DAILY_SUCCESS_RATE"], ascending=[
    True, False]), x="DATE", y="DAILY_SUCCESS_RATE", title='Daily Success Rate')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="DAILY SUCCESS RATE")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#####################################################################################

st.write(""" ## Network Performance Heatmaps """)

c1, c2 = st.columns(2)

with c1:
    # Block per Minute Daily HEAT
    fig = px.density_heatmap(df, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="block per minute on hour of day (UTC)",
                             histfunc='avg', title='Block per Minute Daily HEAT', nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # "transactions per minute on hour of day (UTC)"
    fig = px.density_heatmap(df, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="transactions per minute on hour of day (UTC)",
                             histfunc='avg', title="Transactions per minute on hour of day (UTC)", nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with c2:
    # "transactions per minute on hour of day (UTC)"
    fig = px.density_heatmap(df, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="User per minute on hour of day (UTC)",
                             histfunc='avg', title="User per minute on hour of day (UTC)", nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Failed transactions per minute on hour of day (UTC)
    fig = px.density_heatmap(df2, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Failed transactions per minute on hour of day (UTC)",
                             histfunc='avg', title='Failed transactions per minute on hour of day (UTC)', nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#################################################################################


########################################################################################################################
