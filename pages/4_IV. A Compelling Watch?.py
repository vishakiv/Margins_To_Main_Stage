import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

st.title("IV. A Compelling Watch?")

st.markdown(
    """
    <div style="text-align: left; font-size: 22px;">
    A competitive World Cup requires a delicate balance between a level playing field and a sense of unpredictability, combined with strong audience engagement.
    Viewers want to see goals — but not one-sided games. Is this the case in the Women’s World Cup?<br><br>

    I have defined a one-sided game (a thrashing) as a match in which the goal difference (difference in goals scored between two teams) exceeds 3. 
    The percentage per tournament statistics for the WWC are revealing:

    In the inaugural tournament of 1991, a staggering 30% of games ended in blow-outs — and up until 2007, this number was still high as 22%.<br>
    In the Men’s World Cup, in comparison, no tournament since 1958 has had an equivalent rate of over 10%.

    While there was a signficant dip from 2011, every expanded tournament (2015 and 2023) has seen an increase in the percentage of thrashings.
    Newcomers to the tournament are often significantly weaker than established tournament opposition, creating more mismatches. Nowhere was this clearer when debutants Thailand
    suffered a miserable 13-0 loss in their group stage game against USA in 2019.
     </div>""", unsafe_allow_html=True
)


matches = pd.read_csv("data/matches.csv",index_col=0)
matches["goal_difference"] = (matches['home_score'] - matches['away_score']).abs()

thrashings = matches[matches["goal_difference"] > 3]\
            .groupby("Year").size()

total_games = matches.groupby("Year").size()
share_thrashings = (thrashings/ total_games * 100.0).round(2).reset_index()
share_thrashings.columns = ["Year","Thrashing_Rate"]

fig_6 = px.line(share_thrashings,
              x='Year',
              y='Thrashing_Rate',
              title='Thrashings per tournament (%)',
              labels={"Thrashing_Rate":"Thrashings(%)"},
              hover_data = {"Thrashing_Rate": True,'Year': False},
              hover_name="Year"
             )
fig_6.update_traces(mode='lines+markers', marker=dict(size=8, color='#2a76d9'))
fig_6.update_layout(
    title={
        "text": "How competitive are games at the WWC?<br><span style='font-size:14px; font-weight:normal; color:gray;'>Thrashings per tournament(%)</span>",
        "font": {
            'family': "Helvetica-Bold",  
            'size': 18,                   
            'color': "black",             
        },
         "x": 0, 
        "xanchor": "left" 
    },
    font=dict(
        family="Helvetica",  
        size=14,  
        color="black" 
    ),
    template='plotly_white',
    showlegend=True,
    width=600,
    height=400,
    yaxis_title="",
    yaxis=dict(showgrid=True),
    xaxis=dict(showgrid=False)
)
fig_6.update_xaxes(title='',tickmode='array', tickvals=[1991, 1995, 1999, 2003, 2007, 2011, 2015, 2019, 2023])
fig_6.update_yaxes(title='Percentage',tickmode='array', tickvals=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

st.plotly_chart(fig_6, use_container_width=True, key="knockout_stage")

st.markdown(
    """
    <div style="text-align: left; font-size: 22px;">
    Another way of evaulating competitiveness is predictability. Here I have chosen to look at the diversity of teams being represented in the tournament's latter stages.
    Looking at the last 3 World Cups, which feature 16 team knockouts, the emergence of African nations is a clear trend.
     </div>""", unsafe_allow_html=True
)


st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left;">
       Climbing the ladder
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:20px; font-weight:bold; color:gray;'>Regional breakdown of teams progressing to the knockout stages</span>", 
    unsafe_allow_html=True
)
teams = pd.read_csv("data/teams_updated.csv",index_col=0)
knockout = teams[teams["Rank"].isin(["1","2","3","4","Quarter Final","Round of 16"])]
region_representation = knockout.groupby(['Year', 'Region']).agg(
    Teams_count=('Team', 'size'),
    Team_List=('Team', lambda x: ', '.join(x))).reset_index()

region_colors = {
    "UEFA (Europe)": "#003366",  # Dark Blue
    "CONCACAF (North and Central America)": "#FFA500",  # Orange
    "AFC (Asia)": "#FFD700",  # Yellow
    "CAF (Africa)": "#ADD8E6",  # Light Blue
    "CONMEBOL (South America)": "#008000",  # Green
    "OFC (Oceania)": "#800080" 
}

