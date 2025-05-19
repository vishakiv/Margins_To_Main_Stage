import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

st.markdown(
    """
    <style>
    /* Style for pull quotes */
    .pull-quote {
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

st.title("II. Scaling Up the Women’s World Cup")


st.markdown(
    """
    <div style="text-align: left; font-size: 22px;">
    Considering the structural barriers put in place to prevent women from playing organised football during the mid-20th century, 
    is it any surprise that an official FIFA Women’s World Cup was only sanctioned much later and on a much smaller scale than the men’s tournament?
     </div>""", unsafe_allow_html=True
)
st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left;">
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


st.markdown(
    """
    <div style="text-align: left; font-size: 22px;">
    Two unofficial Women's World Cups had been staged previously: the 1970 Coppa del Mondo in Italy and the 1971 Campeonato de Fútbol Femenil in Mexico. These tournaments were 
    widely considered to be successful from a commercial and sporting perspective, attracting tens of thousands of spectators, but it took FIFA a further 15 years before they embraced the women's game and agreed to organise
    an official women's world championship. The inaugural FIFA Women's World Cup event, held in China in 1991, debuted with minimal fanfare, with just 12 teams and no prize money.
     </div>""", unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Create two columns with equal width
col1, col2 = st.columns([1, 1])

# Content for the left column
with col1:
    st.markdown(
        """
        <h1 style="font-size: 30px; color: black; text-align: left;">
            The 1991 WWC in Numbers
        </h1>
        """,
        unsafe_allow_html=True,
    )
    # Create three vertical "boxes" in the left column
    left, middle, right = st.columns(3)

    # Add text to each "box" with styling
    left.markdown(
        "<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>80</span><br><span style='font-size:16px;'>Minutes played each game</span>", 
        unsafe_allow_html=True
    )
    middle.markdown(
        "<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>1</span><br><span style='font-size:16px;'>Sponsor for the entire tournament: M&Ms</span>", 
        unsafe_allow_html=True
    )
    right.markdown(
        "<span style='font-size:30px; font-weight:bold; color:#2a76d9;'>Zero</span><br><span style='font-size:16px;'>Number of TV channels in the US screening the final, where US beat Norway 2-1</span>", 
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
    <div style="text-align: left; font-size: 22px;">
    Since its meagre beginnings, the size of the women’s competition has grown steadily, with the latest edition held in 2023 in 
    Australia and New Zealand expanding for the first time to 32 teams. 
    Expansion means more teams, more players on the world stage, and more role models for young girls and women across the globe. 
    As the pinnacle of international competition, the World Cup also brings eyes on the game and increased media scrutiny, which is often the catalyst for further investment in national and regional youth training programs.  
    At the next World Cup in 2027, held in Brazil, the number of teams will increase from 32 to 48, following a similar change in the Men's format.

     </div>""", unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)


st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left;">
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



st.write(
    """

    """
)

st.markdown(
    """
    <div style="text-align: left; font-size: 22px;">

    The make up of the participating teams is just as signficant as the number of teams.
    
    African representation has doubled over the last 4 editions, while 3 CONCACAF nations -  Haiti, Panama and Costa Rica - made their debuts in the 2023 tournament alone.
    And these emerging football nations are not just making up the numbers. As we will see in the next section, the most recent World Cup demonstrated that the outsiders are increasingly competitive. 
     </div>""", unsafe_allow_html=True
)


st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
       Central American and African nations benefit most from expansion
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