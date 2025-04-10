import streamlit as st 
import pandas as pd
import plotly.express as px
import plotly.io as pio


#Chapter 5
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

