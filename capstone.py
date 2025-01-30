import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio


# Set up the app title and layout
st.set_page_config(
    page_title="From Margins to Main Stage: The Rise of Women's Football"
    #layout="wide",  

)

# Set Open Graph metadata using raw HTML
st.markdown(
    """
    <meta property="og:image" content="https://imgur.com/a/prag7rT" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:title" content="From Margins to Main Stage" />
    <meta property="og:description" content="A data story on the rise of women's football." />
    <meta property="og:url" content="https://frommarginstomainstage.streamlit.app/" />
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Style for title section */
    .title-section {
        background-color: #000000; /* Black background */
        padding: 2rem;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    .title-section h1 {
        font-family: 'Helvetica-Bold';
        font-size: 2rem;
        color: #FFFFFF; /* White text */
    }
    .title-section p {
        font-size: 1.2rem;
        color: #FFFFFF; /* White text */
        margin-bottom: 3rem;
    }
    /* Centered and narrower margin for text */
    .centered-text {
        max-width: 800px;
        margin: 0 auto;  /* Center horizontally */
        text-align: left;
        font-family: 'Georgia', serif;
        line-height: 1.6;
    }
    .centered-text h1 {
        font-size: 2.5rem;
        color: #333333;
        margin-bottom: 1rem;
    }
    .centered-text p {
        font-size: 1.2rem;
        color: #666666;
        margin-bottom: 2rem;
    }
    /* Style for pull quotes */
    .pull-quote {
        background-color: #f9f9f9;
        border-left: 5px solid #2a76d9;
        padding: 1rem;
        margin: 1rem 0;
        font-style: italic;
        color: #444444;
        font-family: 'Helvetica', sans-serif;
        font-size: 24px;
    }

    /* Style for image and text section */
    .image-section img {
        width: 80%;
        height: auto;
        margin-bottom: 1rem;
    }

    .image-section .text {
        font-family: 'Arial', sans-serif;
        font-size: 1rem;
        color: #333333;
        line-height: 1.5;
    }

    /* Style for bottom-right text */
    .bottom-right-text {
        position: absolute;
        bottom: 10px;
        right: 10px;
        font-size: 1rem;
        color: #f8e86f; /* Yellow text */
        font-family: 'Georgia', serif;
    }

    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Set global font size for markdown texts */
    .markdown-text {
        font-size: 22px;  
        font-family: 'Helvetica', sans-serif; 
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and introduction
st.markdown(
    """
    <div class="title-section">
        <h1>All Eyes on the Women's Game</h1>
        <p>From Margins to Main Stage: The Rise of Women's Football</p>
    </div>
    <div class="bottom-right-text">
        <br>A Data Story by Vishaki Vijayakumar<br>
    </div>
    """,
    unsafe_allow_html=True,
)
st.image("assets/images/jamaica.png", caption="Jamaican Joy. Photograph: Anadolu Agency/Getty Images")

#Chapter 1

st.title("1 - Context Matters")
st.divider()

st.image("assets/images/dickkerrladies.png",caption="Dick, Kerr Ladies regularly played to large crowds of thousands in the 1920-21 season. Source: National Football Museum")

st.write(
    """
    The Dick, Kerr Ladies, founded in 1917 was one of the first recognised women's international teams.
    On Boxing Day, 1920  the team met St Helens Ladies at Everton's Goodison Park, drawing a record crowd for domestic women's football of 53,000 - a record that stood for 99 years.
    However, in 1921, spooked by the success of the women's game, The English Football Association, made up of about a dozen old white men, decided it was not a good idea for women to play football.
    On December 5, 1921, just under a year after the spectacularly successful match at Goodison Park, the FA banned women from using its grounds. Other countries soon followed suit.
    """
)

st.markdown(
    """
    <div class="pull-quote">
        "“There is a general feeling that football is no game for women. It is too strenous, that being the view of many famous specialists.”<br>- Sheffield Daily Telegraph, 9 Dec,1921"
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
        The Dark Ages
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:22px; font-weight:bold; color:gray;'>Timeline of Women's Football Bans by Country</span>", 
    unsafe_allow_html=True
)


