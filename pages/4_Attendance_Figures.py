import streamlit as st 
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Chapter 4
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