#Graph 6 - Bar chart: Teams progressing to knockout stages

fig_4= px.bar(
    region_representation,
    x='Year',
    y='Teams_count',
    color='Region',
    template='plotly_white',
    color_discrete_map=region_colors,
    hover_data={"Region":True,
                "Team_List":True,
                "Teams_count":True},
    labels={"Team_List":"Teams","Teams_count":"Number of Teams"}
)

fig_4.update_xaxes(
    title='',
    tickmode='array',
    tickvals=region_representation['Year'].unique(),
    showgrid=True
)
fig_4.update_yaxes(title='Number of teams', showgrid=True)
fig_4.update_layout(
    barmode='stack',
    font=dict(
        family="Helvetica",
        size=14,
        color="black"
    ),
    width=1200,
    height=500,
    legend=dict(
        orientation="h",  
        yanchor="bottom",  
        y=1.05,            
        xanchor="left",  
    ),
    yaxis=dict(showgrid=True),
    xaxis=dict(showgrid=False)
)
st.plotly_chart(fig_4, use_container_width=True)

st.markdown(
    """
    <div style="text-align: left; font-size: 22px;">
    What has become abundantly clear in recent years is that women's football viewership on the rise. Stadium attendance for the WWC has fluctuated
    due to lack of vision and marketing amongst host nations (many who went to France 2019 complained that you wouldn't have known a World Cup was taking place in the country), 
    but the most recent tournament in Australia & New Zealand, marked by a highly noticeable and enthusiastic publicity campaign, was a resounding success by all measures, both in terms of stadium and TV viewership.<br><br>
     </div>""", unsafe_allow_html=True
)

col1, col2 = st.columns([2, 1])  # Two equal-width columns
with col1:
    st.image("assets/images/stadium.png", caption="New Zealand vs Norway, Matchday 1, WWC 2023. Source: FIFA")
with col2:
    st.write(
        """
        """
    )

st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left;">
       Bums on seats
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:20px; font-weight:bold; color:gray;'>Total attendance figures per World Cup, millions</span>", 
    unsafe_allow_html=True
)

df_women = pd.read_csv("data/world_cup_women_clean.csv",index_col=0)

#Graph 6 - Line Chart: Attendance
fig_8 = px.line(df_women,
              x='year',
              y='total_attendance',
              height=500,
              markers=True,
               labels={"host":"Host","num_matches":"Number of Matches","total_attendance":"Total Attendance"},
              hover_data={
                        'year': False,          
                        'host': True,        
                        'num_matches': True,   
                        'total_attendance': True}
             )
fig_8.update_xaxes(title='',tickmode='array', tickvals=[1991, 1995, 1999, 2003, 2007, 2011, 2015, 2019, 2023])
fig_8.update_yaxes(title='')  
fig_8.update_traces(mode='lines+markers', marker=dict(size=8, color='#2a76d9'))
fig_8.update_layout(
    margin={"t": 50},
    font=dict(
        family="Helvetica",  # Font style
        size=14,  # General font size
        color="black"  # Font color
    ),
    yaxis=dict(showgrid=True),
    template='plotly_white',
    showlegend=True,
    width=1200,
    height=500
)

st.plotly_chart(fig_8, use_container_width=True)

st.markdown(
        """
        <h1 style="font-size: 30px; color: black; text-align: left;">
            Record-shattering broadcasting numbers, 2023 WWC
        </h1>
        """,
        unsafe_allow_html=True,
)

left, middle, right = st.columns(3, border=True)

left.markdown("<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>10m</span><br><span style='font-size:18px;'>Viewing audience for Colombia vs. Germany in Germany, the second highest TV audience on any channel in Germany throughout 2023 and the largest FIFA Women’s World Cup viewership in the country since the tournament was hosted in Germany in 2011.</span>", 
        unsafe_allow_html=True)
middle.markdown("<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>53.9m</span><br><span style='font-size:18px;'>China produced the highest audience for a single match anywhere in the world for their group stage encounter with England.</span>", 
        unsafe_allow_html=True)
right.markdown("<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>7m</span><br><span style='font-size:18px;'>Australian audience for Australia's semi-final game against England, the most-watched television programme on record in Australia</span>", 
        unsafe_allow_html=True) 