data = {
    "Country": ["England", "Germany", "Brazil", "France", "Spain"],
    "Start": ["1921", "1955", "1941", "1932", "1935"],
    "End": ["1971", "1970", "1981", "1975", "1980"]
}

bans = pd.DataFrame(data)
bans["Duration"] = bans["End"].astype(int) - bans["Start"].astype(int)
bans = bans.sort_values(by="Duration", ascending=True)

#Graph 1: Bans Timeline

fig = px.timeline(
    bans,
    x_start="Start",
    x_end="End",
    y="Country",
    text="Duration",
    template="plotly_white",
    hover_data={
        "Country":False,
        "Duration":False,
        "Start": True, 
        "End": True}, 
)

fig.update_layout(
    xaxis=dict(title='',showgrid=False,tickfont=dict(size=14)),
    yaxis=dict(title="",automargin=True,tickfont=dict(size=14)), 
    template="plotly_white",
    width=1200,
    height=300,
    font=dict(
        family="Helvetica",  
        size=18, 
        color="black"),  
    showlegend=False,
    bargap=0.1
)

fig.update_traces(
    hovertemplate=(
        "<b>Start:</b> %{customdata[0]}<br>"  # Use customdata for Start
        "<b>End:</b> %{customdata[1]}<br>"    # Use customdata for End
    ),
    customdata=bans[["Start","End"]].values,
    textposition="inside",  # Places text inside the bars
    texttemplate="%{text} years",
    marker_color="#2a76d9")

st.plotly_chart(fig,use_container_width=True)

st.markdown(
    """
    <div class="pull-quote">
        "In the battle for the ball, feminine grace vanishes, body and soul inevitably suffer damage." - Deutscher Fussball Bund, 1955
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
        Late Bloomers
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:20px; font-weight:bold; color:gray;'>FIFA World Cup Timeline</span>", 
    unsafe_allow_html=True
)

#Graph 2: World Cup Timeline
timeline = pd.read_csv("data/timeline.csv",index_col=0)
timeline["Tournament"] = ["Men"] * 22 + ["Women"] * 9

fig_1 = px.scatter(
    timeline,
    x="Year",
    y="Tournament",
    size="Teams",
    color="Tournament",
    hover_name="Host",
    hover_data={"Year": True, "Teams": True, "Tournament": False},
    template="plotly_white",
    size_max=15,
    color_discrete_map={"Men":"#d92ace", "Women":"#2a76d9"},
)
fig_1.update_layout(
    font=dict(
        family="Helvetica",  # Font style
        size=14,  # General font size
        color="black"  # Font color
    ),
    margin={"t": 40},
    yaxis=dict(showgrid=True),
    showlegend=False,
    width=1200,
    height=200,
)
fig_1.update_xaxes(title='',showgrid=True, showline=True,linewidth=2,tickfont=dict(size=14),
        linecolor="black",tickmode='array', tickvals=[1930,1991, 1995, 1999, 2003, 2007, 2011, 2015, 2019, 2023],tickangle=90)
fig_1.update_yaxes(
    title="",
    tickmode="array",
    tickvals=["Men", "Women"],  # Adjust tick values to be based on actual y-axis categories
    ticktext=["Men's World Cup", "Women's World Cup"],  # Add corresponding labels for better clarity
    tickangle=0,
    showgrid=True,
    showline=False,
    linewidth=2,
    categoryorder="array",  # Use array to control the category order
    categoryarray=["Men", "Women"],  
    tickfont=dict(size=14)
)
fig_1.for_each_trace(
    lambda trace: trace.update(marker=dict(opacity=0.2)) if trace.name == "Men" else trace.update(marker=dict(opacity=1))
)

st.plotly_chart(fig_1,use_container_width=True)

# Chapter 2

st.title("2 - Scaling Up")
st.divider()

# Create two columns with equal width
col1, col2 = st.columns([1, 1])

# Content for the left column
with col1:
    st.markdown(
        """
        <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
            The 1991 WWC in Numbers
        </h1>
        """,
        unsafe_allow_html=True,
    )
    # Create three vertical "boxes" in the left column
    left, middle, right = st.columns(3)

    # Add text to each "box" with styling
    left.markdown(
        "<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>80</span><br><span style='font-size:14px;'>Minutes played each game</span>", 
        unsafe_allow_html=True
    )
    middle.markdown(
        "<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>1</span><br><span style='font-size:14px;'>Sponsor for the entire tournament: M&Ms</span>", 
        unsafe_allow_html=True
    )
    right.markdown(
        "<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>Zero</span><br><span style='font-size:14px;'>Number of TV channels in the US screening the final, where US beat Norway 2-1</span>", 
        unsafe_allow_html=True
    )

# Content for the right column
with col2:
    st.image(
        "assets/images/1991.png",
        caption="A ticket for the then-titled ’The Fifa Women’s World Championship For The M&Ms Cup’ which was held in China in 1991 and sponsored by Mars confectionery company. Photograph: National Football Museum",
    )



st.markdown(
    """
    <div class="pull-quote">
        “[The organisers were] afraid our ovaries were going to fall out if we played 90."<br> - USA captain April Heinrichs, 1991
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
        An increasingly global competition
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:20px; font-weight:bold; color:gray;'>Filter by year and hover over each country to view team information and placing</span>", 
    unsafe_allow_html=True
)
#  Graph 3: Map - Geographic Locations'
region_colors = {
    "UEFA (Europe)": "#003366",  # Dark Blue
    "CONCACAF (North and Central America)": "#FFA500",  # Orange
    "AFC (Asia)": "#FFD700",  # Yellow
    "CAF (Africa)": "#ADD8E6",  # Light Blue
    "CONMEBOL (South America)": "#008000",  # Green
    "OFC (Oceania)": "#800080" 
}

