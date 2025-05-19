import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio


st.markdown(
    """
    <style>
    /* Style for pull quotes */
    .pull-quote {
        background-color: #ffffff;
        border-left: 5px solid #2a76d9;
        padding: 1rem;
        margin: 1rem 0;
        font-style: italic;
        color: #444444;
        font-size: 22px;
    }
    """,
    unsafe_allow_html=True
)


st.title("3. Standing Out from the Crowd")

st.markdown(
    """
    <div style="text-align: left; font-size: 22px;">
    Let's talk performance trends. Who's winning the thing? In fact, who's winning the thing, again and again?
    The USA are way out there in this regard, having finished in the top 4 in every World Cup except one: the most recent one.
      
     </div>""", unsafe_allow_html=True
)

st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left;">
       Cream of the crop
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:20px; font-weight:bold; color:gray;'>Most successful teams based on Top 4 placings at the WWC</span>", 
    unsafe_allow_html=True
)
# Graph 5: Horizontal Bar Chart - Team Dominance
# Filtering teams for top 4 placings over each World Cup

teams = pd.read_csv("data/teams_updated.csv",index_col=0)
teams["Year"] = teams["Year"].astype(str)

region_colors = {
    "UEFA (Europe)": "#003366",  # Dark Blue
    "CONCACAF (North and Central America)": "#FFA500",  # Orange
    "AFC (Asia)": "#FFD700",  # Yellow
    "CAF (Africa)": "#ADD8E6",  # Light Blue
    "CONMEBOL (South America)": "#008000",  # Green
    "OFC (Oceania)": "#800080" 
}

teams_filtered = teams[teams['Rank'].isin(['1', '2', '3', '4'])]  
team_counts = teams_filtered['Team'].value_counts().reset_index()
team_counts.columns = ['Team', 'Times_in_Top_4']

# Sort the teams by number of top 4 placings (descending order)

team_counts_sorted = team_counts.sort_values(by='Times_in_Top_4', ascending=False)
country_to_flag = {
    "USA": "🇺🇸",
    "Japan": "🇯🇵",
    "Brazil": "🇧🇷",
    "Sweden": "🇸🇪",
    "Norway": "🇳🇴",
    "Germany": "🇩🇪",
    "China": "🇨🇳",
    "Canada": "🇨🇦",
    "Australia": "🇦🇺",
    "England": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "France": "🇫🇷",
    "Spain": "🇪🇸",
    "Netherlands": "🇳🇱", 
}
country_to_region = {
    "USA": "CONCACAF (North and Central America)",
    "Japan": "AFC (Asia)",
    "Brazil": "CONMEBOL (South America)",
    "Sweden": "UEFA (Europe)",
    "Norway": "UEFA (Europe)",
    "Germany": "UEFA (Europe)",
    "China": "AFC (Asia)",
    "Canada": "CONCACAF (North and Central America)",
    "Australia": "AFC (Asia)",
    "England": "UEFA (Europe)",
    "France": "UEFA (Europe)",
    "Spain": "UEFA (Europe)",
    "Netherlands": "UEFA (Europe)", 
}
team_counts_sorted["Region"] = team_counts_sorted["Team"].map(country_to_region)
team_counts_sorted["Flag"] = team_counts_sorted["Team"].map(country_to_flag)


# Create a bar plot for the most successful teams
fig_5 = px.bar(team_counts_sorted, 
             x="Times_in_Top_4",
             y="Flag", 
             color="Region", 
             hover_name = "Flag",
             labels={"Times_in_Top_4": "Top 4 Placings"},
             color_discrete_map=region_colors,
             hover_data = {"Team":False,"Flag":False},
             category_orders={"Flag": team_counts_sorted["Flag"].tolist()},
             orientation="h",
             text="Team"  # Add the team name as text
)

