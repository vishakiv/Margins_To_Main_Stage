import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio


st.markdown(
    """
    <style>
    .pull-quote {
        border-left: 5px solid #2a76d9;
        padding: 1rem;
        margin: 1rem 0;
        font-style: italic;
        color: #444444;
        font-size: 22px;
    }
    .text {
        text-align: left;
        font-size: 22px;
    }
    .graph-title {
        font-size: 30px;
        font-weight: bold;
        color: black; 
        text-align: left;
    } 
    .graph-subtitle {
        font-size:22px;
        font-weight:bold;
        color:gray;
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

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
team_names = sorted(teams["Team"].unique())
df_rankings = teams[["Team", "Rank", "Year"]].copy()

rank_order = [
    '1', '2', '3', '4',
    'Semi Final',
    'Quarter Final',
    'Round of 16',
    'Group Stage',
    'Did Not Qualify'
]

# Prepare data
df_rankings['Rank'] = pd.Categorical(df_rankings['Rank'], categories=rank_order, ordered=True)
df_rankings['Year'] = df_rankings['Year'].astype(int)
world_cup_years = list(range(1991, 2024, 4))

# Team selection
selected_team = st.selectbox("Choose a team", team_names)

# Filter and reindex to include all WC years
team_df = df_rankings[df_rankings["Team"] == selected_team]
team_df = team_df.set_index("Year").reindex(world_cup_years).reset_index()
team_df["Team"] = selected_team
team_df["Rank"] = team_df["Rank"].fillna("Did Not Qualify")

# Plot with Seaborn
plt.figure(figsize=(10, 5))
sns.stripplot(data=team_df, x='Year', y='Rank', size=10,color="#E34234")
plt.xticks(world_cup_years)
plt.title(f"{selected_team}'s Previous Tournaments")
plt.xlabel("")
plt.ylabel("")
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


# Display in Streamlit
st.pyplot(plt)



# # Input data
# team_names = sorted(teams["Team"].unique())
# df_rankings = teams[["Team", "Rank", "Year"]].copy()
# df_rankings["Year"] = df_rankings["Year"].astype(int)

# # Streamlit selectbox
# selected_team = st.selectbox("Choose a team", team_names)

# # Define rank order
# rank_order = [
#     '1', '2', '3', '4',
#     'Semi Final',
#     'Quarter Final',
#     'Round of 16',
#     'Group Stage',
#     'Did Not Qualify'
# ]

# world_cup_years = list(range(1991, 2024, 4))

# # Filter selected team and reindex with all World Cup years
# team_data = df_rankings[df_rankings["Team"] == selected_team].set_index("Year").reindex(world_cup_years).reset_index()

# # Fill in missing team name and missing rank values
# team_data["Team"] = selected_team
# team_data["Rank"] = pd.Categorical(team_data["Rank"], categories=rank_order, ordered=True)
# team_data["Rank"] = team_data["Rank"].fillna("Did Not Qualify")
# team_data["dummy"] = False

# # Dummy rows to force y-axis to show all rank levels
# dummy = pd.DataFrame({
#     "Year": [world_cup_years[0]] * len(rank_order),
#     "Rank": pd.Categorical(rank_order, categories=rank_order, ordered=True),
#     "Team": [selected_team] * len(rank_order),
#     "dummy": [True] * len(rank_order)
# })

# # Combine real data and dummy data
# plot_df = pd.concat([team_data, dummy], ignore_index=True)

# # Split out real data for coloring
# real_data = plot_df[plot_df["dummy"] == False]
# colors = ['grey' if r == 'Did Not Qualify' else 'blue' for r in real_data['Rank']]

# # Plot real data
# fig = px.scatter(
#     real_data,
#     x='Year',
#     y='Rank',
#     text='Rank'
# )

# # Add invisible dummy points
# invisible = px.scatter(
#     plot_df[plot_df["dummy"] == True],
#     x='Year',
#     y='Rank',
#     opacity=0
# ).data[0]

# fig.add_trace(invisible)

# # Update trace styles
# fig.update_traces(marker=dict(size=12, color=colors), textposition='top center')

# # Layout settings
# fig.update_layout(
#     xaxis=dict(
#         tickmode='array',
#         tickvals=world_cup_years,
#         range=[min(world_cup_years) - 1, max(world_cup_years) + 1],
#         title='World Cup Year'
#     ),
#     yaxis=dict(
#         categoryorder='array',
#         categoryarray=rank_order[::-1],  # Highest at top
#         tickmode='array',
#         tickvals=rank_order[::-1],
#         title='Rank'
#     ),
#     title=f"{selected_team}'s World Cup Placings Over Time",
#     showlegend=False
# )

# Show plot
#st.plotly_chart(fig, use_container_width=True)


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