teams = pd.read_csv("data/teams_updated.csv",index_col=0)

teams_year = st.radio("Year",teams["Year"].unique(), horizontal=True)

fig_2 = px.choropleth(
    data_frame=teams[teams["Year"]==teams_year], 
    locations="ISO_Code", 
    projection='kavrayskiy7',
    color="Region", 
    hover_name="Team_with_Flag",
    color_discrete_map=region_colors,
    #animation_frame = "Year",
    hover_data = {'Team': False,'ISO_Code': False, 'Rank': True,'Year': True,'Manager': True },
    labels = {"Rank":"Placing"}
)

fig_2.update_layout(
    geo=dict(
        #projection_scale=5,
        showland=True,
        landcolor="rgb(243, 243, 243)",
        showocean=True,
        oceancolor="rgb(204, 255, 255)",
    ),
)

fig_2.update_layout(
    font=dict(
        family="Helvetica",  # Font style
        size=14,  # General font size
        color="black"  # Font color
    ),
    yaxis=dict(showgrid=True),
    template='plotly_white',
    showlegend=True,
    legend=dict(
        orientation="h",  # Horizontal legend
        yanchor="bottom",  # Anchor legend vertically at the bottom
        y=1.02,            # Position legend slightly above the graph
        xanchor="left",  # Center legend horizontally
        #x=0.5              # Position legend in the center
    ),
    width=1200,
    height=600,
    #margin=dict(t=50),
)

st.plotly_chart(fig_2,use_container_width=True)


container = st.container(border=True)
container.markdown("<span style='font-size:20px; font-weight:bold; '>At the next :blue[World Cup in 2027], held in Brazil, the number of teams will :blue[increase] from :blue[32 to 48], following a similar change in the Men's format.</span>", 
    unsafe_allow_html=True)


st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
       Central American and African nations benefit most
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:20px; font-weight:bold; color:gray;'>Geographical representation of teams over time by region</span>", 
    unsafe_allow_html=True
)

# Graph 4: Area chart - regional representation
teams_region = teams.groupby(['Year', 'Region']).agg(
    Teams_count=('Team', 'size'),
    Team_List=('Team', lambda x: ', '.join(x))
).reset_index()

