import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
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
        background-color: #ffffff;
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


st.write("# Welcome to my data analytics visualisation project exploring the growth and development of international women's football.")


st.markdown(
    """

    **👈 Navigate through the sidebar** to explore key metrics such as
      global and regional representation, performance data, attendance figures and more.

    ## 🔍Key Questions:
    - What historical challenges has women’s football faced?
    - How global is the Women’s World Cup? How have participation rates evolved, and who has benefited most from expansion?
    - Which nations have had the most success, and what insights can we gain from their success? 
    - How can we measure competitiveness in Women’s World Cup matches? 
    - Has the level of public interest in the competition grown?
    - What inequalities persist in women’s football at the World Cup level?
      

    ## 📊 Data sources:
    - Women's World Cup match data from **Kaggle**
    - Additional Women's World Cup data web-scraped from **FBref**.
    - Prize Money and Manager Data collected from publicly available sources.
    
    ## 🛠️Tech stack
    - Programming Language: Python 
    - Libraries: Pandas, Plotly, Streamlit, BeautifulSoup
    - Visualizations: created with Plotly

"""
)



#streamlit run capstone.py