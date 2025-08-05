import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
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


st.title("III. Standing Out from the Crowd")

st.markdown(
    """
    <div style="text-align: left; font-size: 22px;">
    Before evaluating the competitiveness of the World Cup, let's talk broad performance trends. Who's winning the thing? In fact, who's winning the thing, again and again?
    The USA are way out there. They have won the World Cup a record 4 times, and have finished in the top 4 in every World Cup except one — the most recent one in 2023.
    No other country comes close to their level of success.<br>
    <br>
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
       Cream of the crop
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:20px; font-weight:bold; color:gray;'>Most successful teams based on number of Top 4 placings at the WWC</span>", 
    unsafe_allow_html=True
)
# Graph 5: Horizontal Bar Chart - Team Dominance
# Filtering teams for top 4 placings over each World Cup

teams = pd.read_csv("data/teams_updated.csv",index_col=0)
teams["Year"] = teams["Year"].astype(str)

teams_filtered = teams[teams['Rank'].isin(['1', '2', '3', '4'])]  
team_counts = teams_filtered["Team"].value_counts()\
    .reset_index()\
    .rename(columns = {"Team":"Team","count":"Times_in_top_4"})

country_to_flag = {
    "USA": "USA🇺🇸",
    "Japan": "Japan 🇯🇵",
    "Brazil": "Brazil 🇧🇷",
    "Sweden": "Sweden 🇸🇪",
    "Norway": "Norway 🇳🇴",
    "Germany": "Germany🇩🇪",
    "China": "China 🇨🇳",
    "Canada": "Canada 🇨🇦",
    "Australia": "Australia 🇦🇺",
    "England": "England 🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "France": "France 🇫🇷",
    "Spain": "Spain 🇪🇸",
    "Netherlands": "Netherlands 🇳🇱", 
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
team_counts["Region"] = team_counts["Team"].map(country_to_region)
team_counts["Country_Flag"] = team_counts["Team"].map(country_to_flag)

region_colors = {
    "UEFA (Europe)": "#003366",  # Dark Blue
    "CONCACAF (North and Central America)": "#FFA500",  # Orange
    "AFC (Asia)": "#FFD700",  # Yellow
    "CAF (Africa)": "#ADD8E6",  # Light Blue
    "CONMEBOL (South America)": "#008000",  # Green
    "OFC (Oceania)": "#800080" 
}

# Create a bar plot for the most successful teams
fig_5 = px.bar(team_counts, 
             x="Times_in_top_4",
             y="Country_Flag", 
             color="Region", 
             hover_name = "Team",
             labels={"Times_in_top_4": "Number of Top 4 Placings"},
             color_discrete_map=region_colors,
             hover_data = {"Team":False,"Country_Flag":False},
             category_orders={"Country_Flag": team_counts["Country_Flag"].tolist()},
             orientation="h"
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
    yaxis_title="",
    bargap=0.2
)

st.plotly_chart(fig_5)

winner_counts = teams[teams["Rank"].isin(["1"])]\
    ["Team"].value_counts() \
    .reset_index()\
    .rename(columns={"Team":"Team","count":"Wins"})

winner_counts["Country_Flag"] = winner_counts["Team"].map(country_to_flag)

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
             y='Country_Flag',
             category_orders={"Country_Flag": winner_counts["Country_Flag"].tolist()}
            )
fig_5_a.update_xaxes(title="",tickmode='linear', dtick=1)

fig_5_a.update_layout(
    font=dict(
        family="Helvetica",  # Font style
        size=16,  # General font size
        color="black"  # Font color
    ),
    yaxis=dict(showgrid=False),
    xaxis=dict(showgrid=True),
    template='plotly_white',
    width=1200,
    height=500,
    yaxis_title="",
    bargap=0.1
)

st.plotly_chart(fig_5_a)

st.markdown(
    """
    <div style="text-align: left; font-size: 22px;">
    What is behind the USA's formula for success? The passing of Title IX in 1972 prevented sex-based discrimination in educational institutions, leading to increased girls' participation in soccer,
    competitive collegiate programs, and the creation of a large talent pool for the national team. An progressive approach to gender equality in sport and education.. and voila!<br> 
    <br>
     </div>""", unsafe_allow_html=True
)

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
selected_team = st.selectbox("Choose a team to view their World Cup placings over time", team_names)

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


st.markdown(
    """
    <div style="text-align: left; font-size: 22px;">

    Some notable performance highlights include Germany's consecutive wins in 2003 and 2007, 
    and Sweden's three semi-final placings across the last 4 tournaments. However, the USA's consistency is unrivalled.
    Their round of 16 exit in 2023, while unexpected by the general public, was not a shock in some quarters, and signalled a wave of generational change under new coach Emma Hayes.
    Their subsequent gold medal in the 2024 Olympics tournament has demonstrated the effectiveness of that transition, and 
    the USA are in a strong position to show at the 2027 World Cup that their 2023 placing was just a blip.

     </div>""", unsafe_allow_html=True
)