fig_3 = px.area(
    teams_region, 
    x='Year', 
    y='Teams_count', 
    color='Region',
    hover_data={
        'Year': False,          
        'Region': True,         
        'Teams_count': True,    
        'Team_List': True       
    },
    labels={"Teams_count": "Number of Teams","Team_List":"Teams"},
    color_discrete_map=region_colors
)

# Customize the x-axis ticks for years
fig_3.update_xaxes(title='', tickmode='array', tickvals=[1991, 1995, 1999, 2003, 2007, 2011, 2015, 2019, 2023])

# Update layout
fig_3.update_layout(
    font=dict(
        family="Helvetica",  
        size=14,  
        color="black"  
    ),
    yaxis=dict(showgrid=True),
    template='plotly_white',
    showlegend=True,
    legend=dict(
        orientation="h",  # Horizontal legend
        yanchor="bottom",  # Anchor legend vertically at the bottom
        y=1.02,            # Position legend slightly above the graph
        xanchor="left",  # Center legend horizontally
        #x=0.5              # Position legend in the center
    ),
    width=1200,
    height=500,
    margin=dict(l=50, r=50, t=50, b=50),
)
# Show the plot
st.plotly_chart(fig_3,use_container_width=True)


#Chapter 3 

st.title("3 - On The Pitch")
st.divider()


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
        <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
            Squad Goals: The US Women's National Team
        </h1>
        """,
        unsafe_allow_html=True,
    )

    # Create three vertical "boxes" in the right column
    left, middle, right = st.columns(3)

    # Add text to each "box" with styling
    left.markdown(
        "<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>4</span><br><span style='font-size:14px;'>Number of World Cup Wins<br>(Rank #1)</span>", 
        unsafe_allow_html=True
    )
    middle.markdown(
        "<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>76%</span><br><span style='font-size:14px;'>Overall win percentage across WWC<br>(Rank #1)</span>", 
        unsafe_allow_html=True
    )
    right.markdown(
        "<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>142</span><br><span style='font-size:14px;'>Total goals scored<br>(Rank #1)</span>", 
        unsafe_allow_html=True
    )


st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
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

expander = st.expander("What's behind the USA's formula for success? Explore below.")
expander.write('''
    The passing of **Title IX in 1972** prevented sex-based discrimination in educational institutions, leading to....
    - Increase in girls' participation in soccer 
    - Competitive collegiate programs
    - Creation of a large talent pool for the national team
    
    Also...
    - Early and sustained investment by national soccer federation     
    - Professionalised league system dating back to 2009    
''')


st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
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

df_women = pd.read_csv("data/world_cup_women_clean.csv",index_col=0)

# Chapter 4

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
    <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
       Bums on seats
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:20px; font-weight:bold; color:gray;'>Total attendance figures per World Cup, millions</span>", 
    unsafe_allow_html=True
)
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
        <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
            Record-shattering broadcasting numbers, 2023 WWC
        </h1>
        """,
        unsafe_allow_html=True,
)

left, middle, right = st.columns(3, border=True)

left.markdown("<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>10m</span><br><span style='font-size:14px;'>Viewing audience for Colombia vs. Germany in Germany, the second highest TV audience on any channel in Germany throughout 2023 and the largest FIFA Women’s World Cup viewership in the country since the tournament was hosted in Germany in 2011.</span>", 
        unsafe_allow_html=True)
middle.markdown("<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>53.9m</span><br><span style='font-size:14px;'>China produced the highest audience for a single match anywhere in the world for their group stage encounter with England.</span>", 
        unsafe_allow_html=True)
right.markdown("<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>7m</span><br><span style='font-size:14px;'>Australian audience for Australia's semi-final game against England, the most-watched television programme on record in Australia</span>", 
        unsafe_allow_html=True) 


#Chapter 5
st.title("5 - Equality Drive")
st.divider()

