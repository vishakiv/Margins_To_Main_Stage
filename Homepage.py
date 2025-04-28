import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio


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
    /* --- TITLE SECTION --- */
    .title-section {
        background-color: #000000;
        padding: 2rem;
        text-align: center;
    }
    .title-section h1 {
        font-size: 2rem;
        color: #ffffff;
        font-family: 'Georgia', serif;
    }
    .title-section p {
        font-size: 1.2rem;
        color: #ffffff;
    }

    /* --- MAIN TEXT CONTAINER --- */
    .centered-text {
        max-width: 800px;
        margin: auto;
        text-align: left;
        font-family: 'Georgia', serif;
        line-height: 1.6;
        color: #333333;
    }

    /* --- PULL QUOTE STYLE --- */
    .pull-quote {
        border-left: 5px solid #2a76d9;
        padding-left: 1rem;
        margin: 1rem 0;
        font-style: italic;
        color: #444444;
        font-family: 'Georgia', serif;
        font-size: 1.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Title and introduction
st.markdown(
    """
    <div class="title-section">
        <h1>From Margins to Main Stage: <br>  The Rise of Women's Football</h1>
    </div>
    """,
    unsafe_allow_html=True,
)
st.image("assets/images/jamaica.png", caption="Jamaican Joy. Photograph: Anadolu Agency/Getty Images")


st.markdown(
    """
    <h2 style="text-align: center; font-size: 26px;">Welcome to my data analytics visualisation project exploring the growth and development of international women's football.</h2>
        <div style="text-align: left; font-size: 22px;">
   
    ## 🔍Key Questions:
    - What historical challenges has women’s football faced globally?
    - How global is the Women’s World Cup? 
    - Which nations have had the most success, and what insights can we gain from their success? 
    - How can we measure competitiveness in Women’s World Cup matches? 
    - Has the level of public interest in the competition grown?
    - What inequalities persist in women’s football at the World Cup level?
      

    ## 📊 Data sources:
    - Women's World Cup match data from **Kaggle**
    - Additional Women's World Cup data web-scraped from **FBref**.
    - Prize Money and Manager Data collected from publicly available sources.
    
    ## 🛠️Tech stack:
    - Programming Language: Python 
    - Libraries: Pandas, Plotly, Streamlit, Matplotlib, BeautifulSoup
    - Visualizations: created with Plotly
      </div>""", unsafe_allow_html=True
)