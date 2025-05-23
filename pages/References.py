import streamlit as st 
import pandas as pd
import plotly.express as px
import plotly.io as pio


#Chapter 5
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

st.title("References")


st.link_button("Kaggle Dataset containing FIFA Women's World Cup 1991 - 2023 match results", "https://www.kaggle.com/datasets/piterfm/football-fifa-womens-world-cup-1991-2023?select=matches_1991_2023.csv")

st.link_button("FBref for detailed match statistics", "https://fbref.com/en/comps/106/history/Womens-World-Cup-Seasons")

st.link_button("Article on the history of the Women's World Cup, National Football Museum", "https://artsandculture.google.com/story/the-fascinating-history-of-the-women-s-world-cup-nationalfootballmuseum/yQXhGYa-UKS_Lw?hl=en")

st.link_button("FIFA Report on the Impact of the FIFA Women's World Cup Australia & New Zealand 2023", "https://artsandculture.google.com/story/the-fascinating-history-of-the-women-s-world-cup-nationalfootballmuseum/yQXhGYa-UKS_Lw?hl=en")

st.link_button("Women’s Sport Trust figures on women’s sport viewership", "https://www.womenssporttrust.com/latest-research-from-womens-sport-trust-reveals-fans-are-watching-barclays-womens-super-league-matches-for-longer-than-ever-before/")

st.link_button("A Woman's Game: The Rise, Fall, and Rise Again of Women's Football by Suzanne Wrack", "https://www.amazon.co.uk/Womans-Game-Again-Womens-Football/dp/1783352159")


st.title("Tech Stack")

st.markdown(
    """
    
        <div style="text-align: left; font-size: 22px;">

This app was made exclusively using Python and its related libraries: 

  - Pandas: web-scraping, data cleaning and manipulation.
  - Streamlit: interactive app interface.
  - Plotly: interactive data visualizations.

      </div>""", unsafe_allow_html=True
) 