st.markdown(
    """
    <div class="pull-quote">
        "One day the men in suits will understand."<br> - Ada Hegeberg, inaugural Ballon D'or winner in 2019
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
       Put Your Money Where Your Mouth Is
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:20px; font-weight:bold; color:gray;'>Prize money (USD) comparison, millions</span>", 
    unsafe_allow_html=True
)
prize_money = pd.read_csv("data/prize_money.csv",index_col=0)
prize_money = prize_money.drop(columns="Unnamed: 0")

#Graph 9 - Bar Chart: Prize Money Difference
fig_9 = px.bar(
    prize_money, 
    x='Year', 
    y='Total Prize Money (USD)', 
    color='Tournament Type', 
    barmode='stack',
    labels={'Prize Money': 'Prize Money (in millions USD)'},
    hover_data= {'Total Prize Money (USD)':True,
                 'Year':False,
                 'Tournament Type':False,
                 'Host':True},
    color_discrete_map={"Men":"#f18a9f", "Women":"#074b7c"}
  
)
fig_9.update_layout(
    font=dict(
        family="Helvetica",  # Font style
        size=14,  # General font size
        color="black"  # Font color
    ),
    yaxis=dict(showgrid=True),
    template='plotly_white',
    showlegend=True,
    width=1200,
    height=500,
)
fig_9.update_xaxes(title='',tickmode='array', tickvals=[2006, 2007,2010, 2011, 2014, 2015, 2018, 2019, 2022,2023])
fig_9.update_layout(
    yaxis=dict(title=''),
    bargap=0.1
)

st.plotly_chart(fig_9, use_container_width=True)

container = st.container(border=True)
container.markdown("<span style='font-size:20px; font-weight:bold; '>FIFA President Gianni Infantino has announced a goal to :blue[achieve equal prize money] for the men’s and women’s World Cups by :blue[2027].</span>", 
    unsafe_allow_html=True)


st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
       Who's on the Sidelines?
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:20px; font-weight:bold; color:gray;'>Gender distribution of managers across all WWCs</span>", 
    unsafe_allow_html=True
)

from plotly.subplots import make_subplots
import plotly.graph_objects as go

gender_counts = teams.groupby(['Year', 'Gender']).size().reset_index(name='Count')

#Graph 10 - Donut chart: Manager Gender Inequality

# Create subplots with an empty layout (default layout works for pie charts)
fig_10 = make_subplots(
    rows=3, cols=3, 
    subplot_titles=[str(year) for year in gender_counts['Year'].unique()],
    specs=[[{'type': 'pie'}]*3]*3  # Default subplots (no 'polar' specified)
)

# Add pie charts for each year
for i, year in enumerate(gender_counts['Year'].unique()):
    gender_data = gender_counts[gender_counts['Year'] == year]
    fig_10.add_trace(
        go.Pie(
            labels=gender_data['Gender'],
            values=gender_data['Count'],
            hole=0.3,  # Reduce the hole size to make the donut thicker (optional)
            marker=dict(colors=["#074b7c", "#f18a9f"]),
            domain=dict(x=[(i % 3) * 0.5, (i % 3) * 0.33 + 0.33],  
                        y=[(i // 3) * 0.33, (i // 3) * 0.33  + 0.33]),
            textposition='inside',  # Force text to always appear inside
            textinfo='percent',  # Display labels and percentages
            insidetextorientation='horizontal'  # Keep text horizontal inside
        ),
        row=(i//3)+1, col=(i%3)+1
    )
# Update layout and show the figure
fig_10.update_layout(
    font=dict(
        family="Helvetica", 
        size=14,  
        color="black"  
    ),
    template='plotly_white',
    showlegend=True,
    legend_title="Gender",
    width=1000,
    height=600,
    margin=dict(t=50, b=50, l=50, r=50),  
)

# Display the plot
st.plotly_chart(fig_10, use_container_width=True)


container = st.container(border=True)
container.markdown("<span style='font-size:20px; font-weight:bold; '>Since 2000, :blue[all but two] of the major women's football tournaments - the Women's World Cup, Women's Euros and the Olympics - have been won by :blue[female-coached teams]</span>", 
    unsafe_allow_html=True)



st.markdown("---")



#streamlit run capstone.py