# Adjust text position and layout
fig_5.update_traces(
    textposition="inside", 
    textfont=dict(size=12, color="white")  
)   
fig_5.update_yaxes(
    tickfont=dict(size=20)  
)
fig_5.update_layout(
    font=dict(
        family="Helvetica",  # Font style
        size=16,  # General font size
        color="black"  # Font color
    ),
    yaxis=dict(showgrid=False),
    xaxis=dict(showgrid=True),
    template='plotly_white',
    showlegend=True,
    legend=dict(
        orientation="h",  
        yanchor="bottom",  
        y=1.02,            
        xanchor="left",  
                     
    ),
    margin=dict(t=50),
    width=1200,
    height=500,
    xaxis_title="",
    yaxis_title="Number of Top 4 placings",
    bargap=0.1
)

st.plotly_chart(fig_5,use_container_width=True)

winners =  teams[teams["Rank"].isin(["1"])]
winner_counts = winners["Team"].value_counts().reset_index()
winner_counts.columns = ["Team","Wins"]
winner_counts["Team"] = winner_counts["Team"].map(country_to_flag)
winner_counts = winner_counts.sort_values(by="Wins",ascending=False)

st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left;">
       USA leads the way
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:20px; font-weight:bold; color:gray;'>World Cup Winners, 1991-2023</span>", 
    unsafe_allow_html=True
)


fig_5_a = px.bar(winner_counts, x='Wins',
             y='Team',
             height=300
            )
fig_5_a.update_xaxes(title="",tickmode='linear', dtick=1)
fig_5_a.update_yaxes(tickfont=dict(size=20))

fig_5_a.update_layout(
    yaxis=dict(showgrid=True),
    template='plotly_white',
    showlegend=True,
    width=1000,
    height=600
)

st.plotly_chart(fig_5_a,use_container_width=True)


st.markdown(
    """
    <div style="text-align: left; font-size: 22px;">
    
    A few teams have had periods of success, such as Germany's consecutive wins in the 2003 and 2007, and Sweden's three top 3 placings across four editions of the tournament, but 
    the USA's consistency is unrivalled.

    From the dropdown box below, you can select a team to view their placings across all the World Cups they have been participated in.

     </div>""", unsafe_allow_html=True
)


team_names = sorted(teams["Team"].unique())
df_rankings = teams[["Team","Rank","Year"]]

selected_team = st.selectbox("Choose a team", team_names)

team_data = df_rankings[df_rankings["Team"] == selected_team].sort_values("Year")

st.dataframe(team_data)

st.markdown(
    """
    <div style="text-align: left; font-size: 22px;">
    What is behind the USA's formula for success? The passing of Title IX in 1972 prevented sex-based discrimination in educational institutions, leading to increased girls' participation in soccer,
    competitive collegiate programs, and the creation of a large talent pool for the national team. An progressive approach to gender equality in sport and education.. and voila!

     </div>""", unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align: left; font-size: 22px;">
        


     </div>""", unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1])  

# Left column content
with col1:
    st.image(
        "assets/images/US_cele.png", 
        caption="The USWNT celebrating their World Cup Victory in 2019. Source: Getty Images"
    )

# Right column content
with col2:
    st.markdown(
        """
        <h1 style="font-size: 30px; color: black; text-align: left;">
            Squad Goals: The US Women's National Team
        </h1>
        """,
        unsafe_allow_html=True,
    )

    # Create three vertical "boxes" in the right column
    left, middle, right = st.columns(3)

    # Add text to each "box" with styling
    left.markdown(
        "<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>4</span><br><span style='font-size:16px;'>Number of World Cup Wins<br>(Rank #1)</span>", 
        unsafe_allow_html=True
    )
    middle.markdown(
        "<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>76%</span><br><span style='font-size:16px;'>Overall win percentage across WWC<br>(Rank #1)</span>", 
        unsafe_allow_html=True
    )
    right.markdown(
        "<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>142</span><br><span style='font-size:16px;'>Total goals scored<br>(Rank #1)</span>", 
        unsafe_allow_html=True
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
knockout = teams[teams["Rank"].isin(["1","2","3","4","Quarter Final","Round of 16"])]
region_representation = knockout.groupby(['Year', 'Region']).agg(
    Teams_count=('Team', 'size'),
    Team_List=('Team', lambda x: ', '.join(x))).reset_index()

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

#Calculating average goal difference per World Cup
matches = pd.read_csv("data/matches.csv",index_col=0)
matches["goal_difference"] = round(abs(matches['home_score'] - matches['away_score']),1)
goal_diff = matches.groupby("Year")["goal_difference"].mean().round(1).reset_index()

#Graph 7 - Average Goal Difference over time
fig_6 = px.line(goal_diff,
              x='Year',
              y='goal_difference',
              title='Average Goal Difference Over Time',
              labels={"goal_difference":"Goal Difference"},
              hover_data = {"goal_difference": True,'Year': False},
              hover_name="Year"
             )
fig_6.update_traces(mode='lines+markers', marker=dict(size=8, color='#2a76d9'))
fig_6.update_layout(
    title={
        "text": "Closing the gap<br><span style='font-size:14px; font-weight:normal; color:gray;'>Average Goal Difference per tournament</span>",
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
    xaxis_title="",
    yaxis_title="Goal Difference",
    yaxis=dict(showgrid=True),
    xaxis=dict(showgrid=False)
)
fig_6.update_xaxes(title='',tickmode='array', tickvals=[1991, 1995, 1999, 2003, 2007, 2011, 2015, 2019, 2023])

st.plotly_chart(fig_4, use_container_width=True, key="knockout_stage")
col1, col2 = st.columns(2)


matches['is_draw'] = matches['home_score'] == matches['away_score']
draw_stats = matches.groupby('Year').agg(
    total_games=('is_draw', 'size'),
    total_draws=('is_draw', 'sum')
).reset_index()

# Calculate percentage of draws
draw_stats['percent_draws'] = round((draw_stats['total_draws'] / draw_stats['total_games']) * 100,2)
draw_stats['percent_non_draws'] = 100 - draw_stats['percent_draws']

# Reshape data for stacked bar plot
draw_stats_melted = draw_stats.melt(
    id_vars='Year', 
    value_vars=['percent_draws', 'percent_non_draws'],
    var_name='Result', 
    value_name='Percentage'
)

# Rename result categories for clarity
draw_stats_melted['Result'] = draw_stats_melted['Result'].map({
    'percent_draws': 'Draw',
    'percent_non_draws': 'Non-Draw'
})

# Graph 8 - Stacked Bar chart: Number of draws
fig_7 = px.bar(
    draw_stats_melted, 
    x='Year', 
    y='Percentage', 
    color='Result', 
    title='Draw Percentage Across Each World Cup',
    labels={'Percentage': '%'},
    color_discrete_map={'Draw': '#1d4e9e', 'Non-Draw': '#2a76d9'},
    barmode='stack'
)

fig_7.update_layout(
    title={
        "text": "Stalemate Statistics<br><span style='font-size:14px; font-weight:normal; color:gray;'>Proportion of games resulting in a draw</span>",
        "font": {
            'family': "Helvetica-Bold",  # Font family
            'size': 18,                   # Font size
            'color': "black",             # Font color
        },
         "x": 0, 
        "xanchor": "left" 
    },
    font=dict(
        family="Helvetica",  # Font style
        size=12,  # General font size
        color="black"  # Font color
    ),
    yaxis=dict(showgrid=True),
    template='plotly_white',
    showlegend=True,
    width=600,
    height=400,
    xaxis_title="",
    yaxis_title="Percentage of Games (%)",
)

fig_7.update_xaxes(title='',tickmode='array', tickvals=[1991, 1995, 1999, 2003, 2007, 2011, 2015, 2019, 2023])

# Average Goal Difference
with col1:
    st.plotly_chart(fig_6, use_container_width=True, key="goal_difference")

# Draw percentage
with col2:
    st.plotly_chart(fig_7, use_container_width=True, key="draw_percentage")


st.title("4 - All Eyes on the Women's Game")
st.divider()

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
